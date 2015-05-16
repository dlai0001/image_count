## Requirements ## 
* Python 2.7 /w PyPi (pip)
* Virtual Env
	[sudo] pip install virtualenv

## Dev Setup ##

1. Setup virtual env to ensure you have a clean Python Sandbox.

	Davids-MacBook-Pro:image_count dlai$ virtualenv env
	New python executable in env/bin/python2.7
	Also creating executable in env/bin/python
	Installing setuptools, pip...done.

	Davids-MacBook-Pro:image_count dlai$ source env/bin/activate
	(env)Davids-MacBook-Pro:image_count dlai$

2.  Install required dependencies.

	> pip install -r requirements.txt

## Available Commands ##

* Run the program.

	> python ./image_count.py 

* Run the unit or integration tests.

	> shovel test.unit

	> shovel test.integration


