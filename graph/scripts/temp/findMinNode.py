import struct

min_node = float('inf')
max_node = float('-inf')

with open("../cnr-2000.binedgelist", "rb") as f:
    while True:
        data = f.read(8)  # 每条边 = 2 个 uint32 = 8 字节
        if len(data) < 8:
            break
        src, dst = struct.unpack("<II", data)
        min_node = min(min_node, src, dst)
        max_node = max(max_node, src, dst)

print("最小节点 ID =", min_node)
print("最大节点 ID =", max_node)
