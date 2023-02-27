"""
Collection of functions to convert a picture to
a dds which can be used as a falcon bms kneeboard texture.
"""
import os.path
from wand import image as WandImage
from PIL import Image as PILImage
import traceback
from submodules.python_core_libs.logging.project_logger import Log
from wand import image


def convert_to_kneeboard(dest_dir: str, file_name: str, kneeboard_page: int, out_dir: str, logger=None):
    """
    :param dest_dir: destination directory where the dds goes in the end
    :param file_name: Kneeboard png to be converted
    :param kneeboard_page:  which kneeboard page shall it become
    :param out_dir: path to which dds is written.
    :param logger: logger object which supports logger.info / logger.error and logger.debug
    :return: None

    This method resizes the png to 2048x2048 pixels as required by BMS before it converts to dds. So the
    closer you pick the values the better the result will be.
    """

    logger.info(f"Processing {file_name}")

    # HACK: I do not exactly know how many pages should be replaced, but before writing over needed data, I chose 17 for now.
    # If you run into this restriction, we will have to figure it out :)
    assert 0 < kneeboard_page < 17
    with PILImage.open(file_name) as img:
        resized_image = img.resize((1024, 2048))
        # Save the cropped image
        resized_image.save(file_name)

    page1 = 7982
    page = page1 - 1 + kneeboard_page
    bkp_dds = os.path.join(dest_dir, str(page) + '.dds_bkp')
    logger.info(f"Trying to open original dds {bkp_dds}")
    with image.Image(filename=bkp_dds) as left:
        img.compression = "no"
        with image.Image(filename=os.path.join(out_dir, str(kneeboard_page) + '.png')) as right:
            right.resize(1024, 2048)
            with image.Image(width=2048, height=2048) as output:  # make a 2048
                output.composite(image=left, left=0, top=0)
                output.composite(image=right, left=1024, top=0)
                output.compression = 'dxt5'
                output.save(filename=os.path.join(dest_dir, str(page) + '.dds'))


if __name__ == "__main__":
    logger = Log.instance().set_up_logger("."+os.sep+"convert_to_kneeboard.log").logger
    logger = Log.instance().logger
    logger.info("Start")
    import glob
    files = glob.glob('./*.png')
    files = files + glob.glob('./*.jpg')

    for i, file in enumerate(files):
        try:
            convert_to_kneeboard(file, i+1, "."+os.sep, logger)
        except Exception as e:
            print(str(e))
            print("\n".join(traceback.TracebackException.from_exception(e).format()))

