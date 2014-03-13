#! /bin/sh

REDSVD="redsvd"

if [ $# -ne 3 ]; then
	echo "Error: wrong number of argument" > /dev/stderr
	echo "USAGE: $0 input output rank" > /dev/stderr
	exit 1
fi

$REDSVD -f sparse -m SVD -i $1 -o $2 -r $3

