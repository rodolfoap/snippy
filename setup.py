#!/usr/bin/env python3

from setuptools import setup, find_packages
from datetime import datetime

setup(name='snippy',
	version=datetime.today().strftime('%Y.%m.%d'),
	author='RodolfoAP',
	author_email='rodolfoap@gmail.com',
	url='https://github.com/rodolfoap/snippy',
	download_url='https://github.com/rodolfoap/snippy',
	description='Just some Python3 snippets...',
	long_description='Just some Python3 snippets...',

	packages = find_packages(),
	include_package_data = True,
	package_data = {
		'': ['*.txt', '*.rst'],
		'snippy': ['data/*.txt', 'data/*.zip'],
	},
	exclude_package_data = { '': ['README.txt'] },

	scripts = ['bin/snippy.example'],

	keywords='python3 tools utils internet www',
	license='GPL',
	classifiers=['Development Status :: 5 - Production/Stable',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: GNU Affero General Public License v3',
		'Topic :: Internet',
		'Topic :: Internet :: WWW/HTTP',
	],
	#setup_requires = ['python-stdeb', 'fakeroot', 'python-all'],
	install_requires = [open("requirements.txt", "r").read()[1]],
	)
