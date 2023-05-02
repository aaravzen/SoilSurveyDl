# SoilSurveyDl
Soil Survey Geographic Database Batch Downloader

# Prerequisites

Run `pip3 install requests`

or install the python requests library somehow else.

# How to run

Now copy some of the files from `soup.links.out` to `download_these.in` - see the examples in the file.

You can cut/paste them, and then you don't even have to keep track of which ones you've already done.

Run `python3 dl.py` to download the files listed in `download_these.in`
