from setuptools import setup, find_packages

setup(
    name="file_counter",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "file_counter = file_counter.main:main",
        ],
    },
)