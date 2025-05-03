import networkx as nx

def txt_to_graphml(input_file, output_file, directed=False):
    # 创建图对象：有向图或无向图
    G = nx.DiGraph() if directed else nx.Graph()

    with open(input_file, 'r') as f:
        for line in f:
            u, v = line.strip().split()
            G.add_edge(u, v)

    nx.write_graphml(G, output_file)
    print(f"已保存为 {output_file}")

if __name__ == '__main__':
    # txtGraph = '../graph.txt'
    # mlGraph = '../graph.graphml'
    txtGraph = '../cnr-2000.txt'
    mlGraph = '../cnr-2000.graphml'
    txt_to_graphml(txtGraph, mlGraph, directed=False)
