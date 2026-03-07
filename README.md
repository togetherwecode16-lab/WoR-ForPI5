# Guide
Download UEFI.zip
Format a storage device that you will not use for Windows as FAT32
Copy files from the UEFI.zip to the storage device
Try booting the storage device on your Pi 5 and see the uefi do its magic!
Download the python script Download_ESD_Image.py
Install python on your primary pc and then run the command python (thepathoftheesddownloadfile) for windows and for linux or mac use python3 (thepathoftheesddownloadfile)
Replace (thepathoftheesddownloadfile) with your actual path to the file that you downloaded for the ESD Image download
Then install Heslo WinToUSB on a windows vm/machine(Free version can be used, it only supports installing the home edition but we can switch to pro edition later after windows boots.)
Select Windows to go
Select the esd image as your installation source
Select the destination drive as the storage device you are using to install windows and make sure its not the one used for uefi
Flash the ESD image to a storage device u didnt use for uefi using Heslo WinToUSB
Boot, if you see No options or any error wait a few secs then press esc
Select the Boot maintenance manager then click Boot devices/Boot Options/Similar
Click the storage device that you flashed the esd image to its most likely 3rd.
You should see a folder named EFI at bottom open it you will see 2 folders Microsoft and Boot select Boot then select bootaa sometimes there could be something after bootaa like bootaa.efi
Cick commit changes then reboot the PI.
Go through windows oobe steps.
(Only if you want to switch to pro) open settings in windows go to System > Activation > Change product key and enter VK7JG-NPHTM-C97JM-9MPGT-3V66T.
Click Activate
Wait for it to finish.
