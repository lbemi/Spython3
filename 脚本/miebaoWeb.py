from paramiko import SSHClient,ssh_exception,AutoAddPolicy
from os import system
def star_up(host, user, pwd, execmd):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=user, password=pwd, timeout=10)
    stidn, stdout, stderr =ssh.exec_command(execmd)
    stidn.write('Y')
    for info in stdout:
        print(info)
    ssh.close()
def main():
    host = '192.168.1.184'
    user = 'root'
    pwd = 'admin'
    excmd = 'python /root/webgit.py'
    star_up(host, user, pwd, excmd)
main()
system('start http://192.168.1.184:83')