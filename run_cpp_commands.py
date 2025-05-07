import subprocess
import time

# 定义要执行的命令列表
commands = [
    "./toolkits/pagerank ./graph/enwiki-2024.binedgelist 6790971 50",
    "./toolkits/pagerank ./graph/graph.binedgelist 8 20",
    "./toolkits/pagerank ./graph/cnr-2000.binedgelist 325557 20"
]

for cmd in commands:
    print(f"\n=== Running: {cmd} ===")
    start_time = time.time()

    # 使用 shell=True 允许你传入整条命令作为字符串执行
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("---- STDOUT ----")
        print(result.stdout)
        print("---- STDERR ----")
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        print("---- STDOUT ----")
        print(e.stdout)
        print("---- STDERR ----")
        print(e.stderr)

    end_time = time.time()
    print(f"=== Finished in {end_time - start_time:.2f} seconds ===")
