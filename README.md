ansible-nginx

Задание 0

 ./ping.sh

Задание 1 
ansible-playbook -i inventory.ini playbook.yml -K 
ansible-playbook -i inventory.ini playbook.yml -D 

./ping.sh

Задание 1
ansible-playbook -i inventory.ini playbook.yml -K
ansible-playbook -i inventory.ini playbook.yml -D
curl http://localhost:8080/files
http://localhost:8080/files

Задание 2
cat library/nginx_port.py
ansible-playbook -i inventory.ini playbook.yml -K
