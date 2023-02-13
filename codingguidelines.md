# Coding guidlines <!-- omit in toc -->

Welcome to the coding notebook! This notebook contains guidelines and best practices for writing clean and well-structured code. In this notebook, you will learn about the following tools:

1. **Poetry**: Poetry is a package manager for Python projects. It allows you to manage dependencies, create virtual environments, and publish packages. We will be using Poetry to manage the dependencies for our project.
2. **Linter**: A linter is a tool that checks the source code for potential errors and provides suggestions for improving the code's quality. We will be using pylint as our linter.
3. **Git**: Git is a distributed version control system that allows multiple developers to work on a project simultaneously. We will be using Git to track changes to our code and collaborate with others.

By following the guidelines in this notebook, you will ensure that your code is maintainable, scalable, and easy to collaborate on. Let's get started!

## Table of contents <!-- omit in toc -->

- [Installing poetry on macOS](#installing-poetry-on-macos)
- [Poetry example](#poetry-example)
- [Installing git on macOS](#installing-git-on-macos)
- [Setup Github on macOS](#setup-github-on-macos)
- [Using linter for coding](#using-linter-for-coding)
- [Python class](#python-class)

## Installing poetry on macOS

**Andre**: How to install poetry on macOS?

**ChatGPT**: To install poetry on macOS, you can use the following steps:

Open a terminal window on your Mac.

Use the command

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

to download and run the poetry installer.

Once the installation is complete, you can use the command

```sh
poetry --version
```

to check that poetry has been correctly installed.

You can also add poetry to your shell profile. You can do this by using the command

```sh
poetry completions bash &gt; $(brew --prefix)/etc/bash_completion.d/poetry.bash-completion
```

if you use bash or

```sh
poetry completions zsh &gt; "$(brew --prefix)/share/zsh/site-functions/_poetry"
```

if you use zsh.

(optional) To use poetry virtual environment, you need to install pyenv-virtualenv. You can do this by using the command

```sh
brew install pyenv-virtualenv
```

(optional) To use poetry with pyenv, you need to set the path of poetry to pyenv. You can do this by using the command

```sh
echo 'eval "$(pyenv init -)"' &gt;&gt; ~/.bash_profile
```

or

```sh
echo 'eval "$(pyenv init -)"' &gt;&gt; ~/.zshrc
```

depending on your shell.

Once the installation is complete, you can use the

```sh
poetry
```

command to manage your Python projects, create virtual environments, and manage dependencies.
***
**Andre**: Why should we use poetry to manage Python dependencies?

**ChatGPT**: Poetry is a package management tool for Python that allows developers to easily manage and install dependencies for their projects. It can help to simplify the process of managing dependencies by handling things like creating virtual environments, installing packages, and managing package versions. Some benefits of using Poetry over other package management tools include:

1. It creates isolated virtual environments for your projects, which can help to prevent conflicts between dependencies.
2. It has a simple and user-friendly command-line interface that makes it easy to use.
3. It can automatically generate lock files which help to ensure that your project is always using the same version of dependencies, which can help to prevent issues caused by dependency updates.
4. It supports both Python 2 and 3 and you can specify the Python version you want to use.
5. It also support both PEP 508 and PEP 440 for specifying dependencies.

Overall, using Poetry to manage Python dependencies can help to make the process of managing dependencies more streamlined and less error-prone, which can lead to fewer bugs and more reliable code.

## Poetry example

**Andre**: Poetry is especially useful when collaborating in teams so that people's code is based on the same package versions. For publishing Python packages Poetry offers additional useful features.
***

**Andre**: Can you show an example python project created with poetry and poetry init?

**Chatgpt**: Sure! Here's an example of creating a Python project using Poetry:

1. Initialize a new project

    ```sh
    poetry init
    ```

2. Answer the questions prompted by Poetry

    ```sh
    This command will guide you through creating your pyproject.toml configuration file.

    Step 1 of 6: Project name []: My Python Project
    Step 2 of 6: Version [0.1.0]: 0.1.0
    Step 3 of 6: Description []: A simple Python project created with Poetry
    Step 4 of 6: Author [Your Name &lt;you@example.com&gt;, n to skip]: Your Name &lt;you@example.com&gt;
    Step 5 of 6: License [MIT, n to skip]: MIT
    Step 6 of 6: Compatible Python versions [^3.6, n to skip]: ^3.8
    ```

3. Add a dependency to the project:

    ```sh
    poetry add requests
    ```

4. Create a file for the project, for example: ```main.py```

    ```python
    import requests

    def main():
        response = requests.get("https://api.github.com/repos/python/cpython")
        print(response.json())

    if __name__ == "__main__":
        main()
    ```

5. Run the project:css

    ```sh
    poetry run python main.py
    ```

That's it! You have now created a Python project using Poetry and added a dependency. Poetry will manage the dependencies for you, so you don't have to worry about version compatibility issues or having to manually install packages.

**Andre**: Can you show how to publish a project to pypi which was created with poetry?

**ChatGPT**: Yes, I can show you how to publish a Python project to PyPI using Poetry.

Here are the steps to follow:

1. Create a Python project using Poetry: If you have not created your project yet, you can create one using the following command:

    ```sh
    poetry new my_project
    ```

2. Configure your project: In the project directory, you can open the `pyproject.toml` file and configure your project by adding the project name, version, description, etc.

3. Add dependencies: If your project requires any dependencies, you can add them to the `pyproject.toml` file under the `[tool.poetry.dependencies]` section.

4. Create a distribution package: To create a distribution package of your project, you can run the following command:

    ```sh
    poetry build
    ```

5. Publish the package to PyPI: To publish the package to PyPI, you need to create an account on the PyPI website and then run the following command:

    ```sh
        poetry publish
    ```

It will ask you to enter your PyPI username and password. After entering the credentials, Poetry will publish the distribution package to PyPI.

That's it! Your Python project is now published on PyPI and is available for others to install and use.
***

## Installing git on macOS

**You**: How to install git on macOS?

**ChatGPT**: There are several ways to install Git on macOS, but the easiest way is to use the package manager Homebrew.Install Homebrew by opening a terminal window and running the following command:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/main/install.sh)"
```

Once Homebrew is installed, use it to install Git by running the following command:

```sh
brew install git
```

Verify the installation by running the following command:

```sh
git --version
```

This should display the version of Git that is currently installed on your system.

Alternatively, you can also download the installer from the official website of Git and install it manually.
You can also install Git via Xcode Command Line Tools if you're running an older version of macOS. To install it you can use the following command:

```sh
xcode-select --install
```

And then you can check if git is installed by running

```sh
git --version
```

Both methods will install the latest version of Git on your Mac.
***

## Setup Github on macOS

**You**: How to setup Github on macOS?

**ChatGPT**: Install Git on your macOS by following the instructions provided in the previous answer.

Open a terminal window and generate a new SSH key:

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

This will create a new SSH key pair, with the public key stored in ```~/.ssh/id_rsa.pub``` and the private key stored in ```~/.ssh/id_rsa```.

Add your new SSH key to your GitHub account:Go to your GitHub account settings and select "SSH and GPG keys".Click on "New SSH key" and give it a title, like "macOS"Copy the contents of your public key file (```~/.ssh/id_rsa.pub```) and paste it into the "Key" field on GitHub.Click on "Add SSH key" to save the key.

Test the connection by running the following command:

```sh
ssh -T git@github.com
```

You should see a message like "Hi username! You've successfully authenticated, but GitHub does not provide shell access."

Now that you have Git and SSH set up, you can clone an existing repository or create a new one on GitHub.

To clone an existing repository, copy the repository URL from GitHub and use the

```sh
git clone
```

command to download it to your local machine:

```sh
git clone git@github.com:username/repository.git
```

To create a new repository, log in to your GitHub account and select "New repository" from the "+" button. Give your repository a name and select "Public" or "Private" as desired.

Once your repository is created, you can push your local files to the new repository using the

```sh
git push
```

command:

```sh
git push origin master
```

This is a basic setup process for Github on macOS, you can further customize your setup to your needs and preferences.
***
**You**: What is the idea behind a SSH key pair?

**ChatGPT**: A SSH key pair is a method of securely logging into a remote computer or server without the need for a password. It consists of two keys: a public key and a private key. The public key is stored on the remote server and the private key is stored on the local computer or device.

The idea behind a SSH key pair is based on the concept of public-key cryptography. In this type of cryptography, there are two keys: a public key and a private key. The public key can be shared freely and is used to encrypt data that is sent to the owner of the private key. The private key is kept secret and is used to decrypt the data that was encrypted with the corresponding public key.

When you log in to a remote server using a SSH key pair, the remote server uses your public key to encrypt a challenge message and send it back to your local computer. Your local computer then uses your private key to decrypt the challenge and prove that it is the owner of the corresponding public key. Once the remote server has verified your identity, it grants you access to the server without the need for a password.

The main advantage of using a SSH key pair over a password is that it is more secure. Passwords can be guessed, stolen, or otherwise compromised, but a private key can only be used by the person who has possession of the key. Additionally, SSH keys can be set to expire, so if a key is lost or stolen you can remove it from the server and create a new one.

It is important to keep your private key safe and secure, as anyone who gets access to it will be able to log in to the servers that you have configured to use the corresponding public key.
***
**Andre**: What is the difference between git and github?

**ChatGPT**: Git and GitHub are related but distinct technologies.

Git is a version control system (VCS) that allows you to keep track of changes made to your code over time. It keeps a history of all your code versions, allowing you to revert to previous versions, collaborate with others, and work on multiple features simultaneously without conflicts. Git is a command-line tool and can be used on any operating system.

GitHub, on the other hand, is a web-based platform built on top of Git that provides hosting for Git repositories, as well as additional features such as bug tracking, project management, and collaboration tools. GitHub provides a web interface for managing Git repositories, and it can be used to share code with others, collaborate on open-source projects, or host your own code for personal use.

In summary, Git is a tool for version control, and GitHub is a web-based platform for hosting and collaborating on Git repositories. While Git is a command-line tool that you can use locally, GitHub provides a web interface for managing and sharing your Git repositories, making it easier to collaborate with others.

**Andre**: What are the most useful and common git commands?

**ChatGPT**: Here are some of the most useful and commonly used Git commands:

```git init```: Initialize a new Git repository.

```git clone```: Clone an existing Git repository from a remote source.

```git add```: Add files to the staging area to prepare them for commit.

```git commit```: Commit changes to the repository.

```git push```: Push changes to a remote repository.

```git pull```: Fetch and merge changes from a remote repository.

```git branch```: Manage branches in a Git repository.

```git checkout```: Switch between branches or restore files to a specific version.

```git merge```: Merge one or more branches into the current branch.

```git status```: Show the status of files in the working directory and the staging area.

```git log```: Show a history of commits.

```git diff```: Show changes between commits, branches, and more.

These commands form the core of Git, and by using them you can perform most of the common Git tasks. There are many more Git commands available, and as you gain more experience with Git, you may find other commands to be useful for your workflow.

## Using linter for coding

**Andre**: Can you give me an example for using pylint in coding?

**ChatGPT**: Certainly! Here's an example of using ```pylint``` in a Python code file:

```python
# example.py

def add(a, b):
    """
    This function adds two numbers together.
    """
    return a + b

def subtract(a, b):
    """
    This function subtracts one number from another.
    """
    return a - b
```

To run ```pylint``` on this code, you can use the following command in your terminal:

```sh
pylint example.py
```

Here's an example of the output that you might see:

```sh
No config file found, using default configuration
************* Module example
example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
example.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
example.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------
Your code has been rated at 6.67/10 (previous run: 6.67/10, +0.00)
```

In this example, ```pylint``` reports three issues with the code: two missing function docstrings and one missing module docstring. ```pylint``` assigns a score to the code based on its analysis, with a score of 10 being the highest and a score of 0 being the lowest.

You can use ```pylint``` to automatically check your code for common errors, best practices, and other issues, helping you to improve the quality of your code.

## Python class

**Andre**: What is the idea of a class in python?

**Chatgpt**: In Python, a class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). Classes define a new data type and provide a way of creating objects of that type, which can be used to represent real-world entities, like a person, an animal, or a bank account.

Classes provide a means of bundling data and functions that work on that data within one unit, or object. Objects created from a class are called instances, and they can have their own state and behavior. The member variables represent the state or attributes of the object, while the member functions represent the behavior of the object.

Here's a simple example of a class in Python:

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")

dog = Dog("Fido", "Labrador", 3)
print(dog.name) # Output: Fido
dog.bark() # Output: Woof!
```

In this example, the `Dog` class has three member variables `name`, `breed`, and `age`, and one member function `bark()`. The `__init__` method is a special method that is called when an object of the class is created, and it is used to initialize the attributes of the object.
