#!/usr/bin/env python3

from __future__ import print_function
import sys
import inspect
import datetime

# Timestamp conversion
def m2t(mstime):
        return datetime.datetime.fromtimestamp(mstime/1000.0)

# STDERR print
def print_(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

# Debug using inspect
# Usage: debug(inspect.stack(), 'message')
def debug(stack, message=''):
        fi=inspect.getframeinfo((stack[0])[0]);
        print(">>> {}::{: >15}()[{}] [{}]".format(fi.filename, fi.function, fi.lineno, message), file=sys.stderr)

# Tensorflow: avoid filling ALL the GPU memory
def protectGpuMemory():
	import tensorflow
	gpu_devices = tensorflow.config.experimental.list_physical_devices("GPU")
	for device in gpu_devices: tensorflow.config.experimental.set_memory_growth(device, True)
