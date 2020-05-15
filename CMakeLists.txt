cmake_minimum_required(VERSION 2.8.3)
project(ecn_navigation)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE Release)

find_package(catkin REQUIRED COMPONENTS
cmake_modules
roscpp)

catkin_package()
