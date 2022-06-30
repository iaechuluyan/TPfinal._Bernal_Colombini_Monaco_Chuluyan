
from setuptools import setup, find_packages

setup(
    name='functions',
    version='1.0.0', #???
    license='MIT',
    packages=find_packages(
        where='.', #hace q vuelvas
        include=['functions*'], #le dice q carpeta abrir
    ),
)