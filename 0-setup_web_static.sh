#!/usr/bin/env bash
# Prepares a server for deployment

sudo apt update
sudo apt install nginx -y
sudo mkdir /data/ -p
sudo mkdir /data/web_static/ -p
sudo mkdir /data/web_static/releases/ -p
sudo mkdir /data/web_static/shared/ -p
sudo mkdir /data/web_static/releases/test/ -p
sudo echo "Hello Mike Rock, I'm Obidient and working" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
replace="server {\n\t\tlisten 80;\n\t\tserver_name index.html;\n\t\troot /var/www/html;\n\n\t\tlocation / {\n\t\tadd_header X-Served-By hostname;\n\t\t}\n\n\t\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/hbnb_static;\n\t\t}"
sudo sed -i "s/server {/$replace/" /etc/nginx/nginx.conf
sudo service nginx restart
