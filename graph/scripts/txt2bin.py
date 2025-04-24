import struct

# input_file = "../cnr-2000-reindex.txt"
# output_file = "../cnr-2000.binedgelist"

input_file = "../twitter-2010.graph"  # 替换为你的 .graph 文件路径
output_file = "../twitter-2010.txt"       # 输出的 .txt 文件路径

with open(input_file, "r") as fin, open(output_file, "wb") as fout:
    for line in fin:
        if line.strip():  # 跳过空行
            parts = line.strip().split()
            if len(parts) == 2:
                u, v = map(int, parts)
                fout.write(struct.pack("<II", u, v))
