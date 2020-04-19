import time, sys, os
from main_func import checkUserFilePathD
from pychatmenu import main1


CAT = '''

                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
[starting in 10(s)]    ; '   : :`-:     _.`* ;
    [*py chat*]      .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        

'''



def progress(count, total, status=''):

    bar_len = 60

    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)

    bar = '8' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))

    sys.stdout.flush()



def gatherinformation():

	total = 100

	i = 0

	while i <= total:

	    progress(i, total, status='Gathering Information')

	    time.sleep(0.17)

	    i += 2.5



	print(CAT)
  




try:

  os.system("color 3")

  print('(PYCHAT) A wrong path => FORCE EXIT')
  gta_sa_pychat_path = str(input('Your GTA DIR$ '))


  if gta_sa_pychat_path.startswith('C:'):

    gta_sa_pychat_path += '\\CLEO\\pychat.cs'

  else:

    print('''

      $unknw path OR pychat.cs not found
      $restart and check file path(it should begin with "C:")
      $closing in 5(s)

      ''')

    time.sleep(4.9)

    os.system('exit')

except Exception as e:

  raise e("Something went wrong! PLEASE RELOAD")

finally:

  if checkUserFilePathD(gta_sa_pychat_path):

  	gatherinformation()

  	print("(PYCHAT): ", gta_sa_pychat_path)

  	time.sleep(9.9)

  	main1()

  else:

  	print(f"{gta_sa_pychat_path} - checking the file failed! Please RELOAD")
  	time.sleep(1.5)