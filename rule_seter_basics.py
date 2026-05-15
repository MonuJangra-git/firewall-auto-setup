import subprocess
# main project part  
def ip_rule_setter(ip):
    rule=f'rule family="ipv4" source address="{str(ip)}" drop'
    print(rule)
    try:
        block = subprocess.run(["firewall-cmd",f"--add-rich-rule={rule}","--timeout=50"],text=True,capture_output=True)
        if block.stdout:
            print(block.stdout)
        else :
            print(block.stderr)
    except Exception as error :
        print(f"there are some issue the program :- \n {error}")
    except KeyboardInterrupt:
        print("exit successfully")
def file_reader(file_path="/home/blackhack/python/paswd.txt"):
    with open(file_path,"r") as f:
        f.seek(0,2) # read from start to end 
        while True:
            pos = f.tell() # tell the postion of pointer 
            line = f.readline()
            if not line:
                f.seek(pos)
            else :
                line=line.strip()
                print(f"the new ip is {line}")
                ip_rule_setter(line)
file_reader()