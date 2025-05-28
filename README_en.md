<div align="center">

<h1><img src="assets/images/logo.png" width="128px"><br>TkinterCLI - Make Tkinter Development Effortless</h1>

</div>

![PyPI - Version](https://img.shields.io/pypi/v/tkintercli?logo=pypi&label=Latest%20version)
![PyPI - Downloads](https://img.shields.io/pypi/dd/tkintercli?logo=pypi&label=Daily%20downloads)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tkintercli?logo=pypi&label=Monthly%20downloads)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Albatros329/tkintercli/python-publish.yml?logo=python&logoColor=white&label=Build%20status)

**:fr: [French](README.md)** - **:gb: [English](README_en.md)**

TkinterCLI is a command-line tool that simplifies project creation with Tkinter. With this tool, you can quickly set up a complete project structure, manage a multi-page navigation system, and take advantage of pre-installed icons, all without tedious manual configuration.

## Features
- **Automatic Project Creation** - Generate a complete Tkinter project structure in a single command
- **Multi-page Navigation System** - Simplified management of interface transitions
- **Built-in Icon Library** - Access to a collection of ready-to-use icons
- **Virtual Environment Support** - Option to automatically create a dedicated virtual environment
- **Organized Architecture** - Clear file structure separating views, controllers, and resources
- **Intuitive Command Line Interface** - Simple commands to create and extend your application

## Installation
### From PyPi (recommended)
```
pip install tkintercli
```
### From Github
```
git clone https://github.com/Albatros329/tkintercli.git
cd tkintercli/
python setup.py install
```

## Usage

Arguments in [] are required, while those in () are optional.

### Create a new project
```
tkintercli new [NAME] (--venv)
```

### Add a new page
```
tkintercli add page [NAME]
```