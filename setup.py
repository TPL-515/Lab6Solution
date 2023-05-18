from setuptools import find_packages, setup

setup(
    name="lab6",
    packages=find_packages(exclude=["lab6_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "scikit-learn"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
