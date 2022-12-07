# Contribute to Library Opinion Project

Thanks for your interest in contributing to Library Opinion project 🎉 This page will give you a quick
overview of how things are organized and most importantly, how to get involved.

## Table of contents

1. [OSS Component Usage Policy](#oss-component-usage-policy)
2. [How to Submit Changes](#how-to-submit-changes)
3. [Style Guide](#style-guide)

## OSS Component Usage Policy
Since this project is licensed under MIT License, if you use any OSS component, 
please ensure that the component is licensed under only the permissive licenses
(e.g., MIT, BSD, Apache) approved by the [Open Source Initiative](https://opensource.org/licenses).
* Third party components or libraries should be included in the [requirement.txt](https://github.com/minaoar/library-version-wise-opinion-extration/blob/main/requirements.txt) file along with the license information (as done currently) so that we can be sure in single place that we are complying with the OSS policy.

## Particpate in Discussion
You can participate in discussion from the [Discussion](https://github.com/minaoar/library-version-wise-opinion-extration/discussions) section 
of this repository. You are welcome to add new discussion, choose a category, and ask any question or provide any idea.

## How to Submit Changes
Whether you want to add a new feature/improvement of fix a bug,
please ensure first that a related issue is posted in the [issue list](https://github.com/minaoar/library-version-wise-opinion-extration/issues).

### Creating an Issue
(If you are new to this repository and if you can have question regarding the project, please consider opening a discussion 
from the [Discussion](https://github.com/minaoar/library-version-wise-opinion-extration/discussions) board as described above before directly creating an issue with initial queries.)

When you create an issue, please provide a meaningful title and appropriate 
label (bug/enhancement/documentation etc.). 
- In case of bug, kindly provide the steps how it can be reproduced. More details [here](#reporting-a-bug)
- In case of an enhancement, please provide why this is a good idea.
- If you can write in simple way how you are planning/expecting to develop,
it would be highly appreciated.

### Reporting a Bug
Even with our meticulous efffort, there can be bugs and we will be glad to get those reported.
While reporting a bug to the [issue list](https://github.com/minaoar/library-version-wise-opinion-extration/issues), please consider adding following information:
- [ ] First of all, add label 'bug' to the issue
- [ ] Provide a clear title that it's a bug
- [ ] Provide what problem you are facing or you are assuming will occur
  - [ ] Kindly provide the version number of branch name of the application you are running
  - [ ] Provide the date/time, operating system, and datasource (database or sample data) of the bug, if applicable 
- [ ] Provide any kind of steps or ideas to reproduce
- [ ] If you have any sort of screenshot or log that you recorded during the bug discovery, please kindly add that to the issue

### Contributing Source Code
To make changes to project's code base, you need to fork then clone the GitHub 
repository and build the project from source. You'll need to make sure that 
you have a development environment consisting of a Python distribution 
including header files, pip, git, mysql installed. 

You cannot push your changes directly to the main branch without a pull request.
Please follow the guidelines of [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)(PR) for creating and submitting a PR.

To initially run and test the application, you will need to download Stack Overflow 
data dump as outlined [here](https://gist.github.com/minaoar/aafd5f97d15a1aad8ccdb650ba2d4d49).


## Style Guide
- Please provide clear and brief summary of your modifications in git commit.
- Since this repository includes only Python code, please follow style guide from 
[PEP 8 Style Guide for Python Code](https://peps.python.org/pep-0008/)(python.org).
