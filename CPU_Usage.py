# TO CHECK CPU Usage in linux Environment in a readable format.

#Calculates cpu usage as well as install psutil package if not installed
install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('psutil')

total_cpu = 0.0

Temp1 = str(psutil.cpu_times()).decode("utf-8")
Temp =Temp1.split(", ")
#print("\n\n")
#print (Temp)

user = float((Temp[0].split("="))[1])
nice = float((Temp[1].split("="))[1])
system = float((Temp[2].split("="))[1])
idle = float((Temp[3].split("="))[1])
iowait = float((Temp[4].split("="))[1])
irq = float((Temp[5].split("="))[1])
softirq = float((Temp[6].split("="))[1])
steal = float((Temp[7].split("="))[1])
guest = float((Temp[8].split("="))[1])
guest_nice = float(((Temp[9].split("="))[1])[:-2:])


for i in range(len(Temp)):
	i = ((Temp[i].split("="))[1])
	if i.endswith(")"):
		i = i[:-1:]
	e= float(i)
	total_cpu += e

usedCpu = ((user + nice + system +iowait + irq +softirq)/total_cpu)*100

freeCpu = (idle/total_cpu)*100

print ("\n"+ "Used Cpu: " +str(usedCpu)[:5]+"%\n"+ "Free Cpu: " + str(freeCpu)[:5]+"%\n")
