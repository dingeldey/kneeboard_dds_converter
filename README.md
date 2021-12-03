# README

## Requirements

- install 'ImageMagick-7.1.0-13-Q16-HDRI-x64-dll.exe' in order to make that work on windows. see here https://imagemagick.org/script/download.php 

## Usage
First make sure that the images you plan to convert are in PNG or JPG format and make their size as close to 
2048x2048 pixesl as you can. The closer you match this the better the quality of the kneeboards will be.

### Usage of python script
Run with python and it will convert all the PNGs and JPGs to dds files with the appropriate size for a kneeboard.

### Usage of Release
The release comes as a self-extracting archive with .exe ending and as a 7z-file. When you run the extracted exe, all the PNGs and 
JPGs in the working directory will be converted to dds files with the appropriate size for a kneeboard.

### Output
The order of the output kneeboard pages is the order the files are found,
where when types are mixed it takes png first and jpg last.

If you want to define an order name the images like:
1.png, 2.png, and so on.