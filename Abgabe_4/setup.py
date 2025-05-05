from setuptools import setup, Extension
import pybind11
import os

EIGEN_DIR = r"C:\Users\ellen\OneDrive\Documents\Studium\Semester5\2D CV\Übung\2D-Computer-Vision\Abgabe_4\eigen-3.4.0"

module = Extension(
    'sobel_demo',
    sources=['sobel_demo.cpp'],
    include_dirs=[
        pybind11.get_include(),  # Pybind11 headers
        EIGEN_DIR,              # Eigen headers
    ],
    extra_compile_args=['/std:c++11'],  # MSVC flag
    language='c++'
)

setup(
    name='sobel_demo',
    version='1.0',
    description='Sobel filter module',
    ext_modules=[module]
)