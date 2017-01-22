.. contents:: Table of contents

Introduction
============
The passwords encryption utility. Do not save your passwords as plaintext!

Installation
============
Install the fbi utility from PyPI
---------------------------------
::

    $ sudo pip install fbi

Install the fbi utility from GitHub
-----------------------------------
::

    $ sudo pip install git+git://github.com/korniichuk/fbi#egg=fbi

Upgrade the fbi utility from PyPI
---------------------------------
::

    $ sudo pip install -U fbi

or::

    $ sudo pip install --upgrade fbi

Uninstall the fbi utility
-------------------------
::

    $ sudo pip uninstall fbi

Development installation
========================
::

    $ git clone git://github.com/korniichuk/fbi.git
    $ cd fbi
    $ sudo pip install .

Quickstart
==========
**First**, init the fbi utility::

    $ fbi init

**Second**, encode password in a file::

    $ fbi encode PATH

Example::

    $ fbi encode ~/.key/netezza.enc

**Third**, decode password from a file::

    >>> from fbi import getpassword
    >>> path = "~/.key/netezza.enc"
    >>> passwd = getpassword(path)

CLI client
==========
A command line interface for managing an encoded password files.

Help
----
The standard output for –help::

    $ fbi -h

or::

    $ fbi --help

For information on using subcommand "SUBCOMMAND", do::

    $ fbi SUBCOMMAND -h

or::

    $ fbi SUBCOMMAND --help

Example::

    $ fbi init -h

Version
-------
The standard output for –version::

    $ fbi -v

or::

    $ fbi --version

Init the fbi utility
--------------------
::

    $ fbi init

Encode password in a file
-------------------------
::

    $ fbi encode PATH

Where:

* ``PATH`` -- destination path.

Example::

    $ fbi encode /home/titan/.key/netezza.enc

or::

    $ fbi encode ~/.key/netezza.enc

Decode password from a file
---------------------------
::

   $ fbi decode PATH

Where:

* ``PATH`` -- source path.

Example::

    $ fbi decode /home/titan/.key/netezza.enc

or::

    $ fbi decode ~/.key/netezza.enc

.. note:: Do not use ``$ fbi decode PATH`` for your automation scripting.

Client library
==============
A Python client for managing an encoded password files.

Get password from an encoded file
---------------------------------
::

    >>> from fbi import getpassword
    >>> getpassword(path)

Where:

* ``path`` -- source path.

Example::

    >>> from fbi import getpassword
    >>> path = "/home/titan/.key/netezza.enc"
    >>> passwd = getpassword(path)

or::

    >>> from fbi import getpassword
    >>> path = "~/.key/netezza.enc"
    >>> passwd = getpassword(path)
