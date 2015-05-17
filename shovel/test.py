import os
from shovel import task

@task
def unit():
    os.system("nosetests --with-coverage --cover-package=image_count src/")


@task
def integration():
    os.system("nosetests tests/")

