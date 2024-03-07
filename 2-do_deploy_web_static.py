#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers."""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            archive_file = archive_path.split("/")[1]
            archive_folder = ("/data/web_static/releases/" + archive_file.split(".")[0])
            run("mkdir -p {}".format(archive_folder))
            run("tar -xzf /tmp/{} -C {}".format(archive_file, archive_folder))
            run("rm /tmp/{}".format(archive_file))
            run("mv {}/web_static/* {}".format(archive_folder, archive_folder))
            run("rm -rf {}/web_static".format(archive_folder))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(archive_folder))
            return True
        except:
            return False
    return False
