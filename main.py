from helpers import CFG
from helpers import Graph

def check_reachability(cfg, graph, start_vertex, end_vertex):
    queue = [[start_vertex, '']]
    valid_strings = []

    while queue:
        node, string = queue.pop(0)
        
        if node == end_vertex:
            valid_strings.append(string)
            continue

        for edge in graph.get_edges().get(node, []):
            next_node, label = edge
            queue.append([next_node, string + label])

    for string in valid_strings:
        if cfg.cykParse(string):
            return True
    return False

def read_input(file_path):
    with open(file_path, 'r') as file:
        num_inputs = int(file.readline().strip())
        inputs = []
        for _ in range(num_inputs):
            cfg_productions = file.readline().strip()
            graph_data = file.readline().strip()
            start_vertex = file.readline().strip()
            end_vertex = file.readline().strip()
            inputs.append((cfg_productions, graph_data, start_vertex, end_vertex))
        return inputs

def write_output(file_path, results):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(result + '\n')

def main(input_file, output_file):
    inputs = read_input(input_file)
    results = []
    for cfg_productions, graph_data, start_vertex, end_vertex in inputs:
        cfg = CFG(cfg_productions)
        # print(cfg.parse_productions(cfg_productions))
        graph = Graph()
        edge_data = graph_data.split(' ')
        for edge in edge_data:
            src = edge[0]
            dst = edge[1]
            label = edge[3]
            graph.add_edge(src, dst, label)

        reachable = check_reachability(cfg, graph, start_vertex, end_vertex)
        
        # print(reachable)
        results.append('Yes' if reachable else 'No')
    print(results)

    write_output(output_file, results)

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    main(input_file, output_file)

