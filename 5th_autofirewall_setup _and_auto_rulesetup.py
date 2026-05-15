import subprocess
def run_cmd(cmd:list):
    try:
        output=subprocess.run(cmd,text=True,capture_output=True,timeout=20)
        return output.returncode==0,output.stdout.strip(),output.stderr.strip()
        # 0 means true command runned successfully
    except subprocess.TimeoutExpired:
        return False,"","timeout_error"
    except Exception as error:
        return False,"",error
def admin_check():
    id_cmd=["id","-u"]
    success,stdout,stderr=run_cmd(id_cmd)
    if success:
        if stdout=="0":
            print("user can use the script ")
            return 1
        if stdout !="0":
            print("user can not use the script \nlogin as admin 1st  \nexiting")
            return 0
        if stderr:
            print(f"there are some issue {stderr}")
    else :
        print("failed to check")
def firewall_check():
    # now initially we making it to check specific for firewalld in future i add many firewall checking setup like iptables,etc
    check=["which","firewalld"]
    success,stdout,stderr=run_cmd(check)
    if success:
        if stdout:
            print(f"firewalld is installed ")
            return 1 
        
        else:
            print(f"there are some issue , the error is {stderr}")
            return 0
    else:
        print("script not runned successfully , may be systemic error ")
def firewalld_installer():
    inst_cmd=["apt","install","firewalld"]
    success,stdout,stderr=run_cmd([inst_cmd])
    if success:
        if stdout:
            print("firewalld is installing ......")
            return 1
        if stderr:
            print(f"there may be :- \n {stderr}")
            return 0
    else :
        print("cmd not run there are some issues")
def auto_setup():
    setup0=["systemctl","enable","firewalld"]
    setup1=["systemctl","start","firewalld"]
    success,stdout,stderr=run_cmd(setup0)
    if success:
        print("-"*100)
        print("firewalld setup successfully you can now setup rule ")
        return 1
    else :
        print("there are some issue ")
        return 0
def rule_setter():
    """next time i add new auto rule setup"""
    pass
def cli_interface():
    """in this i add a user interface so that user can setup the manually according its need """
    print("ADMIN INTERACTION PANEL TO SETUP THE RULE MANUALLY")
    print("1.port\n2.ip_block\n3.zone\n4.protocoles\n5.services")
    try:
        cmd=int(input("choose your option from above as integer only"))
        if cmd>=6:
            print("choose correct option from above")
            cli_interface()
    except Exception as error:
        print(error)
    else:
        return cmd
run=subprocess.run("figlet -l MONU JANGRA",shell=True,capture_output=True,text=True)
print(run.stdout)
# auto_setup()
print(cli_interface())

