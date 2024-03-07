#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives."""
from fabric.api import env, local, run
from os.path import isdir

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """Deletes out-of-date archives."""
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1

    local("cd versions; ls -t | tail -n +{} | xargs rm -rf --".format(number))
    run("cd /data/web_static/releases; ls -t | tail -n +{} | xargs rm -rf --".format(number))
