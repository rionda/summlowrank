import sys

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Error: wrong number of arguments\n")
        sys.stderr.write("Usage: {} FILE\n".format(sys.argv[0]))
        return 1

    adj_lists = dict()
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            if line[0] == "#":
                continue
            tokens = line.split()
            head = int(tokens[0])
            tail = int(tokens[1])
            if head != tail: # XXX WE ARE IGNORING SELF LOOPS!
                if head not in adj_lists:
                    adj_lists[head] = set([tail])
                else:
                    adj_lists[head].add(tail)
                if tail not in adj_lists:
                    adj_lists[tail] = set([head])
                else:
                    adj_lists[tail].add(head)
         
        vertex_ids = dict()
        curr_id = 0
        for vertex in sorted(adj_lists.keys()):
            vertex_ids[vertex] = curr_id
            curr_id += 1

        adj_lists_with_ids = [[] for i in range(len(adj_lists.keys()))]
        for vertex in vertex_ids:
            for end in adj_lists[vertex]:
                #sys.stderr.write("Adding {} ({}) to {} ({})\n".format(vertex_ids[end], end,
                #            vertex_ids[vertex], vertex))
                adj_lists_with_ids[vertex_ids[vertex]].append(vertex_ids[end])

        for i in range(len(adj_lists_with_ids)):
            for end in sorted(adj_lists_with_ids[i]):
                sys.stdout.write("{}:1 ".format(end))
            sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    main()

