import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KSPython", # Replace with your own username
    version="0.1.0",
    author="Luiz Frederico Villalobos",
    author_email="luizf.villalobos@gmail.com",
    description="A package made for plan and develop rockets in KSP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)