#! /bin/sh

DATA_DIR="../data"
PYTHON_BIN="python3"

if [ $# -ne 2 ]; then
	echo "ERROR: wrong number of arguments" > /dev/stderr
	echo "USAGE: $0 RANK GRAPH_FILE" > /dev/stderr
	exit 1
fi

K=$1
GRAPH_FILE=$2
GRAPH_NAME=`basename ${GRAPH_FILE} | cut -d "." -f 1`

if [ ! -e ${DATA_DIR}/sparse/${GRAPH_NAME}-sparse.txt ]; then
	${PYTHON_BIN} edgelist_to_sparsematrix.py ${GRAPH_FILE} > ${DATA_DIR}/sparse/${GRAPH_NAME}-sparse.txt
fi

if [ ! -e ${DATA_DIR}/dense/${GRAPH_NAME}-dense.txt ]; then
	${PYTHON_BIN} edgelist_to_densematrix.py ${GRAPH_FILE} > ${DATA_DIR}/dense/${GRAPH_NAME}-dense.txt
fi

sh svd.sh ${DATA_DIR}/sparse/${GRAPH_NAME}-sparse.txt ${DATA_DIR}/SVD/${GRAPH_NAME}-SVD-${K} ${K}

${PYTHON_BIN} get_low_rank_from_svd.py ${DATA_DIR}/SVD/${GRAPH_NAME}-SVD-${K} > ${DATA_DIR}/lowrank/${GRAPH_NAME}-lowrank-${K}.txt

ERR=`${PYTON_BIN} get_norm_of_difference.py 2 ${DATA_DIR}/dense/${GRAPH_NAME}-dense.txt ${DATA_DIR}/lowrank/${GRAPH_NAME}-lowrank-${K}.txt`

echo ${GRAPH_NAME}\t${K}\t${ERR}

