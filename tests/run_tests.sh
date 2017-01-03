#!/bin/bash 

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

echo "RUNNING TESTS"

cd "$DIR"

if [[ $# -ne 1 ]] ; then
	python -m unittest $(echo test_*.py | sed 's/.py//g' | sed 's/^\.\///')
else
	python -m unittest "$@"
fi
