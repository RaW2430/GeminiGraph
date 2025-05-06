# webgraph
Download and use
关于使用webgraph数据集的方法：

关于github使用方法:

1.下载所有文件。其中uk-2007-05@100000.graph和uk-2007-05@100000.properties是从webgraph网站上下载来的数据集，您下载后可以用这两个数据集验证程序是否能正常读取graph文件

2.新建一个文件名为lib，把除了uk-2007-05@100000开头的两个文件其他文件都放入lib。
  能成功运行的目录格式为：
  
    -uk-2007-05@100000.graph
    
    -uk-2007-05@100000.properties
    
    -lib
    
      -checker-qual-3.5.0.jar
      
      -.......
      
 3.在terminal中找到存储文件的正确目录，运行代码：
 java -cp "lib/*" it.unimi.dsi.webgraph.ArcListASCIIGraph uk-2007-05@100000 uk200705.txt
 java -cp "lib/*" it.unimi.dsi.webgraph.ArcListASCIIGraph twitter-2010 twitter-2010.txt
 java -cp "lib/*" it.unimi.dsi.webgraph.ArcListASCIIGraph enwiki-2024 enwiki-2024.txt
 将txt转换为二进制格式:
 ./convert graph.txt graph.binedgelist 
 ./convert twitter-2010.txt twitter-2010.binedgelist 
 ./convert enwiki-2024.txt enwiki-2024.binedgelist 
  图文件会被转化成txt格式供后续使用，官方网站以及代码来源：https://webgraph.di.unimi.it/
  如果有自己的图文件，代替代码中的uk-2007-05@100000即可。
  
  关于google drive：
  下载压缩包并解压文件，已经是正确的目录格式，直接执行上文提到的第三步即可。
  https://drive.google.com/file/d/1VMq5KvTdM44pObsbRZzkcCvjCcjgr09W/view?usp=sharing

  
  有问题请联系taowe@umich.edu
