def read_graph(f):
    graph = {}
    while True:
        line1 = f.readline()
        line2 = f.readline()
        if not line1:
            break
        lst = {}
        if line2.strip() != '':
            splt_line2 = line2.strip().split(',')
            for i in range(0, len(splt_line2), 2):
                lst[float(splt_line2[i].strip("()"))] = float(splt_line2[i+1].strip("()"))
        graph[float(line1.strip())] = lst
    return graph
