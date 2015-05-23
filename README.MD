[![Build Status](https://travis-ci.org/dlai0001/image_count.svg)](https://travis-ci.org/dlai0001/image_count)

## Requirements
* Python 2.7 /w PyPi (pip)
* Virtual Env
	[sudo] pip install virtualenv

## Dev Setup

Setup virtual env to ensure you have a clean Python Sandbox.

	Davids-MacBook-Pro:image_count dlai$ virtualenv env
	New python executable in env/bin/python2.7
	Also creating executable in env/bin/python
	Installing setuptools, pip...done.

Then activate it when you're ready to develop.

	Davids-MacBook-Pro:image_count dlai$ source env/bin/activate
	(env)Davids-MacBook-Pro:image_count dlai$

Install required dependencies.

	> pip install -r requirements.txt

At this point you can run any of shovel commands in the next section.


After you're done developing.  Use `deactivate` to exit your virtual env.

	> deactivate


## Available Commands


* Run the program.

	> ./image_count.py -k ROTTEN_TOMATOES_API_KEY

* Run the unit or integration tests.

	> shovel test.unit	# performs unit test with code coverage

	> shovel test.integration # performs integration tests, no code coverage

* Run integration tagged by feature/test type

	> shovel test.integration performance # run only tests tagged with performance.

* Run all tests.

	> shovel test.all

* Run watcher that reruns unit test upon any files changed.

	> shovel watch

Note about watch: To it will only run unitests in the same package level
as the file that's affected in order to optimize the scope of unit tests
that are run on each save.  It will do code coverage, but only for files
tested.

## About the design

* A movie image is defined as any property in the rotten tomatoes response
that contains a image extension in the file name.

* Unit tests placed in corresponding './tests' folder of their respective
module to aid in making large refactoring easier.  This also works with
running the isolated set of affected unit tests (with code coverage) via
the `shovel watch` task

* Dependency injection done via constructor injection to aid in substituting
out module dependencies for unit and integration testing.

* Tests on the integration level are tagged, so they can be run selectively.
This allows developers to run slower running tests filtered by feature or type
without running the whole suite.