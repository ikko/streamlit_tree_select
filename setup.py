import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-tree-select-themed",
    version="0.0.18",
    author="ikko",
    author_email="",
    description="A simple and elegant checkbox tree for Streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ikko/streamlit_tree_select_themed",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
