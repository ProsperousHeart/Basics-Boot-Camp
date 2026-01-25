<a href='http://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

# Overview

In our [week 3 training](../../Week_3) we brought all of our basic training together. You learned about:
1. Input/Output
2. Exceptions & Assertions

This implementation work expects you to bring in all of what you learned into this program. 

# Week 3 Implementation Work Expectations

## Requirements

1. Use functions - remember to keep these as small as possible
2. Read in a file - for this exercise, use the `Alice In Wonderland Text.txt` in [Files](Files)
3. Search for a text phrase (pattern)  in the file
4. Keep a log file
   1. Have a new file created for each day - do not overwrite your log file
   2. Be sure to ALWAYS include the following:
      1. search phrase used
      2. number of times found (if any)
      3. separator for when you have multiple runs
   3. If not found, notate in log file.
   4. If found, notate line number in log file.

## Nice To Have

1. Ability for user to turn on or off printing line in log file.
2. Ability to print synopsis of run on CLI

# Reminders & Additional Tips

For this project you will likely be using:
- [str.rstrip()](https://docs.python.org/3/library/stdtypes.html#str.rstrip)
- module `re` ([regular expressions](https://docs.python.org/3/library/re.html) & specifically [re.search()](https://docs.python.org/3/library/re.html#re.search) ... though there are other options out there
  - [Guru99 examples](https://www.guru99.com/python-regular-expressions-complete-tutorial.html)
  - [Google For Education - Regular Expressions](https://developers.google.com/edu/python/regular-expressions)
  - [Geeks For Geeks:  re.search() vs re.findall()](https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/)
- regex tools:
  1. [regexr](https://regexr.com/)
  2. [regex101](https://regex101.com/)
- [checking if a file exists](https://www.pythontutorial.net/python-basics/python-check-if-file-exists/)