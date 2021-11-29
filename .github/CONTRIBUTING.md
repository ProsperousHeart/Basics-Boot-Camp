<a href='https://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

As this repo is meant for my students, this [CONTRIBUTING file](https://opensource.guide/starting-a-project/#writing-your-contributing-guidelines) is meant to explain how to contribute. In other words:
- how to propose fixes to items in this repo
- how to submit homework

# Found A Bug Or Have A Feature Request?
If you've noticed a bug or have a feature request, [make one](https://github.com/prosperousheart/Basics-Boot-Camp/issues/new)! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

## Fork & Create Branch
If this is something you think you can fix (a bug) or improve upon (feature request) then:
1. (if not already done so) [fork this](https://help.github.com/articles/fork-a-repo) Python Basics Boot Camp
2. create a branch with a descriptive name, e.g.:  `git checkout -b 42-add-YOURNAMEHERE-homework` where issue #42 is the ticket you're working on

# Pull Requests

## Making A Pull Request
Your first step (if you haven't already) is to switch back to your main branch & make sure it's up to date with the latest main branch:
```
git remote add upstream git@github.com:prosperousheart/Basics-Boot-Camp.git
git checkout main
git pull upstream main
```

Then make your changes on your feature or issue branch via your local copy then push!

```
git checkout 42-add-YOURNAMEHERE-homework
git rebase main
git push --set-upstream origin 42-add-YOURNAMEHERE-homework
```

Finally, go to GitHub and [make a Pull Request](https://help.github.com/articles/creating-a-pull-request).

Github Actions are not currently set up, so confirmations and checking will be done manually.

## Keeping Your PR Updated
I would add this section in from [here](https://github.com/activeadmin/activeadmin/blob/63146bd720031fc7deee18acab026b2b4c5054e7/CONTRIBUTING.md#keeping-your-pull-request-updated) but the following should work for our purposes:
```
git checkout main
git pull upstream main
git checkout 42-add-YOURNAMEHERE-homework
git merge main 42-add-YOURNAMEHERE-homework
git push
```

## Merging A PR (Maintainers Only)
While there is great info [here](https://github.com/activeadmin/activeadmin/blob/63146bd720031fc7deee18acab026b2b4c5054e7/CONTRIBUTING.md#merging-a-pr-maintainers-only) for general repos, this boot camp is a bit different.

A PR can only be merged into master by a maintainer if:
- it has been approved by repo owner
- it is up to date with current master
- it is clear what you are requesting

# Important Resources

TBD