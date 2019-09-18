# Tells you the amount of free ram and free Disk

import subprocess
import re

cmd1 = "free -h"
cmd2 = "df -h"

def gcis(str1):
	args = str1.split(" ")
	out = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	process, err = out.communicate()
	process = process.decode('utf-8')
	return (re.sub(" +", " ", process))

def stl(str2):
	temp_list = gcis(str2).split("\n")
	temp_list = [x.split(" ") for x in temp_list]
	return (temp_list)
#Ram Usage
data = stl(cmd1)[1]

print ("Total Ram : "+ data[1] + "\n" +"Used Ram: " +data[2] + "\n" + "Free Ram: " +str(int( (data[3])[:-2])+int((data[6])[:-2]))+"Mb")

# Disk Space
dsks= stl(cmd2)
for i in range(len(dsks)):
	if "/data" in dsks[i]:
		tot = (dsks[i])[1]
		usd = (dsks[i])[2]
		avl = (dsks[i])[3]
		frp = 100-(int(((dsks[i])[4])[:-1]))
		break

print("\n\nTotal space : " + tot + "\n" + "Used space: "+ usd + "\n" + "Avl. Space: " +avl + "\n"+ "Free disk %: " + str(frp)+"%")
