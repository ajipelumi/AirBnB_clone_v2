#!/usr/bin/env bash
# Prepares a server for deployment

sudo apt update
sudo apt install nginx -y
mkdir /data/ -p
mkdir /data/web_static/ -p
mkdir /data/web_static/releases/ -p
mkdir /data/web_static/shared/ -p
mkdir /data/web_static/releases/test/ -p
echo "Hello Mike Rock, I'm Obidient and working" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
replace="server {\n\t\tlisten 80;\n\t\tserver_name index.html;\n\t\troot /var/www/html;\n\n\t\tlocation / {\n\t\tadd_header X-Served-By hostname;\n\t\t}\n\n\t\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/hbnb_static;\n\t\t}"
sed -i "s/server {/$replace/" /etc/nginx/nginx.conf
sudo service nginx restart
