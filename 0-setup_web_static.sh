#!/usr/bin/env bash
# This script sets up our web servers for the deployment of web_static.

# Update system
apt update

# Install Nginx
apt install -y nginx

# Create necessary folders and files
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

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
echo "$content" | tee /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership and group to ubuntu
chown -R ubuntu:ubuntu /data/

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
service nginx restart
