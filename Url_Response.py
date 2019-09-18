# CODE TO CHECK RESPONSE CODE OF A URL WHEN HIT WITH A CURL COMMAND

import subprocess
args = ("curl -I " + input ("Enter website: ")).split(" ")

out = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
process, err = out.communicate()

result = process.decode("utf-8").split("\r\n")[0]
print (result.split("HTTP/1.1")[1])
