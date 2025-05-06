import sys

DAMPING = 0.85

def load_graph(filename):
    graph = {}
    nodes = set()
    with open(filename, 'r') as f:
        for line in f:
            src, dst = map(int, line.strip().split())
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)
            nodes.add(src)
            nodes.add(dst)
    return graph, nodes

def initialize_ranks(nodes, graph):
    ranks = {}
    N = len(nodes)
    for node in nodes:
        out_deg = len(graph.get(node, []))
        ranks[node] = 1.0 / out_deg if out_deg > 0 else 0.0
    return ranks

def pagerank(filename, num_nodes, iterations):
    graph, nodes = load_graph(filename)
    curr = initialize_ranks(nodes, graph)
    next_rank = {node: 0.0 for node in nodes}
    N = len(nodes)

    for i in range(iterations):
        for node in nodes:
            for neighbor in graph.get(node, []):
                next_rank[neighbor] += curr[node]
        
        delta = 0.0
        for node in nodes:
            new_rank = (1 - DAMPING) + DAMPING * next_rank[node]
            delta += abs(new_rank - curr.get(node, 0.0))
            curr[node] = new_rank / len(graph.get(node, [])) if graph.get(node) else new_rank
            next_rank[node] = 0.0

        delta /= N
        print(f"delta({i}) = {delta:.6f}")

    # 输出最大 PageRank 节点
    max_node = max(curr, key=curr.get)
    print(f"max pr node: {max_node}, pr = {curr[max_node]}")
    print(f"pr sum = {sum(curr.values())}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python pagerank.py <file> <vertices> <iterations>")
        sys.exit(1)

    filename = sys.argv[1]
    num_nodes = int(sys.argv[2])  # 不强依赖，可用于校验
    iterations = int(sys.argv[3])

    pagerank(filename, num_nodes, iterations)
