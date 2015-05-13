import os
from shovel import task

@task
def unit():
    os.system("ls -ltr")
