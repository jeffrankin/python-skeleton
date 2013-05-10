python-skeleton
===============

Taken from "Learn Python the Hard Way"

Also need directories bin and docs

Next, install the following python packages:

1. pip from http://pypi.python.org/pypi/pip
2. distribute from http://pypi.python.org/pypi/distribute
3. nose from http://pypi.python.org/pypi/nose/
4. virtualenv from http://pypi.python.org/pypi/virtualenv

nosetests should be run from the project dir not from tests

Whenever you want to start a new project, just do this:

1. Make a copy of your skeleton directory. Name it after your new project.
2. Rename (move) the NAME module to be the name of your project or whatever you want to call your root module.
3. Edit your setup.py to have all the information for your project.
4. Rename tests/NAME_tests.py to also have your module name.
5. Double check it’s all working using nosetests again.
6. Start coding.

Things to be done after:

1. Read about how to use all of the things you installed.
2. Read about the setup.py file and all it has to offer. Warning, it is not a very well-written piece of software, so it will be very strange to use.
3. Make a project and start putting code into the module, then get the module working.
4. Put a script in the bin directory that you can run. Read about how you can make a Python script that’s runnable for your system.
5. Mention the bin script you created in your setup.py so that it gets installed.
6. Use your setup.py to install your own module and make sure it works, then use pip to uninstall it.