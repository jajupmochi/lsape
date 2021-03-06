import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()

setuptools.setup(
    name="lsape",
    version="0.1b1",
    author="Linlin Jia",
    author_email="linlin.jia@insa-rouen.fr",
    description="Python tools for solving the Linear Sum Assignment Problem with Edition (LSAPE) and the Linear Sum Assignment Problem (LSAP)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jajupmochi/lsape",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
)
