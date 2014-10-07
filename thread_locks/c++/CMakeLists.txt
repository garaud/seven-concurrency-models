CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(Threads_Locks)

set(CMAKE_CXX_FLAGS "${CMAXE_CXX_FLAGS} -std=c++11 -Wall -pedantic -Wextra")

find_package(Threads)

add_executable(hello_thread hello_thread.cpp)
target_link_libraries(hello_thread ${CMAKE_THREAD_LIBS_INIT})
