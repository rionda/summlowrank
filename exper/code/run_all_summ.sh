#! /bin/sh

DATA_DIR="../data"
PYTHON_BIN="python3"

SUMMRES_TO_MATRIX_BIN="summ_to_dense_matrix"

if [ $# -ne 3 ]; then
	echo "ERROR: wrong number of arguments" > /dev/stderr
	echo "USAGE: $0 K SUMM_RES GRAPH_FILE" > /dev/stderr
	exit 1
fi

K=$1
SUMM_RES=$2
GRAPH_FILE=$3
GRAPH_NAME=`basename ${GRAPH_FILE} | cut -d "." -f 1`

if [ ! -e ${DATA_DIR}/dense/${GRAPH_NAME}-dense.txt ]; then
  echo -n "creating dense matrix for original graph..." 
  ${PYTHON_BIN} edgelist_to_densematrix.py ${GRAPH_FILE} > ${DATA_DIR}/dense/${GRAPH_NAME}-dense.txt
  echo "done"
fi

if [ ! -e ${DATA_DIR}/summlowrank/${GRAPH_NAME}-summlowrank-${K}.txt ]; then
  echo "creating low-rank matrix from summary..."
  ${SUMMRES_TO_MATRIX_BIN} ${GRAPH_FILE} ${SUMM_RES} 2> ${DATA_DIR}/summlowrank/${GRAPH_NAME}-summlowrank-${K}.txt
  echo "done"
fi

echo -n "computing error..."
ERR=`${PYTHON_BIN} get_norm_of_difference.py 2 ${DATA_DIR}/dense/${GRAPH_NAME}-dense.txt ${DATA_DIR}/summlowrank/${GRAPH_NAME}-summlowrank-${K}.txt`
echo "done. Error: ${ERR}"

echo "${GRAPH_NAME}\t${K}\t${ERR}" > /dev/stderr

