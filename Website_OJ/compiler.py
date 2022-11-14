import subprocess

# files read
input=open("input.txt",'r')
output=open("output.txt",'w')

# runing cpp file and writing in output
subprocess.run(["g++","test.cpp","-o","test.exe"],text=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
result=subprocess.run(["./test.exe"],text=True,stdin=input, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output.write(result.stdout)
output.close()
input.close()