import os,sys, shutil

files = os.listdir('.')

i=0

for ffff in files:

    #print (ffff)
    if "Store" in ffff:
        continue

    i=i+1
    f = open(ffff,'r')
    lines = f.readlines()

    #print (i, ffff)

    for line in lines:
        if "-1-" in line:
            print (ffff, line.replace("\n",""))

        if "-2-" in line:
            print (ffff, line.replace("\n",""))

        if "-3-" in line:
            if "LINK-3-UPDOWN" in line:
                i = i + 1
            else:
                print (ffff, line.replace("\n",""))

        if "-4-" in line:
            print (ffff, line.replace("\n",""))

        if "-5-" in line:
            if "LINEPROTO-5-UPDOWN" or "SYS-5-CONFIG" in line:
                i = i + 1
            else:
                print (ffff, line.replace("\n",""))

        if "-6-" in line:
            print (ffff, line.replace("\n",""))

        if "-7-" in line:
            print (ffff, line.replace("\n",""))