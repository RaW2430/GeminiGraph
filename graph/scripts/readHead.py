import struct

with open("../cnr-2000.binedgelist", "rb") as f:
    for i in range(10):  # 读取前10条边
        data = f.read(8)  # 每条边由两个 uint32_t 组成 (4字节 * 2 = 8 字节)
        if len(data) < 8:
            break
        src, dst = struct.unpack("<II", data)
        print(f"{src} -> {dst}")
