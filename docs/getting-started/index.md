<a href='http://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

# Getting Started

Welcome to the Python Basics Boot Camp! This guide will help you get set up and ready to start learning Python.

## Prerequisites

- A computer with internet access
- Basic computer skills (file management, installing software)
- Enthusiasm to learn!

## Installation

### Installing Python

You'll need Python installed on your computer. We recommend Python 3.8 or later.

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important:** Check "Add Python to PATH" during installation

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Verify Installation

Open a terminal/command prompt and run:
```bash
python --version
# or
python3 --version
```

You should see the Python version displayed.

## Setting Up Your Environment

### Virtual Environment (Recommended)

We recommend using a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

For more detailed instructions, see our [Virtual Environment Tutorial](../tutorials/recreating-virtual-environments-virtualwrapper.md) or [Transitioning to UV](../tutorials/transitioning-to-uv.md).

### Installing Jupyter

To run the interactive notebooks locally:

```bash
pip install jupyter notebook
```

## Course Structure

This bootcamp is organized into 3 weeks:

### Week 1: Python Basics
Learn fundamental Python syntax, variables, data types, and basic operations. Complete the calculator homework assignment.

### Week 2: Functions & Modules
Dive into functions, iterators, generators, and modular programming. Build a rock-paper-scissors game.

### Week 3: I/O & Exceptions
Master file input/output, error handling, and debugging. Create a text reader and writer application.

## How to Use This Site

- **Navigation Tabs**: Use the tabs at the top to navigate between weeks
- **Interactive Lab**: Access JupyterLite to run notebooks in your browser (no installation needed!)
- **Search**: Use the search bar to find specific topics
- **Code Examples**: Click the copy icon to copy code snippets

## Learning Tips

1. **Practice Regularly**: Code every day, even if just for 15 minutes
2. **Type the Code**: Don't just read - type out the examples yourself
3. **Experiment**: Modify examples to see what happens
4. **Ask Questions**: Use the community forums or GitHub discussions
5. **Complete Homework**: Implementation is key to learning

## Time Commitment

- **Training Content**: ~1-2 hours per week
- **Homework**: ~2-3 hours per week
- **Total**: Plan for 3-5 hours per week for 3 weeks

But remember - you can go at your own pace!

## Need Help?

- Check out our [Helpful Hints](../tutorials/Helpful_Hints.md)
- Review the [Tutorials](../tutorials/index.md) section
- Join the community Discord server (link in course materials)
- Connect on [LinkedIn](https://linkedin.com/in/kkeeton/)

## Ready to Start?

Head over to [Week 1](../BC_Weeks/Week_1/index.md) to begin your Python journey!
