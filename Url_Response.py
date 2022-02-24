import subprocess
inputs = input ("Enter website: ")
if "." in inputs:
    args = ("curl -I " + inputs).split(" ")
    out = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process, err = out.communicate()

    result = process.decode("utf-8").split("\r\n")
    if "Could not resolve host" in result[2]:
        print("DNS resolution error \n check if the entered URL is correct")
        exit()
    else:
        print(result[3])
        exit()
else:
    print("Enter a correct URL")
    exit()
