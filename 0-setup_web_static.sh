#!/usr/bin/env bash
# This script sets up our web servers for the deployment of web_static.

# Update system
sudo apt update

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

# Configure server
SERVER_CONFIG="\
server	{
		listen 80 default_server;
		listen [::]:80 default_server;
		root /var/www/html;
		index index.html index.htm index.nginx-debian.html;
		server_name _;
		location /hbnb_static {
					add_header X-Served-By \$hostname;
					alias /data/web_static/current;
		location / {
					add_header X-Served-By \$hostname;
					try_files \$uri \$uri/ =404;
		}
}"

# Place configuration in nginx file
bash -c "echo -e '$SERVER_CONFIG' > /etc/nginx/sites-enabled/default"

# Restart Nginx
sudo service nginx restart
