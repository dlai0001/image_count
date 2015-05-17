import os
from shovel import task

COVERAGE_SETTINGS = " --with-coverage --cover-branches --cover-min-percentage=95 --cover-package=image_count "

@task
def unit():
    os.system("nosetests src/" + COVERAGE_SETTINGS)


@task
def integration():
    os.system("nosetests tests/")


@task
def path(path):
	os.system("nosetests " + path + "/" + COVERAGE_SETTINGS)