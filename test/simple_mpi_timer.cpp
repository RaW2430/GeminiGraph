#include <iostream>
#include <mpi.h>
#include <unistd.h>  // for sleep()
#include <chrono>    // for timing

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    // 简单同步，确保所有进程同时开始
    MPI_Barrier(MPI_COMM_WORLD);

    for (int i = 0; i < 5; ++i) {  // 每个进程打印5次
        if (i % size == rank) {     // 按进程号轮流打印
            auto now = std::chrono::system_clock::now();
            auto now_time = std::chrono::system_clock::to_time_t(now);
            
            std::cout << "进程 " << rank << "/" << size 
                      << " 在主机 " << processor_name 
                      << " 时间: " << std::ctime(&now_time);
        }
        sleep(1);  // 等待1秒
        MPI_Barrier(MPI_COMM_WORLD);  // 同步所有进程
    }

    MPI_Finalize();
    return 0;
}