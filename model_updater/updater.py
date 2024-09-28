import os
import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ModelUpdater:
    def __init__(
        self,
        model_file="moderation_model.joblib",
        version_file="model_version.txt",
        vectorizer_file="tfidf_vectorizer.joblib",
        model_url="https://raw.githubusercontent.com/botsarefuture/HaSpDe/main/moderation_model.joblib",
        version_url="https://raw.githubusercontent.com/botsarefuture/HaSpDe/main/model_version.txt",
        vectorizer_url="https://raw.githubusercontent.com/botsarefuture/HaSpDe/main/tfidf_vectorizer.joblib",
    ):
        """
        Initialize the ModelUpdater.

        Args:
            model_file (str): Filename for the model file (saved to the current working directory).
            version_file (str): Filename for the version file (saved to the current working directory).
            vectorizer_file (str): Filename for the vectorizer file (saved to the current working directory).
            model_url (str): URL to download the model file.
            version_url (str): URL to download the version file.
            vectorizer_url (str): URL to download the vectorizer file.
        """
        # Get the current working directory
        self.save_dir = os.getcwd()

        # Set file paths to the current working directory
        self.model_file = os.path.join(self.save_dir, model_file)
        self.version_file = os.path.join(self.save_dir, version_file)
        self.vectorizer_file = os.path.join(self.save_dir, vectorizer_file)

        # URLs for downloading the files
        self.model_url = model_url
        self.version_url = version_url
        self.vectorizer_url = vectorizer_url

    def download_file(self, url, save_path):
        """Download a file from the specified URL and save it to the given path."""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            logger.info(f"Successfully downloaded file from {url} to {save_path}.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error downloading from {url}: {e}")
            raise
        except OSError as e:
            logger.error(f"Error saving to {save_path}: {e}")
            raise

    def get_local_version(self):
        """Retrieve the local model version from a file."""
        if os.path.exists(self.version_file):
            try:
                with open(self.version_file, "r") as file:
                    return file.read().strip()
            except OSError as e:
                logger.error(f"Error reading local version file: {e}")
                raise
        return None

    def get_github_version(self):
        """Fetch the model version from the GitHub repository."""
        try:
            response = requests.get(self.version_url)
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching version from GitHub: {e}")
            return None

    def is_newer_version_available(self, local_version, github_version):
        """Check if a newer version is available compared to the local version."""
        if local_version is None:
            return True  # Assume update is needed if no local version exists
        return github_version > local_version

    def update_model(self, force=False):
        """
        Check for updates and download the model if a newer version is available, or if force=True.
        
        Args:
            force (bool): If True, force the update even if the local version is up to date.
        """
        local_version = self.get_local_version()
        github_version = self.get_github_version()

        if github_version:
            if force or self.is_newer_version_available(local_version, github_version):
                logger.info(
                    f"Updating model{' (forced)' if force else ''}. "
                    f"New version: {github_version}"
                )
                self.download_file(self.model_url, self.model_file)
                self.download_file(self.version_url, self.version_file)
                self.download_file(self.vectorizer_url, self.vectorizer_file)

                logger.info(f"Model successfully updated to version {github_version}.")
            else:
                logger.info("Local model is up to date.")
        else:
            logger.error("Could not determine the latest model version. Update aborted.")
