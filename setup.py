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
    description="Communications Module for HomeAssistant SL Sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsorlov/hasl",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
