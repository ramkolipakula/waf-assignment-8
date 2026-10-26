#!/bin/bash
# Script to demonstrate Git Branch Management for Part (a)
set -e

cd "$(dirname "$0")"

echo "=== 1. Initializing Git Repository ==="
rm -rf .git
git init -b main
git add app.py templates/
git commit -m "Initial commit: Basic Student Information Management System"

echo ""
echo "=== 2. Creating a new branch (feature-search) ==="
git branch feature-search
git branch

echo ""
echo "=== 3. Switching to branch (feature-search) ==="
git checkout feature-search

echo ""
echo "=== 4. Modifying code on feature-search branch ==="
echo "# Added feature: Search module coming soon" >> app.py
git status -s
git add app.py
git commit -m "feat: Add search module placeholder on feature branch"

echo ""
echo "=== 5. Switching back to main branch ==="
git checkout main

echo ""
echo "=== 6. Merging feature-search branch into main ==="
git merge feature-search -m "Merge branch 'feature-search' into main"

echo ""
echo "=== 7. Deleting feature-search branch ==="
git branch -d feature-search
git branch

echo ""
echo "=== 8. Verification of Commit History ==="
git log --oneline --graph --decorate
