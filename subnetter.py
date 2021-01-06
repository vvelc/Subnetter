#=============AUTHOR=============#
"""
    Autor:      Víctor Velázquez Cid
    Versión:    Alpha 1.9
    Ult. actualización: 6/1/21
    
    Blog:       liteshut.blogspot.com
    GitHub:     https://github.com/vvelc
    Contacto:   victorvelazquezcid@gmail.com
    
    Titulo:     SUBNETTER

"""

#=============IMPORTS=============#
from ipaddress import *
import os
import time
import math

#=============DATA=============#
net = ""
table = {}
subnets = 0

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

def setnet(n1=None):
    global inp, net, subnets
    if n1 == None:
        print("Lets set IP Network")
        print("Formats: {0}192.168.1.0{1} or {0}192.168.1.0/24{1}".format((color.CYAN+color.BOLD),color.END))
        inp = '[{}IP{}] >> '.format(color.CYAN,color.END)
        n1 = input(inp)

    if not '/' in n1:
        try:
            n1 = ip_address(n1)
        except:
            print("Error: Invalid ip address")
            return None

    if not "/" in str(n1):
        inp = '[{}Prefix{}] >> '.format(color.CYAN,color.END)
        pr = input(inp)
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
        print("Error: Invalid network")
        inp = ">>"
        return None
    inp = '[{}{}{}] >>'.format(color.CYAN,net,color.END)
    subnets = 0

def subnet(n=None):
    global net, subnets, inp

    if net == "":
        print("Error: No network selected")
        return None

    prefix = int(str(net)[(int(str(net).index("/")))+1:])

    if n == None:
        print("Lets subnet your network")
        print("In how many subnets do you want to divide your net? {0}Available: {1}{2}".format(
            color.CYAN, (2**(30-prefix)), color.END))
        inp = '[{}Subnets{}] >> '.format(color.CYAN,color.END)
        n = input(inp)

        if n == "":
            print("Error: No subnets entered")
            return None
        elif not n.isdigit():
            print("Error: Invalid input")
            return None
    
    n = int(n)

    valid = False

    for i in range(33):
        if 2**i == n:
            valid = True
            break
    
    if valid:
        snets = list(net.subnets(int(math.log2(n))))
    else:
        print("Error: Invalid number of subnets")
        return None
    
    count = 0

    #===Two Columns===#
    """
    for s in snets:
        s1 = s
        if count % 2 != 0:
            if (snets.index(s) < len(snets)-1):
                s2 = snets[snets.index(s1)+1]
            print(' [{0}{3}{1}] {2}'.format(color.CYAN,color.END,str(s2),count+1))
        else:
            print(' [{0}{3}{1}] {2:<15}'.format(color.CYAN,color.END,str(s1),count+1), end="")
        count += 1
    """
    #===One Column===#
    for s in snets:
        print(' [{0}{3}{1}] {2:<15}'.format(color.CYAN,color.END,str(s),count+1))
        count += 1
    
    subnets = n

    inp = '[{0}{1}{2} [{0}{3}{2}]] >>'.format(color.CYAN,net,color.END,subnets)

def select(n = None):
    global net, inp, subnets

    if net == "":
        print("Error: No network selected")
        return None

    if subnets == 0:
        print("Error: Network not subnetted")
        return None

    elif n == "":
        print("Error: No subnet selected")
        return None

    snets = list(net.subnets(int(math.log2(subnets))))

    if n == None:
        print("Lets select your subnet")

        count = 0

        for s in snets:
            print(' [{0}{3}{1}] {2:<15}'.format(color.CYAN,color.END,str(s),count+1))
            count += 1
        
        inp = '[{}Select{}] >> '.format(color.CYAN,color.END)

        selection = int(input(inp))

    elif n != "" and not n.isdigit():
        print("Error: Invalid input")
        return None
    
    else:
        selection = int(n)
    
    print("You've selected subnet {0}#{1}{2}".format(color.CYAN,selection,color.END))

    net = snets[selection-1]

    inp = '[{0}{1}{2}] >>'.format(color.CYAN,net,color.END)

    subnets = 0

def basic():
    global net  
    if net == "":
        print("Error: No network selected")
        return None
    
    #basen = str(net)
    #broad = str(net.broadcast())
    hosts = list(net.hosts())
    #print(list(net.subnets()))
    print("[{}+{}] Base network: {}".format(color.CYAN,color.END,hosts[0]-1))
    print("[{}+{}] Usable Hosts:".format(color.CYAN,color.END))
    count = 0
    for h in hosts:
        if count % 2 != 0:
            print(' [{0}+{1}] {2}'.format(color.CYAN,color.END,str(h)))
        else:
            print(' [{0}+{1}] {2:<15}'.format(color.CYAN,color.END,str(h)), end="")
        count += 1

    print("[{}+{}] Broadcast: {}".format(color.CYAN,color.END,h+1))
    pass

