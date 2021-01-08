
import setuptools
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (BASE_DIR / 'README.md').read_text(encoding='utf-8')


setuptools.setup(
    name="py3collections",
    version="0.1.2",

    author="Endalkachew Biruk",
    author_email="eb808826@gmail.com",

    description="Collection of python tools for different scenarios.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/endalk200/py_tools",

    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src", exclude=['docs', 'tests*']),

    install_requires=[],

    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'jpeg=pycollections.scripts:convert_to_jpeg',
        ],
    },

    scripts = [
        "./scripts/converter",
        "./scripts/filefind"
    ],

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",

        'Intended Audience :: Developers',
        "Intended Audience :: Education",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Topic :: Utilities",
    ],
    python_requires='>=3.5',
)