#!/bin/bash
# Script to demonstrate Git and GitHub workflow for Part (b)
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=== STEP 1: Creating Remote Repository (Simulating GitHub Remote) ==="
rm -rf remote_github_repo.git local_repo
git init --bare -b main remote_github_repo.git
REMOTE_URL="$DIR/remote_github_repo.git"
echo "Remote repo created at: $REMOTE_URL"
echo "(In real GitHub, this corresponds to: https://github.com/<username>/student-mgmt.git)"

echo ""
echo "=== STEP 2: Cloning the Remote Repository to Local System ==="
git clone "$REMOTE_URL" local_repo
cd local_repo

echo ""
echo "=== STEP 3: Adding Project Files to the Cloned Local Repo ==="
cp "$DIR/app.py" .
cp -r "$DIR/templates" .
git status

echo ""
echo "=== STEP 4: Staging and Committing Changes ==="
git add app.py templates/
git status
git commit -m "feat: Initial commit of Student Information Management System"

echo ""
echo "=== STEP 5: Pushing the Project to Remote (GitHub) ==="
git push origin main

echo ""
echo "=== STEP 6: Modifying Project Files (e.g. Updating Student Management) ==="
echo "# Updated with logging support" >> app.py
git status -s
git add app.py
git commit -m "chore: Update app.py with logging comment"
git push origin main

echo ""
echo "=== STEP 7: Verification of Remote and Git Log ==="
git remote -v
git log --oneline
