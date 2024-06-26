#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ["52.201.228.176", "54.236.49.211"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean:"""
    number = int(number)
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
