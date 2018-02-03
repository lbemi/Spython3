import paramiko
import os
import sys
import datetime

hostname = '192.168.1.184'
user = 'root'
pwd = 'admin'
port = '22'
local_dir = "D:/项目文件/2017-11-29/1557"
remote_dir = '/usr/local/tomcat1/webapps/'


def upload():
    try:
        t = paramiko.Transport((str(hostname), int(port)))
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        files = os.listdir(local_dir)
        for f in files:
            print('####################################################')
            print('Begin to upload file  to %s ' % hostname)
            print('Uploading ', os.path.join(local_dir, f))
            print(datetime.datetime.now())
            ra = remote_dir + '/' + f
            sftp.put(os.path.join(local_dir, f), ra)
            print(datetime.datetime.now())

        t.close()
        print('####################################################')
        sftp_exec_command()
    except Exception:
        print('Connect Error')

s = paramiko.Transport
def sftp_exec_command():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=int(port), username=user, password=pwd)
        std_in, std_out, std_err = ssh_client.exec_command('sh /root/restart.sh')
        # for line in std_out:
        #     print (line.strip("\n"))
        while True:
            print(std_out.readline())
        ssh_client.close()
    except Exception():
        print('Error')


def print_tomcat_logs():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=int(port), username=user, password=pwd)
        std_in, std_out, std_err = ssh_client.exec_command('tail -f /usr/local/tomcat1/logs/catalina.out')
        # for line in std_out:
        #     print (line.strip("\n"))
        while True:
            print(std_out.readline())
        ssh_client.close()
    except Exception as e:
        print(e)


def docker_restart():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='192.168.1.143', port=22, username=user, password=pwd)
        std_in, std_out, std_err = ssh_client.exec_command('docker restart memcached')
        for line in std_out:
            print(line.strip("\n"))
        print('重启Memcached成功!')
    except Exception as e:
        print(e)



if __name__ == '__main__':
    try:
        while True:
            print('#' * 30)
            print(' 1：上传并重启服务器')
            print(' 2：重启服务器')
            print(' 3：打印tomcat日志')
            print(' 4：重启Memcached')
            print('#' * 30)
            print('输入数字：')
            a = str(input())
            if a == '1':
                upload()
            elif a == '2':
                sftp_exec_command()
            elif a == '3':
                print_tomcat_logs()
            elif a == '4':
                docker_restart()
            else:
                print('wrong select!')
    except KeyboardInterrupt:
        pass
