
# Releasing `cantometrics`

To see the list of available commands and scripts type into your terminal:

`make help`

<small><strong>Note:</strong> This code has been tested for Mac/Windows, but if you are on a windows, please submit a pull request so we can make it easier to run. This step assumes you have a working distribution of `make`. For installation instructions please update XCode or follow the specific guidelines for installing `make` on your system. </small>

## Check the data

The data are currently stored within Google-Drive sheets. Make sure you can access these before trying to create a release.


## Update data from Google Drive

If you have access from Google Drive, you can initiate the downloads using the command:

```make download```

Please inspect any errors and warnings here carefully before proceeding. 

## Process the Data

The Cantometrics data is processed into CLDF format in two parts.

First we convert the data to long format and split any multiple codings into their root forms using 

```make process```

We then create the CLDF format and reorganise the metadata tables using

```make process2```


## Create a release

Create a new release by navigating to https://github.com/theglobaljukebox/cantometrics/releases
and pushing "Draft a new release". Choose a release tag prefixed with `v` to make 
sure the release will be picked up by ZENODO.

Allow ZENODO some time to process the release, then search for the release on
ZENODO, copy the corresponding DOI badge and paste it at the end of the release
description.