def name(nam=None):
    global net, table
    if net == "":
        print("Error: No network selected")
        return None
    elif subnets != 0:
        print("Error: No subnet selected")
        return None
    elif nam == None:
        print("Error: No name entered")
        return None
    elif nam.strip(" ") == "":
        print("Error: Invalid name")
        return None
    elif len(nam) > 20:
        print("Error: Too large name")
        return None

    key_list = list(table.keys())
    val_list = list(table.values())

    if nam in key_list:
        print("Error: Name already used")
        return None

    if str(net) in val_list:
        oldkey = key_list[val_list.index(str(net))]
        #table[nam] = table.pop(oldkey)
        table.pop(oldkey, None)

    nam = nam.strip()
    try:
        table[nam] = str(net)
        print("Succesfully saved")
        return
    except:
        print("Error: Something ocurred while saving")
        return None
    
def showtable():
    global table
    if table == {}:
        print("Error: No named subnets")
        return None
    
    tab = """\
===========================================
| Subnet               Address            |
===========================================
{}
===========================================
"""

    filas = [i for i in table.items()]

    print(tab.format("\n".join("| {:<20} {:<18} |".format(*fila) for fila in filas)))

def help():
    print("""\
================================== HELP ==================================
/{0}set [ip]{1}     Allows to enter IP and Prefix
/{0}basic{1}        Shows base net, broadcast, first and last usable hosts
/{0}subnet [n]{1}   Allows to enter in how many subnets you want to divide
/{0}sel [n]{1}      Allows to select a subnet of your net
/{0}name <name>{1}  Allows to enter the name of a subnet
/{0}table{1}        Shows a table with subnets and names.
/{0}wipe{1}         Wipes actual subnet
/{0}reset{1}        Resets all data
/{0}clear{1}        Cleans the terminal screen
/{0}help{1}         Shows available commands
/{0}exit{1}         Exit Subnetter
==========================================================================\
""".format(color.CYAN,color.END))

def start():
    print("""\r  
==================================================================""" + color.CYAN + """
   _____ _    _ ____  _   _ ______ _______ _______ ______ _____  
  / ____| |  | |  _ \| \ | |  ____|__   __|__   __|  ____|  __ \ 
 | (___ | |  | | |_) |  \| | |__     | |     | |  | |__  | |__) |
  \___ \| |  | |  _ <| . ` |  __|    | |     | |  |  __| |  _  / 
  ____) | |__| | |_) | |\  | |____   | |     | |  | |____| | \ \ 
 |_____/ \____/|____/|_| \_|______|  |_|     |_|  |______|_|  \_\\""" + color.END + f"""

[{color.CYAN}+{color.END}] Author: Víctor Velázquez Cid
[{color.CYAN}+{color.END}] Version: Alpha 1.9

Type /{color.CYAN}help{color.END} to see available commands. Type /{color.CYAN}exit{color.END} to exit Subnetter
""")

def clear(close=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    if close:
        return None
    start()

def wipe():
    global inp,net,subnets

    inp = ">>"
    net = ""
    subnets = 0

def reset():
    global table
    wipe()
    table = {}
    clear()

def close():
    clear(True)
    exit()

def cmd(cm):
    com = ""
    arg = ""

    if cm[0] == "/":
        if " " in cm:
            com = cm[1:cm.index(" ")]
        else:
            com = cm[1:]

        if " " in cm and cm[cm.index(" "):] != "":
            arg = cm[cm.index(" ")+1:]

        if com == "clear":
            return clear()
        elif com == "wipe":
            return wipe()
        elif com == "reset":
            return reset()
        elif com == "set":
            if arg != "":
                return setnet(arg)
            else:
                return setnet()
        elif com == "basic":
            return basic()
        elif com == "subnet":
            if arg != "":
                return subnet(arg)
            else:
                return subnet()
        elif com == "sel":
            if arg != "":
                return select(arg)
            else:
                return select()
        elif com == "exit":
            return close()
        elif com == "help":
            return help()
        elif com == "name":
            if arg != "":
                return name(arg)
            else:
                return name()
        elif com == "table":
            return showtable()
        else:
            print("Error: Non-existent command")
            return None
    else:
        print("Error: Non-existent command")
        return None

#=============SCRIPT=============#
clear()

#help()

while True:
    opt = input("{} ".format(inp))
    
    if len(opt) == 0:
        continue
    
    if opt[0] != "/":
        print("Error: Este comando no es válido")
        continue
    
    cmd(opt)