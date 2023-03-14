#!/bin/sh


umask 0000 &&
exec /usr/bin/fasim_wrapper.py "$@"