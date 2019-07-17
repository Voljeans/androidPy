import os
import time
import subprocess
from threading import Thread

class Playstore(Thread):
	def __init__(self,emulator,adb,playstore):
		Thread.__init__(self);
		self.emulator = emulator;
		self.adb = adb;
		self.playstore = playstore;
	
	def run(self):
		os.system(self.adb + ' wait-for-device');
		print("Connexion reussit...");
		while 1:
			if subprocess.run(self.adb +" shell getprop sys.boot_completed", stdout=subprocess.PIPE).stdout.decode('utf-8') == '1\r\n':
				print("Démarrage fini...")
				break;
			time.sleep(1)

		os.system(self.adb + ' root');
		os.system(self.adb + ' remount');
		os.system(self.adb + ' push '+ self.playstore + ' /system/priv-app/');
		os.system(self.adb + ' shell stop');
		os.system(self.adb + ' shell start');