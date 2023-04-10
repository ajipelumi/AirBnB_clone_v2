#!/usr/bin/python3
# A fabric script that deploys to a web server.
from fabric.api import local, env, put, run, sudo
from datetime import datetime
import os


env.hosts = ['52.23.245.131', '18.215.160.38']
env.user = "ubuntu"


def do_pack():
    """ Generates a tgz archive of the web_static folder. """
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    file = "web_static_" + time + ".tgz"

    # Create directory
    local('mkdir -p versions')

    # Create archive
    result = local('tar -cvzf versions/{} web_static'.format(file))
    if result.succeeded:
        return "versions/{}".format(file)
    else:
        return None


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

    result = sudo('mv {}/web_static/* {}/'.format(new_folder, new_folder))
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


def deploy():
    """ Creates and distributes an archive to our web servers. """
    path = do_pack()
    return do_deploy(path)


def do_clean(number=0):
    """ Deletes out-of-date archives. """
    number = int(number)

    if number == 0:
        number = 1

    result = local('ls -t versions | head -{}'.format(number), capture=True)
    all_files = local('ls versions', capture=True)
    for file in all_files.split('\n'):
        if file != result.strip():
            local('rm versions/{}'.format(file))

    result = run('ls -t /data/web_static/releases | head -{}'.format(number))
    all_files = run('ls /data/web_static/releases')
    for file in all_files.split('\n'):
        if file != result.strip():
            sudo('rm -rf /data/web_static/releases/{}'.format(file))
