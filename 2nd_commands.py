import subprocess
def cmd(command,description="default"):
    out = subprocess.run(command,shell=True,text=True,capture_output=True,timeout=20)
    if out.stdout:
        print(out.stdout)
    if out.stderr:
        print("the error is :- \n"+out.stderr)
cmd("ls | grep 'hack'")