# NVDA Controller Client API 1.0 Fibonacci Documentation #

## Introduction ##
This client API allows an application to communicate to NVDA, in order to do such things as speak text or braille a message. Specifically in this repository, the Fibonacci program allows NVDA to speak and braille messages about numbers in the Fibonacci sequence.

The client API is implemented as a dll (dynamic link library). The functions in this dll can be called from any programming language that supports looking up and calling of any symbol in a dll (such as ctypes in Python), or by linking to it, for languages like C and C++.

## What is included? ##
Note: The header and library files are built along with nvdaHelper. If you want to build them yourself, please see source\nvdaHelper\building.txt in the NVDA source distribution for instructions. Alternatively, you can find a pre-built package at [http://www.nvda-project.org/nvdaControllerClient/](http://www.nvda-project.org/nvdaControllerClient/).

- [nvdaControllerClient32.dll](nvdaControllerClient32.dll): the dll that contains all the functions. This is for use in 32 bit applications. You can distribute this dll with your application.
- [nvdaControllerClient32.lib](nvdaControllerClient32.lib) and [nvdaControllerClient32.exp](nvdaControllerClient32.exp): The import and export libraries for [nvdaControllerClient32.dll](nvdaControllerClient32.dll) (used when linking with C/C++ code).
- [nvdaControllerClient64.dll](nvdaControllerClient64.dll), [nvdaControllerClient64.lib](nvdaControllerClient64.lib) and [nvdaControllerClient64.exp](nvdaControllerClient64.exp): same as above except for use in 64 bit applications.
- [nvdaController.h](nvdaController.h): a C header file containing declarations for all the provided functions.
- [fibonacci.py](fibonacci.py): a Python program that uses the NVDA controller client API to speak and braille messages for Fibonacci numbers.

## Available functions ##
All functions in this dll return 0 on success and a non-0 code on failier. Failier could be due to not being able to communicate with NVDA, or perhaps an incorrect usage of the function. The error codes that these functions return are always standard Windows error codes.

For definitions of all the functions available, please look at [nvdaController.h](nvdaController.h). The functions are documented with comments.

## License ##
The NVDA Controller Client API is licensed under the GNU Lesser General Public License (LGPL) version 2.1. In simple terms, this means you can use this library  in any application, however if you modify the library in any way you must contribute the changes back to the community under the same license.

Please see [license.txt](license.txt) in this directory for more details.
