CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(Threads_Locks)

set(CMAKE_CXX_FLAGS "${CMAXE_CXX_FLAGS} -std=c++11 -Wall -pedantic -Wextra -fdiagnostics-color")
find_package(Threads)

# List of files to compile
set(_COMPILATION_UNITS hello_thread.cpp
                       wrong_counter.cpp)

# Loop on each compilation units.
foreach(ccfile ${_COMPILATION_UNITS})
  get_filename_component(basename ${ccfile} NAME_WE)
  add_executable(${basename} ${ccfile})
  target_link_libraries(${basename} ${CMAKE_THREAD_LIBS_INIT})
endforeach()
