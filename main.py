import os
from emulator import Emulator
from playstore import Playstore
emulator = '"C:\\Users\\<USERNAME>\\AppData\\Local\\Android\\Sdk\\emulator\\emulator.exe"'
adb = "adb.exe"
playstore = '"Phonesky.apk"'

thread_emu = Emulator(emulator,adb);
thread_play = Playstore(emulator,adb,playstore);
thread_emu.start();
thread_play.start();
thread_play.join();
thread_emu.join();
