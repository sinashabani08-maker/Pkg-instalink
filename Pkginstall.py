#coded N3737GS 《■》KINGHacker《■》

#module of script
import os
import sys
import time

#_color
red = '\033[31m'
reset = '\033[0m'
green = '\033[32m'

#banner
print(f"""{red}
  ____    _  __   ____                                                        

 |  _ \  | |/ /  / ___|                                                       

 | |_) | | ' /  | |  _                                                        

 |  __/  | . \  | |_| |                                                       

 |_|     |_|\_\  \____| {green}                                                      

  ___   _   _   ____    _____      _      _       _       ___   _   _    ____ 

 |_ _| | \ | | / ___|  |_   _|    / \    | |     | |     |_ _| | \ | |  / ___|

  | |  |  \| | \___ \    | |     / _ \   | |     | |      | |  |  \| | | |  _ 

  | |  | |\  |  ___) |   | |    / ___ \  | |___  | |___   | |  | |\  | | |_| |

 |___| |_| \_| |____/    |_|   /_/   \_\ |_____| |_____| |___| |_| \_|  \____|

                                                                              

------------------------------------------------

{reset}
""")
os.system('pkg update -y')
os.system('pkg upgrade -y')
time.sleep(8)
os.system('y')
time.sleep(5)
os.system('y')
time.sleep(5)
os.system('y')
packages = [
    'git',
    'python',
    'python2',
    'python3',
    'curl',
    'wget',
    'nano',
    'vim',
    'bash',
    'openssh',
    'clang',
    'make',
    'pkg-config',
    'libffi-dev',
    'libcrypt-dev',
    'libssl-dev',
    'libsqlite3-dev',
    'libjpeg-turbo-dev',
    'libpng-dev',
    'libwebp-dev',
    'libx11-dev',
    'libxext-dev',
    'libxrender-dev',
    'libxrandr-dev',
    'libxi-dev',
    'libxinerama-dev',
    'libxkbcommon-dev',
    'libxkbcommon-x11-dev',
    'gcc',
    'ruby',
    'nodejs',
    'php',
    'perl',
    'unzip',
    'zip',
    'tar',
    'fish',
    'proot', 
    'termux-tools',
    ]
for package in packages:
    os.system(f'pkg install {package} -y')

