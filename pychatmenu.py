from py_menu import Menu, Option
from main_func import *
from pychatcs import *



def main1():
	splash = """\
	--------------------------------------------------------
	                  ~!~ (pychat) ~!~
	--------------------------------------------------------
	"""


	main_menu = Menu(header = f"Username: {getUserNameD()} - Started at: {getWTime()} - Chatlog.txt: {checkUserFilePathD(path)}\n", splash = splash)

	py_mode_menu = Menu(header = "Copychat -> Choose a MODE\n")
	py_info_menu = Menu(header = "Informations")


	main_menu.add_option("(pychat) Choose Mode", py_mode_menu)
	main_menu.add_option("(pychat) Informations", py_info_menu)


	py_mode_menu.add_option("Copy Chat(Normal)", lambda: change(copychatNormal()))#print for debug
	py_mode_menu.add_option("Copy Chat Reversed", lambda: change(copychatReversed()))
	py_mode_menu.add_option("Copy Chat Remove Digits", lambda: change(copychatRemoveDigits()))
	py_mode_menu.add_option("Copy Chat UPPER", lambda: change(copychatUpper()))
	py_mode_menu.add_option("Copy Chat lower", lambda: change(copychatLower()))


	py_info_menu.add_option("Help Default KEY: ", lambda: print("press 'DEL(0x2E)' after choosing MODE"))
	py_info_menu.add_option("[Debug] GTA:SAMP PiD: ", lambda: print(getGTASAPID()))

	main_menu.mainloop()