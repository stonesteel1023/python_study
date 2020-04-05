import json
import subprocess

from fabric.api import *
import requests

env.user = 'ubuntu'
env.key_filename = 'clava-keypair.pem'
env.hosts = ['123.123.123.123', '123.123.123.123']


def demo():
    env.hosts = ['54.180.162.201', '123.123.123.123'


def prod():
    env.hosts = ['0.0.0.0']


def app():
    with shell_env(DJANGO_SETTINGS_MODULE='clava.settings.demo'):
        with cd('/home/ubuntu/clava/'):
            run('git pull origin master')
            run('sudo /usr/local/bin/pip install -r requirements/prod.txt')
            run('/usr/bin/python3 manage.py migrate')
            run('pkill -HUP -f [g]unicorn')

# template, static 배포하는데 굳이 지유니콘 켜서 할 필요 없어서 
def template():
    with cd('/home/ubuntu/clava/'):
        run('git pull origin master')


def static():
    with cd('/home/ubuntu/clava/'):
        run('/usr/bin/python3  manage.py collectstatic')