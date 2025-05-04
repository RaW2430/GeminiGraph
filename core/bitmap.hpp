/*
Copyright (c) 2015-2016 Xiaowei Zhu, Tsinghua University

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

#ifndef BITMAP_HPP
#define BITMAP_HPP

#define WORD_OFFSET(i) ((i) >> 6) // i / 64
#define BIT_OFFSET(i) ((i) & 0x3f)

class Bitmap {
public:
  size_t size;  // 位图总比特数
  unsigned long * data; // 用于存储比特的数组, 每个 data[i] 可存储 64 位
  Bitmap() : size(0), data(NULL) { }
  Bitmap(size_t size) : size(size) {
    data = new unsigned long [WORD_OFFSET(size)+1]; // 设置data数组长度: data.size() = size / 64 + 1
    clear();
  }
  ~Bitmap() {
    delete [] data;
  }
  // 位图置 0
  void clear() {
    size_t bm_size = WORD_OFFSET(size); // 获取 data 数组长度最大索引
    #pragma omp parallel for  // openMPI 并行化清空 data
    for (size_t i=0;i<=bm_size;i++) {
      data[i] = 0;
    }
  }
  // 位图置 1
  void fill() {
    size_t bm_size = WORD_OFFSET(size); // 获取 data 数组长度最大索引
    #pragma omp parallel for  // openMPI 并行化 data 置 1
    for (size_t i=0;i<bm_size;i++) {
      data[i] = 0xffffffffffffffff;
    }
    // 最后一个 data 单位可能不满 64 位，需要特殊处理
    data[bm_size] = 0;
    for (size_t i=(bm_size<<6);i<size;i++) {  // bm_size<<6 最后一个元素的起始位
      data[bm_size] |= 1ul << BIT_OFFSET(i);  // 将对应位置 1
    }
  }
  // 返回位图第 i 个比特的值
  unsigned long get_bit(size_t i) {
    return data[WORD_OFFSET(i)] & (1ul<<BIT_OFFSET(i)); // data[i / 64] & (1 << 64), return 1 or 0
  }
  // 将第 i 个比特设置为 1
  void set_bit(size_t i) {
    __sync_fetch_and_or(data+WORD_OFFSET(i), 1ul<<BIT_OFFSET(i)); // GCC 原子操作将第 i 位置 1: data[i / 64 + offset] |= 1 << 64
  }
};

typedef Bitmap VertexSubset;

#endif
