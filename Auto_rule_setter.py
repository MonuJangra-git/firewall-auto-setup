import subprocess
import os 
# user must be login as admin to access or use the file 
# now we are going to setup
def ip_b(ip):
    try:
        ip_threat=str(ip).strip()
        rule_add=f'rule family=ipv4 source address="{ip_threat}" protocol="tcp" drop'
        rule = subprocess.run(["firewall-cmd",f"--add-rich-rule='{rule_add}'","--timeout=300"],text=True,capture_output=True)
        if rule.stdout:
            print(rule.stdout)
            print("runned successful")
    except Exception as error:
        print(f"there is some issue {error}")
    except KeyboardInterrupt as intrupt:
        print("exit successfully")
    except TimeoutError as timeout:
        print(timeout)

def file_reader(file):
    if os.fspath(file):
        print(os.fspath(file))
        with open(file,"r") as ip_block:
            data = ip_block.readlines()
            for i in data :
                ip_b(i)
            print("wait for new lines ")
            ip_block.seek(0,2)
            while True:
                position  = ip_block.tell()
                ip_block.seek(position)
                ip_  = ip_block.readline()
                if not ip_:
                    ip_block.seek(position)
                else :
                    print(f"the new ip is {ip_.strip()}")
                    ip_b(ip_)
        print("ok")
    else:
        print("no file exixts ")

def auto_rule_setup():
    set_up=subprocess.run(['firewall-cmd','--list-all'],text=True,capture_output=True)
    print(set_up.stdout)
# auto_rule_setup()
file_reader("paswd.txt")
