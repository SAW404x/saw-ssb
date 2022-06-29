import platform
import os, platform
os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://instagram.com/jb1lr?igshid=YmMyMTA2M2Y=")
b = platform.architecture()[0]
if b == '64bit':
    import SSB
elif b == '32bit':
    print("32bit Not Supported! Sorry")
