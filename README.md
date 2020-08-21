#### Intro

A docker script for generating a set of pdfs (one per volume),
from the html source of the _Software Foundations_
book, available at: [https://softwarefoundations.cis.upenn.edu/](https://softwarefoundations.cis.upenn.edu/). I made this because I was having trouble 
getting other Make-based solutions to work on my computer.

Presuming you have docker, `run.sh` should be all thats needed.

#### Code 

A couple python scripts in `source` do the work, shelling out to a few linux
utilities here and there. The pdfs they generate are dictated by the input file
lists in `file_lists`. This (should)could probably be automated by scraping the `toc.html`
when the tar files get downloaded, but this yak shave has already taken too long
this morning. (Should also probably do version checking on it :))

#### Notes

- All copyright and credit belongs to the respective authors of these texts.

- For license see LICENSE.md
