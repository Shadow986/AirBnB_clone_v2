#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers."""
from fabric.api import env
from os.path import isfile
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']

def deploy():
    """Creates and distributes an archive to your web servers."""
    archive_path = do_pack()
    if not isfile(archive_path):
        return False
    return do_deploy(archive_path)
