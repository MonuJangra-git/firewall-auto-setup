import subprocess
cmd = subprocess.Popen(["ls"],text=True,stdout=subprocess.PIPE)
cmdgrp = subprocess.Popen(["grep","1st"],text=True,stdin=cmd.stdout,stdout=subprocess.PIPE)
cmdsrch = subprocess.Popen(['head','-3'],text=True,stdin=cmdgrp.stdout,stdout=subprocess.PIPE)
# output = cmdsrch.communicate() # this not gives clean output
output,_=cmdsrch.communicate()
print(output.strip())
if output:
    print("that is the output ".strip())



