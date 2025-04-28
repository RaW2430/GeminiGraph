# GeminiGraph
# 1.环境配置
* 系统: ubuntu24
* IDE: VS Code
* 依赖项：MPI, NUMA
参考命令：sudo apt-get install -y libopenmpi-dev openmpi-bin libnuma-dev
* 测试：进入根目录输入 ./toolkits/cc ./graph/graph.binedgelist 6 
![](https://notes.sjtu.edu.cn/uploads/upload_039dc096f6558ed9084c8100b9dc89db.png)
出现如上结果说明环境配置成功

# 2.操作说明
## 2.1 数据获取
https://law.di.unimi.it/datasets.php
## 2.2 数据预处理
* 运行 webgraph2txt.py 将 .graph 转换为 .txt
* 运行 reindexTxtGraph.py 将 .txt 中的编号标号映射为从 0 开始的连续自然数
* 运行 txt2bin.py 将新的 .txt 转换为可用的 .binedgelist 格式
## 2.3 执行 
* 在终端执行 ./toolkits/cc ./graph/cnr-2000.binedgelist 269338
![](https://notes.sjtu.edu.cn/uploads/upload_00fcc84eb66dd32d3326129d65d8d332.png)

* 命令解释：求 cnr-2000 的连通分量总数；269338代表总结点数（节点从0开始编号，最大编号为269337）

# 3.存在的问题
1. 单机不支持NUMA，对源代码中的 graph.hpp 做了如下修改
![](https://notes.sjtu.edu.cn/uploads/upload_b7afe6a5941accd1a6bcbf75d449edcc.png)
2. 会无限循环输出如下内容
![](https://notes.sjtu.edu.cn/uploads/upload_a260a909a87be0e869a4a092f9e18e61.png)
3. 其他报错 ./toolkits/pagerank ./graph/cnr-2000.binedgelist 269338 10
![](https://notes.sjtu.edu.cn/uploads/upload_aaf6a3f037ca91d5f99bf3970c42c8d7.png)
*解决方法：删除openmpi, 安装mpich
*sudo apt-get remove  libopenmpi-dev openmpi-bin
*sudo apt-get install  libmpich-dev openmpi-bin
