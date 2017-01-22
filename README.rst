.. contents:: Table of contents

Installation
============
Install the keys utility from PyPI
----------------------------------
::

    $ sudo pip install keys

Install the keys utility from GitLab
------------------------------------
::

    $ sudo pip install git+git://github.com/korniichuk/keys#egg=keys

Upgrade the keys utility from PyPI
----------------------------------
::

    $ sudo pip install -U keys

or::

    $ sudo pip install --upgrade keys

Uninstall the keys utility
--------------------------
::

    $ sudo pip uninstall keys

Development installation
========================
::

    $ git clone git://github.com/korniichuk/keys.git
    $ cd keys
    $ sudo pip install .

Quickstart
==========
**First**, init the keys utility::

    $ keys init

**Second**, encode password in a file::

    $ keys encode PATH

Example::

    $ keys encode ~/.key/netezza.enc

**Third**, decode password from a file::

    >>> from keys import getpassword
    >>> path = "~/.key/netezza.enc"
    >>> passwd = getpassword(path)

CLI client
==========
A command line interface for managing an encoded password files.

Help
----
The standard output for –help::

    $ keys -h

or::

    $ keys --help

For information on using subcommand "SUBCOMMAND", do::

    $ keys SUBCOMMAND -h

or::

    $ keys SUBCOMMAND --help

Example::

    $ keys init -h

Version
-------
The standard output for –version::

    $ keys -v

or::

    $ keys --version

Init the keys utility
---------------------
::

    $ keys init

Encode password in a file
-------------------------
::

    $ keys encode PATH

Where:

* ``PATH`` -- destination path.

Example::

    $ keys encode /home/titan/.key/netezza.enc

or::

    $ keys encode ~/.key/netezza.enc

Decode password from a file
---------------------------
::

   $ keys decode PATH

Where:

* ``PATH`` -- source path.

Example::

    $ keys decode /home/titan/.key/netezza.enc

or::

    $ keys decode ~/.key/netezza.enc

.. note:: Do not use ``$ keys decode PATH`` for your automation scripting.

Client library
==============
A Python client for managing an encoded password files.

Get password from an encoded file
---------------------------------
::

    from keys import getpassword

    getpassword(path)

Where:

* ``path`` -- source path.

Example::

    from keys import getpassword

    path = "/home/titan/.key/netezza.enc"

    passwd = getpassword(path)

or::

    from keys import getpassword

    path = "~/.key/netezza.enc"

    passwd = getpassword(path)
