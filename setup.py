from setuptools import setup, find_packages

setup(
    name="streamlit-text-editor",
    version="1.0.0",
    author="Yogesh Sankaranarayanan Jayanthi",
    author_email="",
    description="A lightweight line-based text editor built with Streamlit",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sjyogesh23/EPITA-TextEditor-Python",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)