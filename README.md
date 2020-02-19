# 0x00. AirBnB clone - The console
# Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
# Python Scripts
* Used editors: vi, vim, emacs
* All files were interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All code used the PEP 8 style (version 1.7 or more)
* All files must be executable
* The length of files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
# Python Unit Tests
* Used editors: vi, vim, emacs
* All files end with a new line
* All test files are inside a folder tests
* We used the unittest module
* All test files should be python files (extension: .py)
* All test files and folders should start by test_
* Our file organization in the tests folder is the same as your project
* e.g., For models/base_model.py, unit tests are in: tests/test_models/test_base_model.py
* e.g., For models/user.py, unit tests are in: tests/test_models/test_user.py
* All tests are executed by using this command: python3 -m unittest discover tests
* We can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All modules have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All classes have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All functions (inside and outside a class) have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
# Execution
Your shell should work like this in interactive mode:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```