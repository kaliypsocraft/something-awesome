# Something Awesome Project 24T3

There is a `REPORT.md` file which is a digest/summary of all that was conducted throughout
the project's lifespan. It consists of weekly updates, basic background information on CTF challenges among other things.
In the repository there consists five directories which contain challenges in relation to the directory. For example
crypto/ will contain all CTF challenges related to cryptography. 

## Table of Contents

- [Features](#features)
- [Scripts](#scripts)
- [Acknowledgments](#acknowledgments)

## Features

Within the `REPORT.md` file there are hyperlinks which automatically send the reader to a particular challenge. Each 
write-up contains challenge-type, difficulty-level, the flag, thought-process and tools utilised. They are located within
each challenge directory.

### Scripts
TODO: deprecate `generate_challenge_file.sh`
`generate_challenge_file.sh` is a shell script which takes in two arguments `<challenge_type> <challenge_name>` and creates a directory and markdown file associated with the challenge. 
#### Use Case:
This automated the process in creating a 

`generate_write_ups.sh` is a shell script which when run within a challenge directory i.e. /crypto, it will generate a `.md` file associated with each exercise within a challenge type e.g. `/crypto/<exercise>.md`. 
#### Use Case:
This was good for existing directories which did not have a write-up file associated with it. 

### Acknowledgements

