# цей скрипт заапускає створення 3 контейневі вордпреса, зміну титукки сайтів створення контейнера NGINX
import os
import fileinput

def clear_all():
    os.system("sudo rm -rf ./docker/uploads.ini/ ./docker/w1 ./docker/w2 ./docker/w3 echo Clear && sudo docker stop $(sudo docker ps -a -q) && sudo docker rm $(sudo docker ps -a -q) && sudo docker container ls -a && sudo docker rmi -f $(sudo docker images -a -q) ")
    print("=========================================================================================")
    print("==============  All forders, files and images destroyed or not exist  ===================")
    print("=========================================================================================")
def start_wordpress():
    os.system('cd ./docker && pwd && docker-compose up -d && cd ~')
    print("=========================================================================================")
    print("==============  Wordresses is started at ports 8000, 8001, 8002  ========================")
    print("=========================================================================================")

def change_files():
    os.system("sudo rm ./docker/w1/wp-admin/install.php")
    os.system("sudo cp ./config/conf_w1 ./docker/w1/wp-admin/install.php")
    os.system("sudo rm ./docker/w2/wp-admin/install.php")
    os.system("sudo cp ./config/conf_w2 ./docker/w2/wp-admin/install.php")
    os.system("sudo rm ./docker/w3/wp-admin/install.php")
    os.system("sudo cp ./config/conf_w3 ./docker/w3/wp-admin/install.php")
    print("=========================================================================================")
    print("==============  Files successfully changed  =============================================")
    print("=========================================================================================")

def change_file_Nginx():
    ip = str(os.popen("dig +short myip.opendns.com @resolver1.opendns.com").read())
    ip = ip.rstrip()
    print(ip)

def start_nginx():
    os.system('cd ./NGINX_2 && docker build -t"lb2:latest" . && docker run -p 80:80 --name nginx2 -d lb2:latest')
    print("=========================================================================================")
    print("==============  NGINX successfully started at port 80  ==================================")
    print("=========================================================================================")
    print()
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  13.69.59.208  ////////////////////////////////////")

#clear_all()
#start_wordpress()
#change_files()
change_file_Nginx()
#start_nginx()

'''
ip-шка в змінній ip
тепер треба сформувати за допомогою построкового дописування файл з ip, які передаються змінною

upstream backend {
      server 13.69.59.208:8000;
      server 13.69.59.208:8001;
      server 13.69.59.208:8002;
   }

   server {
      listen 80;

      location / {
          proxy_pass http://backend;
      }
   }

   видалити файл /home/alex/NGINX_2/load-balancer.conf і зробити копі

'''