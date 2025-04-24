import struct

# input_file = "../cnr-2000-reindex.txt"
# output_file = "../cnr-2000.binedgelist"
input_file = "../graph1.txt"
output_file = "../graph1.binedgelist"

with open(input_file, "r") as fin, open(output_file, "wb") as fout:
    for line in fin:
        if line.strip():  # 跳过空行
            parts = line.strip().split()
            if len(parts) == 2:
                u, v = map(int, parts)
                fout.write(struct.pack("<II", u, v))
