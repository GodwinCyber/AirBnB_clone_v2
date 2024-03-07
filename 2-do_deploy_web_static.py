#!/usr/bin/python3
from fabric.api import *
from os import path

env.hosts = ['52.201.228.176', '54.236.49.211']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        print(file_name)
        no_ext = file_name.split(".")[0]
        print(no_ext)
        remote_path = "/data/web_static/releases/" + no_ext + "/"
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}".format(remote_path))
        run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, remote_path))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(remote_path, remote_path))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(remote_path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(remote_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
