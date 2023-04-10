#!/usr/bin/env bash
# This script sets up our web servers for the deployment of web_static.

# Update system
sudo apt update -y

# Install Nginx
sudo apt install nginx -y

# Create necessary folders
sudo [ -d /data/web_static/shared/ ] || sudo mkdir /data/web_static/shared/ -p
sudo [ -d /data/web_static/releases/test/ ] || sudo mkdir /data/web_static/releases/test/ -p
sudo touch /data/web_static/releases/test/index.html

# Write into index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership and group to ubuntu
sudo chown -R ubuntu:ubuntu /data/

replace="server_name _;\n\n\tlocation \/hbnb_static\/ {\n\t\t alias \/data\/web_static\/current\/;\n\t\tautoindex on;\n\t\tadd_header X-Served-By \$hostname;\n\t}"

# Copy replace to config file
sudo sed -i "s/server_name _;/$replace/" /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
