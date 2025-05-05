from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'sobel_demo',
        ['sobel_demo.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name='sobel_demo',
    ext_modules=ext_modules,
)