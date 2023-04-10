#!/usr/bin/python3
# A fabric script that generates a tgz archive.
from fabric.api import local
from datetime import datetime


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
