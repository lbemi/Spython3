import paramiko
import os
import datetime
server_info ={
    'hostname':'192.168.1.57',
    'username':'root',
    'password':'admin',
    'port':22
}
local_dir = 'D:\项目文件\新建文件夹'
remote_dir = '/root/webapp'


class link_hosts(object):

    def __init__(self, hostname, port, username, password, cmd='' ):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=hostname,
                               port=port,
                               username=username,
                               password=password
                               )
            print('Connect Sucess!!!')
            if cmd == '':
                pass
            else:
                std_in, std_out, std_err = ssh_client.exec_command(cmd)
                for i in std_out:
                    print(i)
            ssh_client.close()
        except Exception:
            print('Connect Error!'
                  ' Please check configure file!!')

# def upload(load_dir, remote_dir, hostname, port, username, password):
#     s = paramiko.Transport(hostname,port)
#     s.connect(username=username,password= password)
#     sftp = paramiko.SFTPClient.from_transport(s)
#     files = os.listdir(load_dir)
#     for f in files:
#         print('#'*50)
#         print(datetime.datetime.now())
#         print('Begin to upload %s to %s' % ( f, hostname))
#         print('Uploading ',os.path.join(load_dir, f))
#         ra = remote_dir + '/' + f
#         sftp.put(os.path.join(load_dir,f), ra)
#         print(datetime.datetime.now())
#     print('#'*50)
#
# upload(load_dir=local_dir, remote_dir=remote_dir,**server_info)

cmd = "rpm -ivh jdk-8u131-linux-x64.rpm && " \
      "echo 'export JAVA_HOME=/usr/java/jdk1.8.0_131'>> /etc/profile && " \
      "echo 'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar'>> /etc/profile && " \
      "echo 'export PATH=$PATH:$JAVA_HOME/bin'>> /etc/profile && " \
      "source /etc/profile && " \
      "java -version"

link_hosts(**       server_info,cmd=cmd)