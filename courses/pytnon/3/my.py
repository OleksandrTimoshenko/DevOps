#  & C:/Users/alex/AppData/Local/Programs/Python/Python37-32/python.exe d:/My/nanshannia_2/cources/devops-2/pytnon/3/my.py 40.114.216.179 22 alex /home usr 20 551
# підключення по ssh ключу, private ключ має лежати в тій самій папці що і виконуваний файл, під назвою mykey.pem
# для виконання користувач має мати право робити sudo

import paramiko, sys, os

host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
path = sys.argv[4]
name = sys.argv[5]
numeric = sys.argv[6]
permissions = sys.argv[7]

def make_dir(path, name,permissions,client):
    full_path = path + "/"+  name
    commant = "sudo mkdir -m " + str(permissions) + " " + full_path
    channel = client.get_transport().open_session()
    channel.get_pty()
    channel.settimeout(5)
    channel.exec_command(commant)
    #channel.send(password+'\n')
    #print channel.recv(1024)
    channel.close()


secret = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "mykey.pem")

k = paramiko.RSAKey.from_private_key_file(secret)
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("connecting")
c.connect( hostname = host, username = user, port = port, pkey = k )
print ("connected")
for i in range (0, int(numeric)):
        make_dir(path, (name + str(i + 1)), permissions,c)
c.close()