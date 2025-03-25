from setuptools import setup, find_packages

setup(
    name="neurofluid",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21",
        "scipy>=1.7",
        "matplotlib>=3.5"
    ],
    entry_points={
        'console_scripts': [
            'neurofluid=neurofluid.cli:main',
        ],
    },
)
