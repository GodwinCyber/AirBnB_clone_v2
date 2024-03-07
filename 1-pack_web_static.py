#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    filename = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(filename)
        local("tar -czvf {} ./web_static/".format(archive_path))
        return archive_path
    except Exception as e:
        return None
