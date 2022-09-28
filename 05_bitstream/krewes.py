krewes = "2$$$A$$$B@@@7$$$C$$$D@@@8$$$E$$$F"

def dev_duck(stKrew):
    di = {}
    info = krewes.split("@@@")
    for i in range(len(info)):
        devo = tuple(info[i].split("$$$"))
        di[devo[0]] = devo[1] + ' ' + devo[2]
print(di)
