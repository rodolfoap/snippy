#!/usr/bin/env python3

from __future__ import print_function
import sys, os
import inspect
import datetime

# Timestamp conversion
def m2t(mstime):
	return datetime.datetime.fromtimestamp(mstime/1000.0)

# Row
def row(char='=', length=0, stdout=False):
	if(length==0): length, rows=os.get_terminal_size()
	print(char*length, file=(sys.stdout if stdout else sys.stderr))

def print_(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

# Debug using inspect
# Usage: debug(inspect.stack(), 'message')
def debug(stack, message=''):
	fi=inspect.getframeinfo((stack[0])[0]);
	print(">>> {}::{: >15}()[{}] [{}]".format(fi.filename, fi.function, fi.lineno, message), file=sys.stderr)
