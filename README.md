# Fasim-LongTarget: A tool for genome-wide accurate prediction of lncRNA/DNA binding

This repo is a fork of https://github.com/LongTarget/Fasim-LongTarget
A dockerfile build the tool inside a container has been added.

## Installation guide - Docker:
* build the docker image by running `docker build -t fasim . `
## Running the container:
* run the container: `docker run --rm -v $PWD/$PWD cf554a3a867a  -f1 $PWD/testDNA.fa -f2 $PWD/H19.fa -O output/ -lg 40`
* paths to file outside of the container must be provided in the form `$PWD/{relative_path}`
