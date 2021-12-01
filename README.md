# Testing python code with pytest lib

## Prerequisites
Create virtual environment: ```python3 -m venv myenv```
Start virtual environment: ```. myenv/bin/activate```
Install dependencies: ```pip3 install -r requirements.txt```

With pytest you can select which tests to run by decorators, run parallel tests, and continue running where you stopped etc. But pytest requires intallation of pytest. The python built in "unittest" does not have as much functionality as pytest but unittest does not require installation of any third part lib so for smaller projects unittest could be an alternative.

## Naming tests
### Files
It is good practise to always name your **files**, that contains your test cases, **starting
with "test_"**, like test_my_class.py. But the file names can also end with "\_test.py". Running pytest without mentioning a filename will
run all files of format test_\*.py or \*_test.py in the current directory and subdirectories but not a file named testMyclass.py or a_test_file.py.

### Test cases
Pytest requires the test **function names to start with test\*** so it will not run any function in the files that does not start with test\*.

## Running
### All tests
You run your tests from the project root folder by for example executing:
```pytest```
or
```pytest <filename>```  
(-v stands for verbose and gives extra output)

### Only tests matching specific name
To only execute the test functions containing a string in its name we can use the following syntax:
```pytest -k <substring>```

### Only tests with specific marker
To only execute the test functions that has a specific marker: ```pytest -m <markername>```  
For example, a test decorated with ```@pytest.mark.great``` can be executed with ```pytest -m great```  
(**NOTE** To get rid of marker warnings, **declare custom markers in pytest.ini file**)

## Example
Lets say you have a structure like this:

```
project/
|
|-- src/
|   |-- my_program.py
|   |-- __init__.py
|
|-- tests/
|   |-- test_my_program.py
|   |-- prov_my_program.py
|   |-- my_program_test.py
|   |-- __init__.py
|
|-- test_my_project.py
|-- do_test_my_program.py
```

my_program.py contains your program code. All other files contains unit tests.
In this case, if you run pytest in your project folder, all tests in test_my_project.py, tests/test_my_program.py and tests/my_program_test.py will be executed, but not do_test_my_program.py or tests/prov_my_program.py.

### Source
https://www.tutorialspoint.com/pytest

