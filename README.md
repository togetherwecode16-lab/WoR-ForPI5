# Guide
Download UEFI/EFI.zip
Format a storage device that you will not use for Windows as FAT32
Copy files from the UEFI/EFI.zip to the storage device
Try booting the storage device on your Pi 5 and see the uefi do its magic!
Download the python script Download_ESD_Image.py
Install python on your primary pc and then run the command python (thepathoftheesddownloadfile) for windows and for linux or mac use python3 (thepathoftheesddownloadfile)
Replace (thepathoftheesddownloadfile) with your actual path to the file that you downloaded for the ESD Image download
Then install WoR
Flash the ESD image to a storage drive separate from your UEFI flashed storage device choose pi 2/3 when it asks pi model(DO NOT USE A MICRO SD CARD USE GOOD HHD/SDD)
Boot if you see No options or any error wait a few secs then press esc
Select the Boot maintenance manager then click Boot devices/Boot Options/Similar
Click the storage device that you flashed the esd image to
You should see 2 Folders at bottom Microsoft and Boot you have to open Boot but not just directly first select Microsoft then click the Boot that appears after.
Select it click commit changes then reboot the PI.
