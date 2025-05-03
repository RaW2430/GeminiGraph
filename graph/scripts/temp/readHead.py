import struct

with open("../graph1.binedgelist", "rb") as f:
    for i in range(120):  # 读取前10条边
        data = f.read(8)  # 每条边由两个 uint32_t 组成 (4字节 * 2 = 8 字节)
        if data == b'\0':
            print("Found NULL byte '\\0' in data. Ending read.")
            break  # 遇到 `\0` 字符，跳出循环
        if len(data) < 8:
            break
        src, dst = struct.unpack("<II", data)
        print(f"{src} -> {dst}")
