#!/usr/bin/python3
# A fabric script that executes commands.
from fabric.api import env, put, sudo
import os


env.hosts = ['52.23.245.131', '18.215.160.38']
env.user = "ubuntu"

def do_deploy(archive_path):
    """ Distributes an archive to our web servers. """
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    result = put(archive_path, '/tmp/')
    if result.failed:
        return False

    # Uncompress the archive to a new folder
    basename = os.path.basename(archive_path)
    file = os.path.splitext(basename)[0]
    new_folder = '/data/web_static/releases/{}'.format(file)
    
    result = sudo('mkdir -p {}'.format(new_folder))
    if result.failed:
        return False

    result = sudo('tar -xzf /tmp/{} -C {}/'.format(basename, new_folder)) 
    if result.failed:
        return False

    # Delete the archive from the web server
    result = sudo('rm -rf /tmp/{}'.format(basename))
    if result.failed:
        return False

    # Delete the symbolic link /data/web_static/current from the web server
    result = sudo('rm -rf /data/web_static/current')
    if result.failed:
        return False

    # Create a new the symbolic link /data/web_static/current on the web server
    result = sudo('ln -sf {} /data/web_static/current'.format(new_folder))
    if result.failed:
        return False

    return True

