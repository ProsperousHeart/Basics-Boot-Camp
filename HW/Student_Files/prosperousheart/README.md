# Expectations

<a href='https://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

This folder is where all of my answers to the homework will go.

As of Nov 19, 2021 - this is just the framework to provide an outline for incoming students.

# Testing

As of Jan 25, 2023 - I am working on also adding in python automated testing. This will not be covered in the basics bootcamp but it will be in another one. I am providing the materials for those who wish to leverage the examples for their own portfolios.

I have structured the code to have a folder per project, so when running the tests it is easier to work with.

When in the folder you wish to run the tests from, call `pytest` to run all tests.

For keywords, run:  `pytest -k keyword_here`

For help, run:  `pytest -h`

If using `input` be sure to run the following to [disable all capture](https://docs.pytest.org/en/7.2.x/how-to/capture-stdout-stderr.html): `pytest -s` (otherwise it might error out)
