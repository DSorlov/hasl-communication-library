import setuptools

with open("README.md") as fp:
    long_description = fp.read()

version = {}
with open("hasl/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="hasl",
    version=version['__version__'],
    author="Daniel Sorlov",
    author_email="daniel@sorlov.com",
    description="SL Communications Module for HomeAssistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsorlov/hasl",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
)
