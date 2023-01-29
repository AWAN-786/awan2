import os

os.system('git pull')

from os import path,system

from platform import uname

bt=uname().machine.lower()

if 'aarch' in bt:

    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')

    if path.isfile("awan2.so"):

        awan2()
















