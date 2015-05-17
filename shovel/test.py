import os
from shovel import task

@task
def unit():
    os.system("nosetests src/")


@task
def integration():
    os.system("nosetests tests/")


@task
def path(path):
	os.system("nosetests " + path + "/" )