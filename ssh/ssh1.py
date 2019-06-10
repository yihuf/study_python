import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('120.77.43.156', 22, 'root', 'Jckj@123')
chan = ssh.invoke_shell()
chan.send('\n')
time.sleep(1)
end_buf = chan.recv(1000)
chan.send('\n')
time.sleep(1)
end_buf = chan.recv(1000)
print(type(end_buf))
print(end_buf)
chan.send('ls -l\n')
time.sleep(1)
recv_buf = chan.recv(1000)
print(str(recv_buf, 'utf-8'))
if recv_buf.endswith(end_buf):
    print('OK')
else:
    print('Error')