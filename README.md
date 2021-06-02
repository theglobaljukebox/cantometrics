![](https://img.shields.io/github/v/release/theglobaljukebox/cantometrics)

# Cantometrics Data

This repository is for pulling, formatting, validating and cleaning the Cantometrics dataset.

Raw data is presented in three data tables within raw/

| file             | description                                              |
|------------------|----------------------------------------------------------|
| data.csv         | Cantometric codings of songs in the sample.              |
| songs.csv        | Metadata on the songs coded in data.csv                  |
| societies.csv    | Metadata on the societies from which the songs originate.|

Cantometrics data is also available in CLDF format within cldf/ 
Within the CLDF dataset, multicodings have been parsed to the original values. 

| file             | description                                              |
|------------------|----------------------------------------------------------|
| data.csv         | Long format Cantometrics codings of the songs in the sample.|
| songs.csv        | Metadata on the songs coded in data.csv                  |
| societies.csv    | Metadata on the societies from which the songs originate.|

Additionally there is information on variable and coding descriptions within etc/ 

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
