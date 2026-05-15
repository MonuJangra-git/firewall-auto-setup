import subprocess
def cmd(command):
    out = subprocess.run([command],text=True,capture_output=True)
    user = subprocess.run(['id','-u'],text=True,capture_output=True)
    print(type(user.stdout))
    if out.stdout:
        if user.stdout.strip()=='0':
            print("You can access the commands")
            print(out.stdout)
            
        else :
            print("you do not have acces the commands")
            return "invalid user "

    if out.stderr:
        print("the error is :- \n"+out.stderr)
try :
    print(subprocess.run("figlet MONU JANGRA",shell=True,text=True,capture_output=True,timeout=10))
except Exception as error :
    print(f"FAILED TO LOAD Dont worry you can use your commands ")
inp = input("enter the command you want to access :-")
cmd(inp)

