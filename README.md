# GeminiGraph
# 1.环境配置
* 系统: ubuntu24
* IDE: VS Code
* 依赖项：MPI, NUMA
参考命令：sudo apt-get install -y libopenmpi-dev openmpi-bin libnuma-dev


# 2.操作说明
## 2.1 数据获取
https://law.di.unimi.it/datasets.php
## 2.2 数据预处理
* 使用 java 的 WebGraph 类将 .graph 和其对应的 .properties 转化为 .txt
* 将 .txt 转换为二进制格式（节点的二进制直接相连）
## 2.3 执行 
* 在终端执行 ./toolkits/cc ./graph/enwiki-2024.binedgelist 6790971 
* 命令解释：求 enwiki-2024 的连通分量总数；6790971代表总结点数（节点从0开始编号，最大编号为6790970）

# 3.存在的问题
* 单机跑bc, bfs, cc, sssp存在段错误问题
