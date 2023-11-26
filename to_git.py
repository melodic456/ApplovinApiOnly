import requests
import subprocess

class GitHubRepoManager:
    def __init__(self, token, repo_name, repo_description):
        self.token = token
        self.repo_name = repo_name
        self.repo_description = repo_description
        self.repo_url = f"https://github.com/{self.repo_name}.git"

    def create_repository(self):
        url = "https://api.github.com/user/repos"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        payload = {
            "name": self.repo_name,
            "description": self.repo_description
        }
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 201:
            print("Repository created successfully!")
        else:
            print(f"Failed to create repository. Status code: {response.status_code}")
            print(response.json())

    def commit_and_push(self, file_path, commit_message):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", file_path])
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "remote", "add", "origin", self.repo_url])
        subprocess.run("git branch -M main".split(" "))
        subprocess.run(["git", "push", "-u", "origin", "main"])

# Replace the following variables with your own values
token = "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"
repo_name = "applovinApi2"
repo_description = "ApplovinApi"
file_path = "."
commit_message = "Initial commit"

# Create an instance of GitHubRepoManager
repo_manager = GitHubRepoManager(token, repo_name, repo_description)

# Create the repository
repo_manager.create_repository()

# Commit and push the file to the repository
repo_manager.commit_and_push(file_path, commit_message)

# Execute the code in the repository
# subprocess.run(["python", "-u", f"{repo_name}/file.py"])