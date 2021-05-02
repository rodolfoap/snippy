#!/usr/bin/env python3

import unittest
import inspect
import subprocess
from snippy import print_, debug, m2t, row
from snippy.experimental import prettyprint
from snippy.tensorflow import protectGpuMemory

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
		prettyprint(['Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', 'Hello,', 'World!', ['Hello,', 'World!']])
		row()

	def test_gpu(self):
		self.assertTrue(protectGpuMemory())

if __name__ == "__main__":
	unittest.main()
