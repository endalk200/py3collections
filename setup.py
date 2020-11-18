
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py3collections",
    version="0.0.3",
    author="Endalkachew Biruk",
    author_email="eb808826@gmail.com",
    description="Collection of python tools for different scenarios.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/endalk200/py_utils",
    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)