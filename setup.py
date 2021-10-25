import setuptools

with open("README.md") as file:
    long_description = file.read()

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setuptools.setup(
    name='remove-apt-repository',
    version='1.1',
    scripts=['remove-apt-repository'] ,
    author="Iliya Rezaee",
    author_email="iliyarezaee2017@gmail.com",
    description="a smal tool for remove apt repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IliyaRezaee/remove-apt-repository",
    packages=setuptools.find_packages(),
    install_requires = requirements,
    classifiers=[
     "Programming Language :: Python :: 3",
     "Operating System :: POSIX :: Linux",
     "Environment :: Console",
    ]
)
