import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdeffe",
    version="0.0.1",
    author="GLMontanari",
    author_email="fakeemail@gmail.com",
    description="A small gui for editing PDFs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/GLmontanari/pdEFFE",
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
            # "food = foo.A.daikin:dunc",
        ],
        "gui_scripts": [
            "pdeffe = pdeffe.app:main",
        ]
    }
)
