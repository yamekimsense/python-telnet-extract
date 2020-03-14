import os,sys, shutil

files = os.listdir('.')

i=0

for ffff in files:
    i=i+1

    #print (ffff)
    if "Store" in ffff:
        continue

    f = open(ffff,'r')
    lines = f.readlines()

    for line in lines:

        if "uptime" in line:
            uptime = line.split('uptime')[1].replace(",", "").replace("is ", "")

            if "weeks" in uptime:
                uptime = uptime.replace(" weeks", "w")

            if "day" in uptime:
                uptime = uptime.replace(" day", "d")

            if "hours" in uptime:
                uptime = uptime.replace(" hours", "h")

            if "minutes" in uptime:
                uptime = uptime.replace(" minutes", "m")


        if "System serial number" in line:
            #print (type(line))
            sn = line.split(':')[1]
            #print (sn)
        if "*" in line:
            while "  " in line:
                line = line.replace("  "," ")
            #print (line)
            line = line.split(" ")
            #print (line)
            model = line[3]
            ios = line [4]

    print (ffff.replace(".txt", ""),  model.replace("WS-C",""), sn.replace("\n",""), ios, uptime.replace("\n",""))

