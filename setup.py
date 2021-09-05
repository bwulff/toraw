from setuptools import setup, find_packages

def load_requirements():
    try:
        with open("./requirements.txt") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("WARNING: requirements.txt not found")
        return []

setup(
    name="toraw",
    version="0.1.0",
    description="",
    author="Ben Wulff",
    url="https://github.com/bwulff/toraw",
    packages=["toraw"],
    package_dir={"toraw": "src/toraw"},
    include_package_data=True,
    install_requires=load_requirements(),
    entry_points="""
        [console_scripts]
        toraw=toraw:cli
    """,
)