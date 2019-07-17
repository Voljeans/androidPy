import os
import sys
from threading import Thread


class Emulator(Thread):
	def __init__(self,emulator,adb):
		Thread.__init__(self);
		self.emulator = emulator;
		self.adb = adb;
	
	def run(self):
		os.system(self.adb+' devices')
		os.system(self.emulator + ' -list-avds')
		device = input("Selectionner un device: ")
		os.system(self.emulator + ' -avd '+ device+' -writable-system')
		sys.exit();