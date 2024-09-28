from setuptools import setup, find_packages

# Read the README file for a long description on PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="model_updater",  # The name of your package on PyPI
    version="0.2.0",  # Updated semantic versioning to reflect the new force option feature
    description="A package for updating machine learning models from remote sources, with force update option.",
    long_description=long_description,  # Use the README as the long description
    long_description_content_type="text/markdown",  # Specify that long description is in Markdown
    author="Verso Vuorenmaa",
    author_email="verso@luova.club",
    url="https://github.com/HateSpeechDetection/model-updater",  # GitHub URL
    project_urls={  # Additional useful URLs for the project
        "Documentation": "https://github.com/HateSpeechDetection/model-updater/wiki",
        "Bug Tracker": "https://github.com/HateSpeechDetection/model-updater/issues",
        "Source Code": "https://github.com/HateSpeechDetection/model-updater",
    },
    packages=find_packages(),  # Automatically discover all packages
    install_requires=[
        "requests>=2.20.0",  # Ensure compatibility with requests library
    ],
    python_requires=">=3.6",  # Specify compatible Python versions
    classifiers=[  # Additional classifiers to better categorize the project
        "Development Status :: 4 - Beta",  # Project maturity
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="model updater machine learning automation force-update",  # Updated keywords
    license="MIT",  # License type
)
