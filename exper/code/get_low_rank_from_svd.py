
import sys

import numpy as np

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Error: wrong number of arguments\n")
        sys.stderr.write("Usage: {} PREFIX\n".format(sys.argv[0]))
        return 1

    U_as_lists = []
    with open(sys.argv[1] + ".U", "rt") as U_file:
        for line in U_file:
            U_as_lists.append([float(x) for x in line.split()])
    V_as_lists = []
    with open(sys.argv[1] + ".V", "rt") as V_file:
        for line in V_file:
            V_as_lists.append([float(x) for x in line.split()])
    S_as_lists = []
    with open(sys.argv[1] + ".S", "rt") as S_file:
        S_list = [float(x) for x in S_file.readlines()]
        for i in range(len(S_list)):
            curr = []
            for j in range(i):
                curr.append(0)
            curr.append(S_list[i])
            for j in range(i+1, len(S_list)):
                curr.append(0)
            assert len(curr) == len(S_list)
            S_as_lists.append(curr)
    U = np.matrix(U_as_lists)
    V = np.matrix(V_as_lists)
    S = np.matrix(S_as_lists)

    res = U * S * V.transpose()

    prev_row_index = 0
    for index, x in np.ndenumerate(res):
        if index[0] != prev_row_index:
            sys.stdout.write("\n")
            prev_row_index = index[0]
        sys.stdout.write("{} ".format(x))


    return 0

if __name__ == "__main__":
    main()

