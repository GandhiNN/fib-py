from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fib_py",
    version="0.0.1",
    author="Ngakan Gandhi",
    author_email="n.nyoman.gandhi@gmail.com",
    description="Calculates a Fibonacci number",
    long_description_content_type="text/markdown",
    url="https://github.com/GandhiNN/fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    entry_points={
        'console_scripts': [
            'fib-number = fib_py.cmd.fib_numb:fib_numb',
        ],
    },
    python_requires='>=3',
    tests_require=['pytest'],
)