'''
1.安装jdk
'''
import os

def check_user():
    if os.getuid() == 0:
        pass
    else:
        print('Please change user to ROOT!!')

def jdk_install():
    rpm = os.system('rpm -ivh jdk-8u131-linux-x64.rpm')
    if rpm == 0:
        with open('/etc/profile', 'a+') as f:
            f.write('export JAVA_HOME=/usr/java/jdk1.8.0_131\n'
                    'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar\n'
                    'export PATH=$PATH:$JAVA_HOME/bin')
        os.system('source /etc/profile')
        f = os.system('java -version')
        if f == 0:
            print('JDK has been sucessfully installed!')
        else:
            print('Please check the installation package and reinstall JDK')
    else:
        print('Please checkout rpm packets')

def tomcat_install():
    url = 'http://mirror.bit.edu.cn/apache/tomcat/tomcat-8/v8.5.21/bin/apache-tomcat-8.5.21.tar.gz'
    file_name = url.split('/')
    if os.path.exists(file_name[-1]):
        os.system('rm -rf ' + file_name[-1])
    else:
        download = os.system('wget ' + url)
        if download == 0:
            os.system('tar zxvf ' + file_name[-1] + ' -C /usr/local')
            os.system('cd /usr/local/apache-tomcat-8.5.21 && ./bin/startup.sh')
        else:
            print('Please check netwok status!')

def zookeeper_install():
    url = 'https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/stable/zookeeper-3.4.10.tar.gz'
    filename = url.split('/')[-1]
    if os.path.exists(filename):
        os.system('rm -rf ' + filename)
    downlad = os.system('wget ' + url)
    if downlad == 0:
        os.system('tar zxvf ' + filename + ' -C /usr/local')
        os.system('cd /usr/local && mv zookeeper-3.4.10 zookeeper')
        os.system('cd /usr/local && '
                  'cp -r zookeeper/conf/zoo_sample.cfg zookeeper/conf/zoo.cfg')
        os.system('/usr/local/zookeeper/bin/zkServer.sh start')
        os.system('ps -ef|grep zookeeper|grep -v grep')
    else:
        print('Please check network status !!')

def nginx_install():
    url ='http://nginx.org/download/nginx-1.12.1.tar.gz'
    filename = url.split('/')[-1]
    download = os.system('wget ' + url)
    if download == 0:
        os.system('tar zxvf ' + filename + ' -C /usr/local')
        os.system('useradd -M -s /sbin/nologin www ')
        os.system('yum install pcre pcre-devel openssl openssl-devel gcc gcc-c++ -y')
        os.system('cd /usr/local/nginx-1.12.1 &&'
                  './configure --prefix=/usr/local/nginx '
                  '--user=www '
                  '--with-http_stub_status_module '
                  '--with-http_ssl_module '
                  '--with-http_realip_module && make && make install')
        os.system('ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx')
        os.system('nginx')
        print('######-Nginx have been installed Sucess!-######')
    else:
        print('Please check network status !!')

def docker_install():
     os.system('yum install -y docker')
     os.system('systemctl docker start')
def memcache_docer_install():
    check_docer =  os.system('rpm -qa|grep docker')
    if check_docer != '256':
        if os.system('ps -ef|grep docker|grep -v grep') == 256:
            os.system('systemctl  start docker')
        os.system('mkdir -p /usr/local/memfile')
        with open('/usr/local/memfile/dockerfile','w') as f:
            f.write('FROM centos\n'
                    'RUN yum update -y\n'
                    'RUN yum install -y memcached\n'
                    'USER daemon\n'
                    'EXPOSE 11211\n'
                    'ENTRYPOINT memcached\n'
                    'CMD ["-m", "128"]')
        os.system('cd /usr/local/memfile &&'
                  'docker build -t centos:memcache .')
        os.system('docker run -p 11211:11211 --name memcached -d centos:memcache')

    else:
        print('Please install Docker before!!')
while True:
    check_user()
    print('#'*30)
    print('1. Install Jdk \n'
          '2. Install Tomcat \n'
          '3. Install Zookeeper\n'
          '4. Install Nginx\n'
          '5. Install Dokcer\n'
          '6. Install Memcached(docker)')
    print('#'*30)
    choice = input('Please input your choice:')
    if choice == '1':
        jdk_install()
    elif choice == '2':
        tomcat_install()
    elif choice == '3':
        zookeeper_install()
    elif choice == '4':
        nginx_install()
    elif choice == '5':
        docker_install()
    elif choice == '6':
        memcache_docer_install()
    else:
        print('Please Input Right Choice!')

