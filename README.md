# Fasim-LongTarget: A tool for genome-wide accurate prediction of lncRNA/DNA binding

This repo is a fork of https://github.com/LongTarget/Fasim-LongTarget
A dockerfile build the tool inside a container has been added.
This repo is a fork of https://github.com/LongTarget/Fasim-LongTarget
A dockerfile build the tool inside a container has been added.

## Installation guide - Docker:
## Installation guide - Docker:
* build the docker image by running `docker build -t fasim . `
## Running the container:
* run the container: `docker run --rm -v $PWD:$PWD fasim -f1 $PWD/testDNA.fa -f2 $PWD/H19.fa -O $PWD/output/ -lg 40`
* `-v $PWD:$PWD` binds current working path, allowing to access it from inside the container
* * paths to file outside of the container must be provided in the form `$PWD/{relative_path}`
* Other options are to be provided exactly like they are with the original tool - refer to [the original readme](https://github.com/LongTarget/Fasim-LongTarget/blob/main/README.md)
