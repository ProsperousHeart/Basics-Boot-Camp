<a href='https://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

# Tutorials

This section contains helpful tutorials and guides for common tasks and tools you'll encounter while learning Python.

## Available Tutorials

### Development Environment

- **[Transitioning to UV](transitioning-to-uv.md)** - Modern Python package management with UV
- **[Recreating Virtual Environments](recreating-virtual-environments-virtualwrapper.md)** - Guide to virtualenv and virtualenvwrapper
- **[Makefile Windows Setup](makefile-windows-setup.md)** - Setting up Make on Windows for automation

### Code Quality

- **[Clean Code Before PR](clean-code-before-pr.md)** - Best practices for code review and pull requests

## Tutorial Categories

### Package Management
Learn different approaches to managing Python packages and dependencies:
- Traditional virtualenv
- Modern UV tool
- Requirements files vs pyproject.toml

### Build Tools
Automate common development tasks:
- Using Makefiles
- Running tests
- Linting and formatting

### Code Quality
Write better, more maintainable code:
- Pre-commit checks
- Code review guidelines
- Testing best practices

## Additional Resources

For more Python resources, check out:
- The instructor's [cheatsheets repository](https://github.com/ProsperousHeart/cheatsheets)
- [Python official documentation](https://docs.python.org/)
- [Real Python tutorials](https://realpython.com/)

## Contributing

Have a tutorial to share? Found an issue with an existing tutorial? Feel free to:
- Open an issue on GitHub
- Submit a pull request
- Reach out on LinkedIn

## Quick Reference

Common tasks covered in these tutorials:

```bash
# Create virtual environment with UV
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
uv add package-name

# Run tests
make test  # if Makefile is set up

# Format code
make format
```

For detailed instructions, see the individual tutorial pages.
