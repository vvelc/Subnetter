"""
    Autor:      Víctor Velázquez Cid
    Versión:    Beta 1.3
    Ult. actualización: 28/12/20
    
    Blog:       liteshut.blogspot.com
    GitHub:     https://github.com/vvelc
    Contacto:   victorvelazquezcid@gmail.com
    
    Titulo:     Red base y Broadcast IPV4 1

"""
#===IMPORTES===#
from time import sleep
import os

#===DATOS===#   
ip = []
mask = []
pair = {'Base':'', 'Broadcast':''}

#===FUNCIONES===#

def help():
    print("""\
======================== MANUAL DE USO ========================
/setip      Permite ingresar la IPV4 // Formato: 192.168.0.1
/setmask    Permite ingresar la Máscara IPV4 // Formato: /8 /24
/view       Muestra la Red Base y Broadcast
/reset      Borra los datos ya existentes
/help       Muestra los comandos disponibles
/exit       Salir del programa
===============================================================\
""")

def setip():
    global ip
    
    ipset = input("IPV4: ")
    ipset = ipset.split(".")
    
    for octet in ipset:
        if ((octet.isdigit() and (int(octet) <= -1 or int(octet) > 255)
            or len(octet) < 1 or not octet.isdigit() or len(ipset) < 4)):  
            fine = False
            break
        fine = True
    
    if fine:
        ip = [int(i) for i in ipset]
    
    else:
        print("Error: Esta IP no es válida")

def setmask():
    global mask
    
    maskset = input("Mask: ")
    maskset = maskset.split(".")
    
    for octet in maskset:
        if ((octet.isdigit() and (int(octet) <= -1 or int(octet) > 255)
            or len(octet) < 1 or not octet.isdigit() or len(maskset) < 4)):
            fine = False
            break
        fine = True
    
    if fine:
        for i in range(len(maskset)):
            if i == 0:
                continue
            
            ant = int(maskset[i-1])
            
            if int(maskset[i]) != 0 and ant != 255:
                fine2 = False
                print("hola")
                break
            fine2 = True
    
    if fine2:
        mask = [int(m) for m in maskset]
    
    else:
        print("Error: Esta máscara de red no es válida")

def reset():
    global ip, mask
    ip = []
    mask = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def close():
    print("Cerrando...")
    sleep(1)
    clear()
    exit()

def view():
    
    #Verificar que no estén vacíos
    if ip == [] or mask == []:
        print("Error: IP o Máscara no introducidas")
        return
    
    base = [i&m for (i,m) in zip(ip,mask)]
    base = '.'.join([str(elem) for elem in base]) 
    pair['Base'] = base
    
    mk = mask
    
    #convertir mascara a binario
    for i in mk:
        if len(bin(i)[2:]) < 8:
            n = 8 - len(bin(i)[2:])
            mk[mk.index(i)] = (f'{"0"*n}{bin(i)[2:]}')
        else:
            mk[mk.index(i)] = bin(i)[2:]

    mk = ''.join([str(elem) for elem in mk]) 

    ind = 0
    #encontrar ultimo bit encendido
    for i in range(len(mk)):
        if not "1" in mk[i:]:
            break
        ind = i

    mk = mk[:ind+1] + mk[ind+1:].replace('0','1')
    mk = mk[:8] + "." + mk[8:]
    mk = mk[:17] + "." + mk[17:]
    mk = mk[:26] + "." + mk[26:]
    mk = mk.split(".")
    broadcast = [int(m,2) for m in mk]
    broadcast = '.'.join([str(elem) for elem in broadcast]) 
    pair['Broadcast'] = broadcast
    print("""\
+======================================+
| Elemento           |              IP |
|--------------------------------------|
{}
+======================================+\
""".format('\n'.join("| {:<20}{:>16} |".format(key, value)
 for key, value in pair.items())))

def cmd(cm):
    if cm == "/help":
        return help()
    elif cm == "/exit":
        return close()
    elif cm == "/setip":
        return setip()
    elif cm == "/setmask":
        return setmask()
    elif cm == "/clear":
        return clear()
    elif cm == "/reset":
        return reset()
    elif cm == "/view":
        return view()
    else:
        print("Error: Este comando no existe")

#=============SCRIPT=============#
clear()

print("""
==================================================================
   _____ _    _ ____  _   _ ______ _______ _______ ______ _____  
  / ____| |  | |  _ \| \ | |  ____|__   __|__   __|  ____|  __ \ 
 | (___ | |  | | |_) |  \| | |__     | |     | |  | |__  | |__) |
  \___ \| |  | |  _ <| . ` |  __|    | |     | |  |  __| |  _  / 
  ____) | |__| | |_) | |\  | |____   | |     | |  | |____| | \ \ 
 |_____/ \____/|____/|_| \_|______|  |_|     |_|  |______|_|  \_\\

Author: Víctor Velázquez Cid
Versión: Beta 1.3\
""")

help()

while True:
    opt = input(">> ")
    
    if len(opt) == 0:
        continue
    
    if opt[0] != "/":
        print("Error: Este comando no es válido")
        continue
    
    cmd(opt)