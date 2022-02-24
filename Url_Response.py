import subprocess
inputs = input ("Enter website: ")
if "." in inputs:
  args = ("curl -I " + inputs).split(" ")

  out = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  process, err = out.communicate()

  result = process.decode("utf-8").split("\r\n")[3]
  print(result)
else:
  print("Enter a correct URL")
  exit()
