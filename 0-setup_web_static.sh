#!/usr/bin/env bash
# This script sets up our web servers for the deployment of web_static.

# Update system
sudo apt -y update

# Install Nginx
sudo apt install -y nginx

# Create necessary folders and files
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Write into index.html
content="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

# Write content into index.html
echo "$content" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership and group to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Copy location block to config file
sudo sed -i 's/server_name _;/server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/g' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
