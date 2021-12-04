conda activate kneeboard_dds_converter

# --paths E:\programme\miniconda\pkgs\openssl-1.1.1l-h8ffe710_0\Library\bin: This allows installer to pack required DDLs like _ssl
pyinstaller.exe -F -y --paths E:\programme\miniconda\pkgs\openssl-1.1.1l-h8ffe710_0\Library\bin convert_to_kneeboard.py 

rm -r .\build
rm -r .\convert_to_kneeboard.spec

New-Item -Path ".\" -Name "kneeboard_dds_converter" -ItemType "directory"
Copy-Item .\README.md -Destination ".\kneeboard_dds_converter"
Copy-Item -Path ".\dist\convert_to_kneeboard.exe" -Destination ".\kneeboard_dds_converter" -Recurse

 & 'C:\Program Files\7-Zip\7z.exe' a -mx9 -sfx .\release\kneeboard_dds_converter.exe kneeboard_dds_converter
 & 'C:\Program Files\7-Zip\7z.exe' a -t7z .\release\kneeboard_dds_converter.7z kneeboard_dds_converter
rm -r kneeboard_dds_converter
