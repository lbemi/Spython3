import  paramiko
import os
import sys
import  datetime

server_info ={
    'host':'192.168.1.64',
    'user':'root',
    'password':'admin',
    'port':22
}
local_dir = ''
remote_dir = ''
def exec_cmd(cmd):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=server_info['host'],
                           port=server_info['port'],
                           username=server_info['user'],
                           password=server_info['password'])
        std_int, std_out, std_err = ssh_client.exec_command(cmd)
        info_list = []
        for info in std_out:
            info_list.append(info)
            print(info)

        print(info_list)
        ssh_client.close()
    except Exception():
        print('Error')

cmd = 'ps -ef|grep tomcat|grep -v grep'
exec_cmd(cmd)