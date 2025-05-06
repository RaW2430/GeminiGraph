from collections import defaultdict, deque

def load_graph_as_undirected(filename):
    graph = defaultdict(set)
    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            graph[u].add(v)
            graph[v].add(u)  # 反向边加上，变为无向图处理
    return graph

def bfs(graph, start, visited):
    queue = deque([start])
    component = []
    visited.add(start)
    while queue:
        node = queue.popleft()
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return component

def find_weakly_connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = bfs(graph, node, visited)
            components.append(component)
    return components

if __name__ == '__main__':
    filename = '../enwiki-2024.txt'  # 请将此文件路径替换为你的实际路径
    graph = load_graph_as_undirected(filename)
    components = find_weakly_connected_components(graph)

    print(f"共 {len(components)} 个弱连通分量：")
    # for comp in components:
    #     print(sorted(comp))

    # 输出最大弱连通分量大小
    max_size = max(len(comp) for comp in components)
    print(f"最大连通分量的节点数：{max_size}")
