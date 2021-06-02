https://img.shields.io/github/v/release/theglobaljukebox/cantometrics

# Cantometrics Data

This repository is for pulling, formatting, validating and cleaning the Cantometrics dataset.

## Getting started

To see the list of available commands and scripts type into your terminal:

`make help`

<small><strong>Note:</strong> This code has been tested for Mac/Windows, but if you are on a windows, please submit a pull request so we can make it easier to run. This step assumes you have a working distribution of `make`. For installation instructions please update XCode or follow the specific guidelines for installing `make` on your system. </small>

## Collect google drive data

`make download`

## Convert data to CLDF format
`make process`

## Update dependencies

`make update`
