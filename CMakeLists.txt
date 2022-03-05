cmake_minimum_required(VERSION 3.20)
project(BugPosition)

set(CMAKE_CXX_STANDARD 17)

find_package(SofaFramework REQUIRED)
add_library(BugPosition SHARED library.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC SofaCore)