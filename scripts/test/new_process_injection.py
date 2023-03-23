import os
import sys
import ctypes
import struct

# Define the code to be injected
code_to_inject = """
def greet(name):
    print(f"Hello, {name}!")
"""

# Get the process ID of the target process from the command line arguments
pid = int(156)

# Attach to the target process using ptrace
libc = ctypes.CDLL("libc.so.6")
libc.ptrace(0, pid, 0, 0)

# Import the missing constants and symbols from ctypes
PROT_READ = 0x1
PROT_WRITE = 0x2
PROT_EXEC = 0x4
MAP_PRIVATE = 0x2
MAP_ANONYMOUS = 0x20
dlopen = ctypes.CDLL(None).dlopen

# Allocate some memory in the target process's address space
addr = libc.mmap(None, 4096, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0)

# Write the code to the allocated memory
libc.ptrace(4, pid, addr, code_to_inject.encode())

# Call the `dlopen` function in the target process to load the injected code
dlopen_addr = dlopen(None, 1)
libc.ptrace(0x5555, pid, dlopen_addr, addr)

# Detach from the target process
libc.ptrace(17, pid, None, None)


