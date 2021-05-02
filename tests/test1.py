#!/usr/bin/env python3

import unittest
import inspect
import subprocess
from snippy.tools import print_, debug, m2t
from snippy.experimental.pretty import pretty

class Test(unittest.TestCase):

	def test_print_(self):
		debug(inspect.stack())
		value = True
		result = True
		self.assertEqual(value, result)
		print_('Hello, World!')
		print('Hello, World!')
		debug(inspect.stack(), 'Test ends here.')
		milliseconds=int(subprocess.getoutput('/bin/date +%s%N|/bin/cut -b1-13'))
		print(m2t(milliseconds))
		pretty(['Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', ['Hello,', 'World!']])

if __name__ == "__main__":
	unittest.main()
