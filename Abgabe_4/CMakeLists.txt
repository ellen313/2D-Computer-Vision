cmake_minimum_required(VERSION 3.14)
project(sobel_demo)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Pybind11 lokal einbinden
add_subdirectory(external/pybind11)

# Eigen-Header einbinden (Pfad zu Eigen-Headern anpassen)
include_directories(external/eigen)

# Modul bauen
pybind11_add_module(sobel_demo sobel_demo.cpp)
