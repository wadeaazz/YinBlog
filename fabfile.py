from fabric.api import env,run
from fabric.operations import sudo


GIT_REPO = 'https://github.com/wadeaazz/YinBlog'
env.user = 'yinzhou'
env.password = 'Wade81587686'

env.hosts = 'www.yz213.com'
env.port = '22'

def deploy():
    source_folder = '/home/yinzhou/sites/yin.yz213.com/YinBlog'
    run('cd %s $$ git pull' % source_folder)
    run("""
        cd {} $$
        ../env/bin/pip install -r requiremengs.txt $$
        ../env/bin/python3 manage.py collectstatic --noinput $$
        ../env/bin/python3 manage.py migrate
    """.format(source_folder)
    )
    sudo('restart gunicorn-www.yz213.com')
    sudo('service nginx reload')
