from ping3 import ping
import paramiko
import paramiko


def channel():
    with open('/home/hmirin/python_apps/new_socket/channel.txt', 'r') as f:
        return f.read()


def pinger(ipaddr: str) -> str:
    ip = 110 + int(ipaddr)
    ping_mag = ping('192.168.100.{ip}'.format(ip=ip))
    if type(ping_mag) == float:
        return "MAG на месте!"
    else:
        return "Караул, приставку сперли!))"


def restart_mag(ipaddr: str) -> str:
    ip = 110 + int(ipaddr)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='192.168.100.{ip}'.format(ip=str(ip)),
                   username='root',
                   password='930920',
                   port=22)
    client.exec_command('reboot')
    client.close()
    return "MAG в ребуте"
