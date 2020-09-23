import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pack",
    version="0.0.1",
    author="GLMontanari",
    author_email="fakeemail@gmail.com",
    description="working minimal python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        'PyQt5',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            # "command = pack.module.submodule:func",
        ],
        "gui_scripts": [
            "command = pack.app:main",
        ]
    }
)
