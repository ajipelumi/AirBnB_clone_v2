#!/usr/bin/env bash
# Prepares a server for deployment

sudo apt update
sudo apt install nginx -y
sudo mkdir /data/ -p
sudo mkdir /data/web_static/ -p
sudo mkdir /data/web_static/releases/ -p
sudo mkdir /data/web_static/shared/ -p
sudo mkdir /data/web_static/releases/test/ -p
sudo touch /data/web_static/releases/test/index.html
echo "Hello Mike Rock, I'm Obidient and working" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
replacement="root \/var\/www\/html;\n\n\t\tlocation \/hbnb_static\/ {\n\t\t alias \/data\/web_static\/current\/hbnb_static;\n\t\t}"
sudo sed -i "s/root \/var\/www\/html;/$replacement/" /etc/nginx/nginx.conf
sudo service nginx restart
