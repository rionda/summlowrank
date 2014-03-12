import math
import sys

def main():
    if len(sys.argv) != 4:
        sys.stderr.write("Error: wrong number of arguments\n")
        sys.stderr.write("Usage: {} NORM ORIG SUMM\n".format(sys.argv[0]))
        return 1

    norm = int(sys.argv[1])
    assert norm == 1 or norm == 2

    orig = []
    with open(sys.argv[2], 'rt') as input_file:
        for line in input_file:
            orig.append([float(x) for x in line.split()])

    summ = []
    with open(sys.argv[3], 'rt') as summ_file:
        i = 0
        for line in summ_file:
            summ.append([float(x) for x in line.split()])
            assert len(summ[i]) == len(orig[i])
            i += 1

    curr_err = 0
    for i in range(len(summ)):
        for j in range(len(summ)):
            curr_err += math.pow(abs(orig[i][j] - summ[i][j]), norm)
    if norm == 2:
        curr_err = math.sqrt(curr_err)

    print(curr_err / math.pow(len(summ), 2))


if __name__ == "__main__":
    main()

