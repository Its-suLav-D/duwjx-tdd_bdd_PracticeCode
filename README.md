# TDD / BDD Practice Code

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)

This repository contains the practice code for the labs in **IBM-CD0241EN-SkillsNetwork Introduction to Test Driven Development**

## Contents

- [Lab 1: Running Test with Nose](labs/01_running_tests_with_nose/README.md)
- [Lab 2: Writing Test Assertions](labs/02_writing_test_assertions/README.md)
- [Lab 3: Creating an Initial State Using Text Fixtures](labs/03_test_fixtures/README.md)
- [Lab 4: Running Test Cases with Coverage](labs/04_test_coverage/README.md)
- [Lab 5: Using Factories and Fakes](labs/05_factories_and_fakes/README.md)
- [Lab 6: Mocking Objects](labs/06_mocking_objects/README.md)
- [Lab 7: Practicing TDD](labs/07_practicing_tdd/README.md)

## Development Environment

These labs are designed to be executed in the IBM Developer Skills Network Cloud IDE environment, however you can work on them locally using Docker and Visual Studio Code with the Remote Containers extension to provide a consistent repeatable disposable development environment for all of the labs in this course.

You will need the following software installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com)
- [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension from the Visual Studio Marketplace

All of these can be installed manually by clicking on the links above or you can use a package manager like **Homebrew** on Mac of **Chocolatey** on Windows.

### Using Remote Containers

To bring up the development environment you should clone this repo, change into the repo directory, and then open Visual Studio Code using the `code .` command. VS Code will prompt you to reopen in a container and you should say **yes**. This will take a while as it builds the Docker image and creates a container from it to develop in.

```bash
git clone https://github.com/ibm-developer-skills-network/duwjx-tdd_bdd_PracticeCode.git
cd duwjx-tdd_bdd_PracticeCode
code .
```

Note that there is a period `.` after the `code` command. This tells Visual Studio Code to open the editor and load the current folder of files. When prompted to **Reopen in Contaner** select that option and it will build a development for you inside a Docker container.

Once the environment is loaded you should be placed at a `bash` prompt in the `/app` folder inside of the development container. This folder is mounted to the current working directory of your repository on your computer. This means that any file you edit while inside of the `/app` folder in the container is actually being edited on your computer. You can then commit your changes to `git` from either inside or outside of the container.

## Author

John Rofrano, Senior Technical Staff Member, DevOps Champion, @ IBM Research

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>

# Benefits of TDD

1. It Saves time when developing
2. In orer to create a DevOPs CI/CD pipeline, all testing
   must be automated
3. It ensure that future changes don't break your code

# Popular Testing Frameworks

1. xUnit Frameworks

   - JUnit for Java
   - PyUnit for Python
   - NUnit for .NET
   - Embunit for C/C++

2. Packages for Python
   - Nose
   - Coverage
   - Pachunnio

# Summary and Highlights

1. To run TDD tests in Bash, you can call unittest or call nosetests if Nose is installed.

2. Unlike unittest, Nose can color code test results, report code coverage, and list missing test cases.

3. Testing frameworks provide tools that simplify testing conditions.

4. Assertions are checks to determine if tests have passed or failed.

5. To create assertions in Python, developers can use the assert() function or any additional PyUnit asserts.

6. Happy paths verify that a function returns positive outcomes when expected, while sad paths verify that a function responds to exceptions appropriately and without breaking.

7. Test fixtures establish a known initial state before and after each test.

8. Test fixtures are helpful for many testing situations such as creating mock objects and loading a database with a known set of data.

9. Test fixtures operate at three levels of specificity:

   - Module

   - Test case

   - Test

# Run Python unit Test

You can make the output more useful by adding the -v flag to turn on verbose mode. Run the command below for more useful output

```
python3 -m unittest
python3 -m unittest -v
```

## Install and Run nose

To see verbose output from nose, run nosetests -v. The verbose output from Nose will return nicer output than from unittest because it only returns the docstring comments:

```
pip install nose

nosetests -v

```

## Install Pinocchio and Run

```
pip install pinocchio
nosetests --with-spec --spec-color
```

## Install Coverage and Run with Missing

```
pip install coverage

nosetests --with-spec --spec-color --with-coverage

coverage report -m
```

## Setup Configuration

```
[nosetests]
verbosity=2
with-spec=1
spec-color=1
with-coverage=1
cover-erase=1
cover-package=triangle

[coverage:report]
show_missing = True

```
