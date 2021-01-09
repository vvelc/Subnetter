dic = {}

net1 = "192.168.10.0/24"
net2 = "192.168.20.0/24"
net3 = "192.168.30.0/24"
net4 = "192.168.40.0/24"

nam1 = "Edificio 1"
nam2 = "Edificio 2"
nam3 = "Edificio 3"
nam4 = "Edificio 4"

dic[nam1] = net1
dic[nam2] = net2
dic[nam3] = net3
dic[nam4] = net4

tab = """\
===================================
| Subnet          Address         |
===================================
{}
===================================
"""

filas = [i for i in dic.items()]

print(tab.format("\n".join("| {:<15} {:<15} |".format(*fila) for fila in filas)))