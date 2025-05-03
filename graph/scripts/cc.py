from collections import defaultdict

def load_directed_graph(filename):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    nodes = set()

    with open(filename, 'r') as f:
        for line in f:
            if not line.strip():
                continue  # 跳过空行
            u, v = map(int, line.strip().split())
            graph[u].append(v)
            reverse_graph[v].append(u)
            nodes.update([u, v])

    # 确保所有节点都加入图中（即使没有出边或入边）
    for node in nodes:
        graph[node]
        reverse_graph[node]

    return graph, reverse_graph

def dfs_iterative(graph, start_node, visited, stack=None, component=None):
    # 使用显式栈模拟递归
    stack_ = [start_node]
    visited.add(start_node)
    if component is not None:
        component.append(start_node)

    while stack_:
        node = stack_.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack_.append(neighbor)
                if component is not None:
                    component.append(neighbor)
        if stack is not None:
            stack.append(node)

def kosaraju_scc(graph, reverse_graph):
    visited = set()
    stack = []

    # 第一遍 DFS，记录完成时间
    for node in list(graph):
        if node not in visited:
            dfs_iterative(graph, node, visited, stack)

    visited.clear()
    components = []

    # 第二遍 DFS，按 stack 顺序在反向图中找强连通分量
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_iterative(reverse_graph, node, visited, component=component)
            components.append(component)

    return components

if __name__ == '__main__':
    filename = '../cnr-2000.txt'  # 替换为你的文件名
    graph, reverse_graph = load_directed_graph(filename)
    components = kosaraju_scc(graph, reverse_graph)

    print(f"共 {len(components)} 个强连通分量：")
    max_component = max(components, key=len)
    print(f"最大强连通分量的节点数是：{len(max_component)}")
