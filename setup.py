import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kashmiri",
    packages=setuptools.find_packages(),
    version="0.0.1",
    author="Izan Majeed",
    author_email='izanmajeed03@gmail.com',
    url='https://github.com/izan-majeed/Kaeshir-Database',
    description="Find the Kashmiri meaning of given English word.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license_files=('LICENSE'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
