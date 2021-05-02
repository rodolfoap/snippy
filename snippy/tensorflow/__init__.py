#!/usr/bin/env python3

# Tensorflow: avoid filling ALL the GPU memory
def protectGpuMemory():
	import tensorflow
	gpu_devices = tensorflow.config.experimental.list_physical_devices("GPU")
	for device in gpu_devices: tensorflow.config.experimental.set_memory_growth(device, True)
	return True
