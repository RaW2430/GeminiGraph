import struct

input_file = "../cnr-2000.graph"  # 替换为你的 .graph 文件路径
output_file = "../cnr-2000.txt"       # 输出的 .txt 文件路径

with open(input_file, "rb") as fin, open(output_file, "w") as fout:
    while True:
        # 每次读取两个 uint32_t（4 字节）表示一个边：src 和 dst
        edge_data = fin.read(8)
        if len(edge_data) < 8:
            break  # 文件读取完毕

        # 解包二进制数据为两个 32 位整数 (小端字节序)
        src, dst = struct.unpack("<II", edge_data)

        # 写入文本文件：src \t dst
        fout.write(f"{src}\t{dst}\n")

print(f"转换完成，结果保存在 {output_file}")
