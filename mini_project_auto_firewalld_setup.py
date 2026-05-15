import subprocess 
run = subprocess.run("cd ~/ & ls -l & pwd",shell=True, capture_output=True , text=True )
print(run.stdout+run.stderr)











