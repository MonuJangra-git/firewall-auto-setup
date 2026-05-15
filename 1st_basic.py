import regex
import os
format=r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"
with open("IP-address.txt","r") as f:
    data = f.readlines()
    for ip in data:
        ip = ip.strip()
        ipr = regex.match(format,ip)
        if ipr :
            print(ipr.groups())
            print(".".join(ipr.groups()))
        else :
            print("invalid ip exit ")


