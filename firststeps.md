# Lecture Reinforcement Learning: First Steps <!-- omit in toc -->

## Table of contents <!-- omit in toc -->

- [Welcome](#welcome)
- [Installing pyenv on macOS](#installing-pyenv-on-macos)
- [Installing Python](#installing-python)
- [Installing Visual Studio Code on macOS](#installing-visual-studio-code-on-macos)
- [First fun with Reinforcement Learning](#first-fun-with-reinforcement-learning)

## Welcome

Hello and welcome to the Reinforcement Learning course!

We are excited to embark on this journey of exploring the cutting-edge field of AI and machine learning. This course is designed to provide you with a solid foundation in Reinforcement Learning, its algorithms, and applications. You will learn about various approaches to solving complex decision-making problems and how to implement these algorithms in practice. We are confident that by the end of this course, you will have a deep understanding of Reinforcement Learning and be able to apply it to real-world problems. So let's get started and see where this adventure takes us!

***

However, before we can start we need to prepare a few things. We use Python to implement the algorithms from the lecture. But why do we use Python? Chatgpt gives us a brief information about this:

**Andre**: Why should we use Python for Reinforcement Learning?

**ChatGPT**:

1. Easy to learn and use: Python has a simple and intuitive syntax, making it easy for beginners to pick up and start coding.
2. Widely adopted: Python is one of the most widely-used programming languages, with a large and active community of developers and users. This means that you have access to a wealth of resources and tools that can help you get started with reinforcement learning.
3. Libraries and Frameworks: Python has many libraries and frameworks specifically designed for reinforcement learning, such as TensorFlow, Keras, OpenAI Gym, and PyTorch, which provide pre-built tools and functions to help you build, train and test your models.
4. Interoperability: Python is compatible with a wide range of tools and technologies, which makes it easy to integrate reinforcement learning models into existing systems and applications.
Overall, Python's ease of use, versatility, and rich ecosystem make it an ideal choice for reinforcement learning projects.

For the Python installation, we use Pyenv, and its advantages are discussed below.

***

## Installing pyenv on macOS

**Andre**: How to install pyenv on macos?

**ChatGPT**: To install pyenv on macOS, you can use the following steps:

Install Xcode command line tools by running

```sh
xcode-select --install
```

in your terminal.

Install Homebrew, a package manager for macOS, by running

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

in your terminal.

Follow the instructions in the terminal to add Homebrew to your `PATH`:

```sh
echo '# Set PATH, MANPATH, etc., for Homebrew.' >>/Users/YOURUSER/.zprofile
echo 'eval "$(opt//homebrew/bin/brew shellenv)"' >>/Users/YOURUSER/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Replace `YOURUSER` by the username of your system.

Use Homebrew to install pyenv by running

```sh
brew install pyenv
```

in your terminal.

Add the following lines to your shell profile file (e.g. .bash_profile, .zshrc)

```sh
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
```

If you do not have a .zshrc file, then you must first create one with the following command.

```sh
touch ~/.zshrc
```

You can then open this with the following command.

```sh
open ~/.zshrc
```

Restart your terminal or run ```source ~/.zshrc``` to reload the shell profile

Verify the installation by running ```pyenv --version``` which should show the version of pyenv you have installed.

Note: If you're using Zsh instead of bash, you need to add the above export and eval lines to your .zshrc file instead.
***

## Installing Python

Next, we want to install a version of Python to run our first Python script. For this we install Python 3.10.

**You**: How to install python 3.10 with pyenv and set it to the global version on your computer?

**ChatGPT**: To install Python 3.10 using pyenv and set it as the global version on your computer, you can use the following steps:

1. Install Python 3.10 using pyenv:

    ```sh
    pyenv install 3.10.0
    ```

2. Set Python 3.10 as the global version:

    ```python
    pyenv global 3.10.0
    ```

3. Verify that Python 3.10 is set as the global version by running:

    ```sh
    pyenv version
    ```

Note: If the python version you want to install is not available in pyenv, you can also build it from source using

```sh
pyenv install --build 3.10.0
```

***
**Andre**: What are the advantages of pyenv?

**ChatGPT**: Pyenv is a tool that allows you to easily switch between multiple versions of Python on a single system. Some advantages of using pyenv include:

Isolation of different Python versions: Pyenv allows you to have multiple versions of Python installed on your system, and easily switch between them. This can be useful if you need to work on projects that use different versions of Python.

Easy installation and management of Python versions: Pyenv makes it easy to install and manage different versions of Python, and keeps them isolated from the system Python.

Compatibility with other tools: Pyenv is compatible with other Python tools such as pip, virtualenv, and pyenv-virtualenv. This allows you to easily manage dependencies for your projects and keep them isolated from each other.

Shell Integration: Pyenv also allows you to integrate with your shell, which makes it easy to switch between different versions of Python.

No need to use Sudo: You don't need to use Sudo to install Python through pyenv, which can help you avoid permission errors.
***

## Installing Visual Studio Code on macOS

To write Python code we need an editor. For this we want to use Visual studio code.

**Andre**: How to install Visual Studio Code on macOS?

**ChatGPT**: To install Visual Studio Code on macOS, you can follow these steps:

Go to the [Visual Studio Code website](https://code.visualstudio.com) and download the macOS version of the software.

Once the download is complete, open the downloaded file, which will be a .zip file. Extract the contents of the file.

Open the extracted folder and find the Visual Studio Code.app file.

Drag the Visual Studio Code.app file to the "Applications" folder to install the software.

Once the installation is complete, you can open Visual Studio Code by searching for it in Spotlight or by navigating to the "Applications" folder and double-clicking the Visual Studio Code.app file.

You can also create a shortcut for Visual Studio Code on the Dock by opening the "Applications" folder, right-clicking the Visual Studio Code.app file, and selecting "Keep in Dock".

Note: You might get a warning from macOS when trying to open the app for the first time, because it was downloaded from the internet. This is a security feature of macOS, you can override the warning by right-clicking the app and selecting "Open".
***
**Andre**: Why is Visual Studio Code a good IDE for Python?

**ChatGPT**: Visual Studio Code (VS Code) is a popular Integrated Development Environment (IDE) for Python development, and is considered a good choice for several reasons:

**IntelliSense**: VS Code includes IntelliSense, a code-completion tool that provides suggestions for variable and function names, and can also display documentation for the code you're writing. This can help you write code more quickly and accurately.

**Debugging**: VS Code has a built-in debugging tool that allows you to set breakpoints, inspect variables, and step through your code. This can make it easier to find and fix bugs in your code.

**Linting and formatting**: VS Code has built-in support for linting and formatting tools such as Pylint, Flake8 and autopep8. These tools can help you catch errors and style issues in your code before you run it.

**Extension ecosystem**: VS Code has a large extension ecosystem that provides additional functionality, including support for specific frameworks, libraries, and languages. This allows you to customize the IDE to suit your specific needs.

**Cross-platform**: VS Code is available for Windows, macOS, and Linux, so you can use it on any platform you prefer, and your settings and extensions will sync across all devices via cloud.

**Built-in Git support**: VS Code has built-in support for Git, which makes it easy to manage your code and collaborate with other developers.

**Lightweight and fast**: VS Code is lightweight and fast, which makes it easy to use and navigate, and it doesn't consume too many resources.

All of these features make VS Code a powerful and flexible IDE for Python development, and it's no wonder why it's become one of the most popular choices among developers.
***

## First fun with Reinforcement Learning

After doing so much theory. Let's load our first reinforcement script.
Follow the steps from the video.
Here are the steps from the video:

1. Create a virtual environment:

    ```sh
    python -m venv .venv
    ```

2. Activate your virtual environment:

    ```sh
    source .venv/bin/activate
    ```

3. Install all requiered packages:

    ```sh
    pip install gym
    pip install pygame
    ```

4. Copy the following code to a python file:

```python
""" play the cart pole game
"""

import gym

# choose the gym environment you want to run
env = gym.make("CartPole-v1", render_mode="human")

# reset the environment to its initial state
observation, info = env.reset()

while True:
    observation = env.reset()
    for _ in range(200):
        env.render()
        action = env.action_space.sample()
        observation, reward, terminated, truncuated, info = env.step(action)
        if terminated or truncuated:
            print(f"Game finished after {_ +1} steps.")
            break
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

env.close()
```
