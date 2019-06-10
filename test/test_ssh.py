import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='120.77.43.156', port=22, username='root', password='Jckj@123')
#stdin, stdout, stderr = ssh.exec_command('passwd')


#print(stdin)

chan = ssh.invoke_shell()



chan.send('passwd' + '\n')

time.sleep(3)

output = chan.recv(1024)
print(output)
