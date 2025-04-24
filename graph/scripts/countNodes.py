import struct

filename = "../cnr-2000-reindex.txt"
max_node = 0

with open(filename, "rb") as f:
    while True:
        data = f.read(8)
        if not data or len(data) < 8:
            break
        src, dst = struct.unpack("II", data)
        max_node = max(max_node, src, dst)

print("最大节点 ID:", max_node)
print("建议 vertex_count 设置为:", max_node + 1)
