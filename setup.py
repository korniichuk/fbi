# -*- coding: utf-8 -*-

from os.path import dirname, join
from setuptools import setup

setup(
    author="Ruslan Korniichuk",
    author_email="ruslan.korniichuk@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    description="The password encryption utility",
    download_url="https://github.com/korniichuk/fbi/archive/0.1.zip",
    entry_points={"console_scripts":"fbi=fbi.fbi:main"},
    include_package_data=True,
    install_requires=[
        "rsa"
    ],
    keywords=["cryptography", "fbi", "key", "python", "python2"],
    license="Public Domain",
    long_description=open(join(dirname(__file__), "README.rst")).read(),
    name="fbi",
    packages=["fbi"],
    platforms=["Linux"],
    url="https://github.com/korniichuk/fbi/",
    version="0.1a7",
    zip_safe=True
)
