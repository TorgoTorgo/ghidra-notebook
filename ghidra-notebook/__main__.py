from ipykernel.kernelapp import IPKernelApp
from .ghidra_kernel import GhidraKernel
IPKernelApp.launch_instance(kernel_class=GhidraKernel)
