#=============AUTHOR=============#
"""
    Autor:      Víctor Velázquez Cid
    Versión:    Alpha 1.1
    Ult. actualización: 28/12/20
    
    Blog:       liteshut.blogspot.com
    GitHub:     https://github.com/vvelc
    Contacto:   victorvelazquezcid@gmail.com
    
    Titulo:     SUBNETTER 2

"""

#=============IMPORTS=============#
from ipaddress import *
import os
import time

#=============DATA=============#
net = ""
subnets = ""

#=============STRINGS=============#
blank = ""
space = " "
inp = ">>"

#=============COLORS=============#
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

#=============FUNCTIONS=============#

def setnet():
    print("Lets set IP Network")
    print("Formats: {0}192.168.1.0{1} or {0}192.168.1.0/24{1}\n".format((color.CYAN+color.BOLD),color.END))

    n1 = input('[{}IP{}] >> '.format(color.CYAN,color.END))

    if not '/' in n1:
        try:
            n1 = ip_address(n1)
        except:
            print("Error: Invalid ip address")
            return None

    if not "/" in str(n1):
        pr = input('Prefix: ')
        try:
            if "/" in pr:
                n1 = str(n1)+pr
            else:
                n1 = (str(n1)+'/'+pr)
        except:
            print("Error: Invalid prefix")

    try:
        net = ip_network(n1)
    except:
        print("Error: Invalid net")

def help():
    print("""\
================================== HELP ==================================
/set        Allows to enter IP // Formato: 192.168.10.0 or 192.168.10.0/24
/basic      Shows base net, broadcast, first and last usable hosts
/reset      Deletes existent data
/clear      Cleans the terminal screen
/help       Shows available commands
/exit       Exit Subnetter
==========================================================================\
""")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def close():
    clear()
    exit()

def cmd(cm):
    if cm == "/clear":
        return clear()
    elif cm == "/set":
        return setnet()
    elif cm == "/exit":
        return close()
    elif cm == "/help":
        return help()
    else:
        print("Error: Este comando no existe")

#=============SCRIPT=============#
clear()

print("""\
==================================================================""" + color.CYAN + """
   _____ _    _ ____  _   _ ______ _______ _______ ______ _____  
  / ____| |  | |  _ \| \ | |  ____|__   __|__   __|  ____|  __ \ 
 | (___ | |  | | |_) |  \| | |__     | |     | |  | |__  | |__) |
  \___ \| |  | |  _ <| . ` |  __|    | |     | |  |  __| |  _  / 
  ____) | |__| | |_) | |\  | |____   | |     | |  | |____| | \ \ 
 |_____/ \____/|____/|_| \_|______|  |_|     |_|  |______|_|  \_\\""" + color.END + f"""

[{color.GREEN}+{color.END}] Author: Víctor Velázquez Cid
[{color.GREEN}+{color.END}] Versión: Alpha 1.1

Type /help to see available commands. Type /exit to exit Subnetter
""")

#help()

while True:
    opt = input("{} ".format(inp))
    
    if len(opt) == 0:
        continue
    
    if opt[0] != "/":
        print("Error: Este comando no es válido")
        continue
    
    cmd(opt)