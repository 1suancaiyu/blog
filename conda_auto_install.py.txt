import subprocess
file_name = input("install_file_name: ")
install_list = open( file_name, "r")
lines = install_list.readlines()
for line in lines:
    line = line.replace('\n','')
    print("line: ,",line)
    subprocess.run(["conda install ",line], shell=True, check=True)

file_name.close()
    
