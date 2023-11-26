#!/bin/bash

# Replace the following variables with your own values
TOKEN="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"
REPO_NAME="ApplovinApiOnly"
REPO_DESCRIPTION="your-repo-description"
COMMIT_MESSAGE="Initial commit"


# Initialize a commit and push it
create_repository() {
    curl -H "Authorization: token $TOKEN" -d '{"name": "'"$REPO_NAME"'", "description": "'"$REPO_DESCRIPTION"'"}' "https://api.github.com/user/repos"
}

# Initialize a commit and push it
commit_and_push() {
    git init
    git remote add origin "https://github.com/melozzz444/$REPO_NAME.git"
    git add .
    git commit -m "$COMMIT_MESSAGE"
    git push -u origin main
}

# Call the functions
create_repository
commit_and_push