#!/bin/bash 

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

echo "RUNNING TESTS"

if [ $# -gt 0 ] ; then
	python -m unittest discover -s $DIR -p "$@"
else
	python -m unittest discover -s $DIR -p 'test_*.py'
fi
