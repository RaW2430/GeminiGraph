# 文件名
input_file = "../cnr-2000.txt"
output_file = "../cnr-2000-reindex.txt"

# 读取原始边数据
edges = []
nodes = set()

# 读取文件并收集所有的节点 ID
with open(input_file, "r") as f:
    for line in f:
        src, dst = map(int, line.strip().split())
        edges.append((src, dst))
        nodes.add(src)
        nodes.add(dst)

# 创建节点映射：节点 ID -> 连续自然数
sorted_nodes = sorted(nodes)  # 将节点按从小到大的顺序排列
node_mapping = {node: idx for idx, node in enumerate(sorted_nodes)}

# 获取最大节点编号（即最大连续自然数）
max_node = len(node_mapping) - 1

# 将边的节点替换为新的连续 ID，并写入到输出文件
with open(output_file, "w") as f:
    for src, dst in edges:
        # 使用映射关系替换源节点和目标节点
        mapped_src = node_mapping[src]
        mapped_dst = node_mapping[dst]
        f.write(f"{mapped_src} {mapped_dst}\n")

print(f"节点映射完成，结果保存到 {output_file}")
print(f"最大节点编号：{max_node}")
