# Snippets

Just some Python3 snippets.

### Features
* setup.py - all distutils, setuptools features
* tests - unittest, pytest
* .tar.gz - source generation
* .deb generation
* _.rpm generation_
* virtualenv - install and put package into it

### Commands
* **make test** - run all tests (before, `pip install unittest2`)
* **make deb** - build Debian package (before, `apt install python3-stdeb`)
* **make source** - build source tarball (see `/dist`)
* **make daily** - make daily snapshot
* **make install** - install program
* **make init** - install all requirements
* **make clean** - clean project, remove temporary files
* **make deploy** - create virtual environment

### Notes

* Packaging based on `git clone git://github.com/vital-fadeev/python-package-template.git`
