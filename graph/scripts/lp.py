# label propagation

from collections import defaultdict

def load_graph(filename):
    graph = defaultdict(set)
    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            # 弱连通：忽略方向
            graph[u].add(v)
            graph[v].add(u)
    return graph

def label_propagation(graph):
    labels = {node: node for node in graph}
    iteration = 0

    while True:
        changed = 0
        new_labels = labels.copy()
        for node in graph:
            min_label = min([labels[neighbor] for neighbor in graph[node]] + [labels[node]])
            if min_label < labels[node]:
                new_labels[node] = min_label
                changed += 1

        labels = new_labels
        print(f"active({iteration}) = {changed}")
        iteration += 1
        if changed == 0:
            break

    # 聚合连通分量
    components = defaultdict(list)
    for node, label in labels.items():
        components[label].append(node)

    return list(components.values())

if __name__ == '__main__':
    filename = '../enwiki-2024.txt'  # 每行格式：u v （有向边）
    graph = load_graph(filename)
    components = label_propagation(graph)

    print(f"\n共 {len(components)} 个弱连通分量：")
    # for comp in components:
    #     print(sorted(comp))
