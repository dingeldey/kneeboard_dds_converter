"""
Collection of functions to convert a picture to
a dds which can be used as a falcon bms kneeboard texture.
"""
import os.path
from wand import image as WandImage
from PIL import Image as PILImage
import traceback


def convert_to_kneeboard(file_name: str, kneeboard_page: int, out_dir: str, logger=None):
    """
    :param file_name: Kneeboard png to be converted
    :param kneeboard_page:  which kneeboard page shall it become
    :param out_dir: path to which dds is written.
    :param logger: logger object which supports logger.info / logger.error and logger.debug
    :return: None

    This method resizes the png to 2048x2048 pixels as required by BMS before it converts to dds. So the
    closer you pick the values the better the result will be.
    """

    # HACK: I do not exactly know how many pages should be replaced, but before writing over needed data, I chose 4 for now.
    # If you run into this restriction, we will have to figure it out :)
    assert 0 < kneeboard_page < 6
    tmp_file = os.path.join(out_dir, "tmp.png").replace("\\", "/")
    with PILImage.open(file_name) as img:
        resized_image = img.resize((2048, 2048))
        # Save the cropped image
        resized_image.save(tmp_file)

    with WandImage.Image(filename=tmp_file) as img:
        page1 = 7982
        page = page1 - 1 + kneeboard_page
        img.compression = 'dxt5'
        dds_file = os.path.join(out_dir, str(page) + '.dds')
        if logger is not None:
            logger.info(f"create kneeboard {dds_file}")
        img.save(filename=dds_file)

    if os.path.exists(tmp_file):
        if logger is not None:
            logger.info("Removing tmp.png")
        os.remove(tmp_file)


if __name__ == "__main__":
    import glob
    files = glob.glob('./*.png')
    files = files + glob.glob('./*.jpg')

    for i, file in enumerate(files):
        try:
            convert_to_kneeboard(file, i+1, './')
        except Exception as e:
            print(str(e))
            print("\n".join(traceback.TracebackException.from_exception(e).format()))