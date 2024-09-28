# Model Updater

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

## Overview

**Model Updater** is a Python package designed to simplify the process of updating machine learning models from remote sources. Originally developed for **HaSpDe** (Hate Speech Detection) models, it can be easily adapted for any machine learning models hosted online.

The package ensures that your system is always using the latest version of a model by automatically checking for updates and downloading the newest version when available. With the newly added **force option**, users can now force an update regardless of the version check, providing additional control over the update process.

## Features

- Automatically fetches and compares model versions between local and remote sources.
- Downloads model updates and related files (e.g., vectorizers) when a newer version is detected.
- **Force updates**: Allows users to skip the version comparison and force a model update.
- Simple API for integration into existing machine learning pipelines.

## Installation

To install the package, use `pip`:

```bash
pip install git+https://github.com/HateSpeechDetection/model-updater
```

## Usage

Here’s an example of how to use the `ModelUpdater` package:

```python
from model_updater import ModelUpdater

# Create an instance of the ModelUpdater class
updater = ModelUpdater()

# Check for updates and download the latest model if available
updater.update_model()
```

### Forcing an Update

If you want to force a model update regardless of the local version, use the `force=True` argument:

```python
# Force the update even if the local version is up to date
updater.update_model(force=True)
```

This will bypass the version check and download the latest files.

### Customizing File Locations

You can specify custom paths for the model, version file, and vectorizer:

```python
updater = ModelUpdater(
    model_file="path/to/custom_model.joblib",
    version_file="path/to/custom_version.txt",
    vectorizer_file="path/to/custom_vectorizer.joblib",
)
```

This is useful if you want to store models in specific directories or if you have different filenames.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request on [GitHub](https://github.com/HateSpeechDetection/model-updater).

### Development Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/HateSpeechDetection/model-updater
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Pull Requests

When contributing, please ensure your changes are well-documented, and include a meaningful pull request title and description. Additionally, please test the code locally to verify its behavior.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

Developed by [Verso Vuorenmaa](https://github.com/verso). For inquiries or support, feel free to reach out via email at verso@luova.club.

---

### Badges and Credits

- **MIT License**: Licensed under [MIT](https://opensource.org/licenses/MIT).
- **Python 3.6+**: Supports Python versions 3.6 and above.

---

## Support

If you encounter any issues or have questions, feel free to contact me at `verso@luova.club`.
