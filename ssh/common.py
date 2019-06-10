#coding:utf-8

import paramiko
import time

# 不能使用改变目录的shell命令
# 不能使用会导致session中断的命令
def send_ssh_command(ip, username, passwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, username, passwd)
    chan = ssh.invoke_shell()
    chan.send('\n')
    chan.recv(1000)
    chan.send('\n')
    end_buf = chan.recv(1000)
    print(type(end_buf))
    print(end_buf)
    while True:
        chan.send(command + '\n')
        time.sleep(1)
        recv_buf = chan.recv(3000)
        print(str(recv_buf, 'utf-8'))
        if recv_buf.endswith(end_buf):
            print('OK')
            break


if __name__ == "__main__":
    command = 'ls -al'
    send_ssh_command('120.77.43.156', 'root', 'Jckj@123', command)