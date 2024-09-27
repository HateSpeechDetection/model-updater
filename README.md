# Model Updater

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

## Overview

**Model Updater** is a Python package designed to simplify the process of updating machine learning models from remote sources. This package was developed for **HaSpDe** (Hate Speech Detection) models, but it can be used with any machine learning models hosted online.

The package automatically checks for new versions of models and downloads updates when available, ensuring that your system is always using the latest version.

## Features

- Automatically fetches and compares model versions between local and remote sources.
- Downloads model updates and related files (e.g., vectorizers) if a newer version is found.
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

This will automatically:
1. Compare the local model version with the version stored remotely.
2. Download the new model, version file, and vectorizer if there is a newer version.

## Customizing File Locations

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

Developed by [Verso Vuorenmaa](https://github.com/verso). Feel free to reach out via email at verso@luova.club.

---

### Badges and Credits

- **MIT License**: Licensed under [MIT](https://opensource.org/licenses/MIT).
- **Python 3.6+**: Supports Python versions 3.6 and above.

---

## Support

If you encounter any issues or have questions, feel free to contact me at `verso@luova.club`.