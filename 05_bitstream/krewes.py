krewes = "2$$$A$$$B@@@7$$$C$$$D@@@8$$$E$$$F"

info = krewes.split("@@@")
for i in range(len(info)):
    devo = info[i].split("$$$")
    print(devo)
print(info)