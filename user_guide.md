## Project Overview
Main purpose of the application is to extract developers' opinions on certain libraries from a popular question and answer site [stackoverflow.com](stackoverflow.com). Since stackoverflow provides data dump of their posts using mysql database, we have used that data dump in the development machine. We have also provided cached data in csv file so that general users can test the application without installing mysql or downloading 500+ GB of data dump.

Since the opinions posted in stackoverflow does not contain any version information, we have collected the version information from [mavenrepository.com](mavenrepository.com) which is a package manager for Java libraries. Since mavenrepository does not provide any data dump or API, we have scraped the site to get the relevant content. However, in some cases, the scraper fails to collect data because of the site's processes. To overcome this situation, we have also cached the collected version information in local csv files so that without reaching out to the maven repo and scraping the site, developers can start testing the application.

After collecting the library related opinion and version information, we provide the summarized data on a library which is the final output of this application.

The background and objective of this project is provided in more details in the project [README](https://github.com/minaoar/library-version-wise-opinion-extration/blob/main/README.md) file.

This is a script based application without any graphical user interface.
It is developed on Python programming language. Hence, to run the application, users will need to be able to run Python commands from command line interface. The instructions for running the application is provided in the [how to get started](https://github.com/minaoar/library-version-wise-opinion-extration/edit/main/README.md#how-to-get-started) section of README file.
The application sequence diagram is provided [here](https://github.com/minaoar/library-version-wise-opinion-extration/blob/main/library-opinions-workflow.png).

## Project Directory Structure
Source code of the project is located under ./source folder.
Data files (positive/negative keywords, cached data file with Stack Overflow opinions, scraped data files from maven repository, and opinion output files) are located inside ./data folder. 
Test code is located under ./test folder.
All other files (readme, license etc.) are located in the root folder.

### Data Files
INPUT FILES:
- Stackoverflow data files (e.g., stackoverflow_gson_2.8.csv) start with prefix stackoverflow_ and contains the library (and version number) name only. 
- Files (e.g., gson_version_info.csv) which start with library names contain library information (license, version, release date) collected from maven repository.
- There are some sentiment files (negative-words, positive-words.txt) which are used to identify opinionated sentences from the stackoverflow posts.

OUTPUT FILES:
- The output files contain the name in the format stackoverflow_<library>_opinion.csv (e.g., stackoverflow_gson_opinion.csv.)
  > <img width="978" alt="output" src="https://user-images.githubusercontent.com/5583535/206252379-59cb9dd2-06c6-495c-ae09-e7b73e873c37.png">

### Source Code
The main file which extracts opinions and maps the opinions with library name and versions is library_version_opinion_extraction.py. All other files are helper modules for specific purposes.



