import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess
import networkx as nx
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import font_manager

# 设置根目录
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(project_root)

# 设置中文字体
font_paths = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
zh_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc')
plt.rcParams['font.family'] = zh_font.get_name()

# 加载图文件
def load_graph_from_txt(filepath):
    G = nx.DiGraph()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                src, dst = parts[0], parts[1]
                G.add_edge(src, dst)
    return G

# 绘图函数
def draw_graph(G, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6, 6))
    pos = nx.kamada_kawai_layout(G)
    nx.draw(
        G, pos, ax=ax,
        with_labels=True,
        node_size=150,
        font_size=6,
        width=0.5,
        font_family=zh_font.get_name(),
        node_color='lightblue',
        arrows=True
    )
    ax.set_axis_off()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# 执行命令并输出
def run_command(command, output_box):
    output_box.insert(tk.END, f"$ {command}\n")
    output_box.see(tk.END)
    output_box.update()
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output_box.insert(tk.END, result.stdout + '\n')
        if result.stderr:
            output_box.insert(tk.END, "[stderr]:\n" + result.stderr + '\n')
    except Exception as e:
        output_box.insert(tk.END, f"[error] {e}\n")
    output_box.see(tk.END)

# 获取用户输入的节点编号
def get_node_input():
    node_input = node_entry.get()
    if not node_input.isdigit():
        output_box.insert(tk.END, "节点编号应为整数。\n")
        return None
    node_input = int(node_input)
    if node_input < 0 or node_input >= graph_data["node_count"]:
        output_box.insert(tk.END, f"节点编号应在 0 到 {graph_data['node_count'] - 1} 之间。\n")
        return None
    return node_input

# 主界面
def main():
    global output_box, node_entry, graph_data
    root = tk.Tk()
    root.title("有向图可视化 + 命令执行器")

    graph_data = {"G": None, "node_count": 0, "graph_binedgelist_path": ""}

    # 图区域
    graph_frame = tk.Frame(root)
    graph_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # 控制区域
    control_frame = tk.Frame(root)
    control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # 输出框
    output_box = scrolledtext.ScrolledText(control_frame, width=60, height=25, font=("Courier", 10))
    output_box.pack(pady=10)

    # 节点编号输入框
    node_label = tk.Label(control_frame, text="节点编号：")
    node_label.pack()
    node_entry = tk.Entry(control_frame)
    node_entry.pack(pady=2)

    # 迭代次数输入
    iter_label = tk.Label(control_frame, text="迭代次数：")
    iter_label.pack()
    iter_entry = tk.Entry(control_frame)
    iter_entry.insert(0, "10")
    iter_entry.pack(pady=2)

    # 加载图文件
    def load_file():
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            G = load_graph_from_txt(path)
            graph_data["G"] = G
            graph_data["node_count"] = len(G.nodes)
            graph_data["graph_binedgelist_path"] = os.path.splitext(path)[0] + '.binedgelist'
            draw_graph(G, graph_frame)

    tk.Button(control_frame, text="加载图文件 (.txt)", command=load_file, width=25).pack(pady=5)

    # 运行命令
    def run_custom_command(command, output_box):
        if graph_data["G"] is None:
            output_box.insert(tk.END, "请先加载图文件。\n")
            return

        node_count = graph_data["node_count"]

        # 获取节点编号（仅对需要节点编号的命令）
        if "[root]" in command:
            node_input = get_node_input()
            if node_input is None:
                return
        else:
            node_input = ""  # 对于不需要节点编号的命令

        # 获取迭代次数
        iterations = iter_entry.get()
        if "[iterations]" in command and not iterations.isdigit():
            output_box.insert(tk.END, "迭代次数应为整数。\n")
            return

        # 获取图文件路径
        graph_binedgelist_path = graph_data.get("graph_binedgelist_path", "")
        if not graph_binedgelist_path:
            output_box.insert(tk.END, "图文件路径无效，请重新加载图文件。\n")
            return

        # 替换命令中的占位符
        full_command = command.replace("[graphPath]", graph_binedgelist_path)
        full_command = full_command.replace("[vertices]", str(node_count))
        full_command = full_command.replace("[iterations]", str(iterations))
        full_command = full_command.replace("[root]", str(node_input))

        # 执行命令
        run_command(full_command, output_box)

    # 命令列表
    commands = [
        ("pagerank", "./toolkits/pagerank [graphPath] [vertices] [iterations]"),
        ("cc", "./toolkits/cc [graphPath] [vertices]"),
        ("bfs", "./toolkits/bfs [graphPath] [vertices] [root]"),
        ("sssp", "./toolkits/sssp [graphPath] [vertices] [root]"),
        ("bc", "./toolkits/bc [graphPath] [vertices] [root]"),
    ]

    # 为每个命令生成按钮，按需求替换路径和命令格式
    for label, cmd in commands:
        tk.Button(control_frame, text=label, command=lambda c=cmd: run_custom_command(c, output_box), width=25).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
