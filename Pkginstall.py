#coded N3737GS 《KINGHacker》《sina》

#module of script
import os
import sys
import time
import random

#banner of script
print ('                KINGHacker♤SINA♤              ')

os.system("pkg update && pkg upgrade")
os.system("pkg install python")
os.system("pkg install python2")
os.system("pkg install git")
os.system("pkg install wget")
os.system("pkg install curl")
os.system("pkg install nano")
os.system("pkg install vim")
os.system("pkg install openssh")
os.system("pkg install clang")
os.system("pkg install make")
os.system("pkg install gcc")
os.system("pkg install python3")
os.system("pkg install ruby")
os.system("pkg install nodejs")
os.system("pkg install php")
os.system("pkg install perl")
os.system("pkg install unzip")
os.system("pkg install zip")
os.system("pkg install tar")
os.system("pkg install fish")
os.system("pkg install proot")
os.system("pkg install termux-tools")

# Install all Termux tools

import os

# Update package list
os.system('pkg update -y')

# Upgrade installed packages
os.system('pkg upgrade -y')

# Install essential packages
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
    ]
for package in packages:
    os.system(f'pkg install {package} -y')

