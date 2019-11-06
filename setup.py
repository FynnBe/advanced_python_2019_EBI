from pathlib import Path

from setuptools import find_packages, setup


# Get the long description from the README file
with (Path(__file__).parent / "README.md").open() as f:
    long_description = f.read()

setup(
    name="ap2019ebi",
    version="0.1.0",
    description="toy package for advanced python course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fynnbe/advanced_python_2019_EBI",
    author="Fynn Beuttenmueller",
    author_email="fynnbe@gmail.com",
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["tests"]),  # Required
    install_requires=["jupyter", "pandas", "plotly", "psutil", "sphinx", "rise"],
)
