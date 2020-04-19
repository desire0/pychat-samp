import time, getpass, os, re, wmi
from os.path import getsize, isfile
from pathlib import Path
from ctypes import windll


def getUserPath():
	return Path('C:\\Users\\'+ getUserNameD() + '\\Documents\\GTA San Andreas User Files\\SAMP\\chatlog.txt')

	

def getUserNameD():
    return getpass.getuser()


def checkUserFilePathD(filepath):
	if isfile(filepath): return True
	else: raise Exception('wrong path file')



def getGTASAPID(): #Debug Function
	c = wmi.WMI ()
	prcID = 0

	for process in c.Win32_Process ():

	    if process.Name == 'gta_sa.exe':

	        prcID = process.ProcessId

	        return prcID




def getWTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time



def read_last_line(path, N):
    list_of_lines = []

    with open(path, 'rb') as read_obj:

        read_obj.seek(0, os.SEEK_END)

        buffer = bytearray()

        pointer_location = read_obj.tell()

        while pointer_location >= 0:

            read_obj.seek(pointer_location)

            pointer_location = pointer_location -1

            new_byte = read_obj.read(1)

            if new_byte == b'\n':

                list_of_lines.append(buffer.decode()[::-1])

                if len(list_of_lines) == N:

                    return list(reversed(list_of_lines))

                buffer = bytearray()

            else:

                buffer.extend(new_byte)
 
        if len(buffer) > 0:

            list_of_lines.append(buffer.decode()[::-1])
            
    return list(reversed(list_of_lines))


path = getUserPath()
#last_line = read_last_line(path, 2)[0][11:].rstrip()
#last_line = re.sub(r"(\s?\{[A-F0-9]{6}\}\s?)", "", last_line)

def formatLine():
	global last_line
	last_line = read_last_line(path, 2)[0][11:].rstrip()
	last_line = re.sub(r"(\s?\{[A-F0-9]{6}\}\s?)", "", last_line)


def copychatNormal():
	
	while True:

		if windll.user32.GetKeyState(0x2E):
			print("sending...")
			formatLine()
			time.sleep(1)
			return last_line
			break
		else:
			time.sleep(0.1)
			


def copychatReversed():

	while True:

		if windll.user32.GetKeyState(0x2E):
			print("sending...")
			formatLine()
			time.sleep(1)
			return last_line[::-1]
			break
		else:
			time.sleep(0.1)


def copychatRemoveDigits():

	while True:

		if windll.user32.GetKeyState(0x2E):
			print("sending...")
			formatLine()
			time.sleep(1)
			return re.sub(pattern=r"\d", repl=r"", string=last_line)
			break
		else:
			time.sleep(0.1)
		


def copychatUpper():

	while True:

		if windll.user32.GetKeyState(0x2E):
			print("sending...")
			formatLine()
			time.sleep(1)
			return last_line.upper()
			break
		else:
			time.sleep(0.1)

	


def copychatLower():

	while True:

		if windll.user32.GetKeyState(0x2E):
			print("sending...")
			formatLine()
			time.sleep(1)
			return last_line.lower()
			break
		else:
			time.sleep(0.1)