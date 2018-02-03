import fileinput
import re
import time
from collections import Counter
import math
import sys
from datetime import datetime, timedelta

# 初始化显示的日志条目，None表示显示全部
records = None

# 脚本使用方法
def usage():
    print('Usage: %s nginx_log_file [max_record_nums] [datetime]' % sys.argv[0])
    print('Usage: [max_record_nums] for int number. eg: 10 ')
    print('Usage: [datetime] for [5d | 5h | 5m | 5s] for [5 days | 5 hours | 5 minutes | 5 seconds]')
    print('eg: ./ngx.py /var/log/nginx/access.log [10] [5d | 5h | 5m | 5s]')
    sys.exit(0)


# 过去多长时间的时间点时间戳
def tmstamp():
    if len(sys.argv) <= 3:
        # return datetime.now().timestamp()
        return 0
    elif re.match('^[\d]+d$', sys.argv[3]):
        return (datetime.now() - timedelta(days=float(sys.argv[3].rstrip('d')))).timestamp()
    elif re.match('^[\d]+h$', sys.argv[3]):
        return (datetime.now() - timedelta(hours=float(sys.argv[3].rstrip('h')))).timestamp()
    elif re.match('^[\d]+m$', sys.argv[3]):
        return (datetime.now() - timedelta(minutes=float(sys.argv[3].rstrip('m')))).timestamp()
    elif re.match('^[\d]+s$', sys.argv[3]):
        return (datetime.now() - timedelta(seconds=float(sys.argv[3].rstrip('s')))).timestamp()
    else:
        usage()


# 转换字节单位
def convertBytes(bytes, lst=['B', 'KB', 'MB', 'GB', 'TB', 'PB']):
    i = int(math.floor(math.log(bytes, 1024)))
    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f ' + lst[i]) % (bytes / math.pow(1024, i))


# 日志解析生成器
def ngx():
    try:
        with fileinput.input(sys.argv[1]) as f:
            for line in f:
                ip, _, _, dtime, _, mthd, _, _, status, size, *_ = re.split('[\s"]+', line)
                dtstamp = time.mktime(time.strptime(dtime.lstrip('['), '%d/%b/%Y:%H:%M:%S'))
                yield [ip, status, size, dtstamp]
    except:
        usage()


# 参数判断
if len(sys.argv) < 2 or len(sys.argv) > 4:
    usage()
if len(sys.argv) < 3:
    records = None
elif len(sys.argv) == 3:
    try:
        re.match('[\d]+', sys.argv[2])
        records = int(sys.argv[2])
    except:
        usage()
elif len(sys.argv) == 4:
    try:
        re.match('^[\d]+[dhms]$', sys.argv[3])
    except:
        usage()

# 初始化各统计变量
iptotal, ipsize, ip200, ip302, ip304, ip403, ip404, ip500, ip502, ip503, totsize = Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), Counter(), 0

# 定义映射表头
header = ['ip', 'statuscode', 'size', 'dtstamp']

# 进行迭代统计
for line in ngx():
    # 将两个列表转换为字典
    datadict = dict(zip(header, line))

    # 统计n天/时/分/秒之前的访问量和带宽等信息
    if datadict['dtstamp'] > tmstamp():

        # 每个IP的流量带宽
        ipsize[datadict['ip']] += int(datadict['size'])

        # 总流量
        totsize += int(datadict['size'])

        # 每IP的总访问量
        iptotal[datadict['ip']] += 1

        # 统计个状态码的请求数
        if datadict['statuscode'] == '200':
            ip200[datadict['ip']] += 1
        elif datadict['statuscode'] == '302':
            ip302[datadict['ip']] += 1
        elif datadict['statuscode'] == '304':
            ip304[datadict['ip']] += 1
        elif datadict['statuscode'] == '403':
            ip403[datadict['ip']] += 1
        elif datadict['statuscode'] == '404':
            ip404[datadict['ip']] += 1
        elif datadict['statuscode'] == '500':
            ip500[datadict['ip']] += 1
        elif datadict['statuscode'] == '502':
            ip502[datadict['ip']] += 1
        elif datadict['statuscode'] == '503':
            ip503[datadict['ip']] += 1

# 判断是否有存在数据，存在则打印，否则，输出错误信息！
if totsize:
    # 打印网站总流量,总访问量
    print("\nTotal traffic : %s  Total request times : %d\n" % (convertBytes(totsize), sum(iptotal.values())))

    # 打印表头
    print('%-15s %-10s %-12s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s' % (
    'Ip', 'Times', 'Traffic', '200', '302', '304', '403', '404', '500', '502', '503'))

    print('%-15s %-10s %-12s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s' % (
    '-' * 15, '-' * 10, '-' * 12, '-' * 8, '-' * 8, '-' * 8, '-' * 8, '-' * 8, '-' * 8, '-' * 8, '-' * 8))
    # 打印前多少条数据
    # for k, v in sorted(iptotal.items(), key=lambda v: v[1], reverse=True):
    for k, v in iptotal.most_common(records):
        print('%-15s %-10s %-12s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s' % (
        k, v, convertBytes(ipsize[k]), ip200[k], ip302[k], ip304[k], ip403[k], ip404[k], ip500[k], ip502[k], ip503[k]))

else:
    print('Not found data!')