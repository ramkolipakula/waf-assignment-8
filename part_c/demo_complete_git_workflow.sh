#!/bin/bash
# Complete Git & GitHub Workflow Demonstration Script for Part (c)
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=========================================================="
echo "PART (C): COMPLETE GIT WORKFLOW DEMONSTRATION"
echo "=========================================================="

# Cleanup past runs if any
rm -rf .git remote_course_repo.git collaborator_workspace

echo ""
echo "=== 1. REPOSITORY INITIALIZATION ==="
git init -b main
echo "Repository initialized with main branch."

echo ""
echo "=== 2. FILE TRACKING AND STAGING ==="
git status
git add app.py templates/
git status -s

echo ""
echo "=== 3. COMMITTING CHANGES ==="
git commit -m "feat: Initial commit of Online Student Course Registration System"

echo ""
echo "=== 4. REMOTE REPOSITORY MANAGEMENT ==="
# Setup bare repository representing GitHub remote
git init --bare -b main remote_course_repo.git
REMOTE_URL="$DIR/remote_course_repo.git"
git remote add origin "$REMOTE_URL"
git remote -v
git push -u origin main

echo ""
echo "=== 5. BRANCHING ==="
git checkout -b feature-course-limit
git branch

echo ""
echo "=== 6. MODIFYING FILES ON BRANCH & COMMITTING ==="
echo "# Added course limit logic placeholder" >> app.py
git add app.py
git commit -m "feat(courses): Add maximum enrollment limit validation"

echo ""
echo "=== 7. MERGING BRANCH INTO MAIN ==="
git checkout main
git merge feature-course-limit -m "Merge branch 'feature-course-limit' into main"
git branch -d feature-course-limit
git push origin main

echo ""
echo "=== 8. COLLABORATIVE DEVELOPMENT (SIMULATION) ==="
echo "--- Collaborator clones the remote GitHub repository ---"
git clone "$REMOTE_URL" collaborator_workspace
cd collaborator_workspace
git checkout main

echo "--- Collaborator makes a contribution and commits ---"
echo "# Contributed by Collaborator: Added logging for registration events" >> app.py
git add app.py
git commit -m "collab: Add registration audit logging"
git push origin main

echo ""
echo "--- Original developer fetches and pulls collaborator updates ---"
cd "$DIR"
git pull origin main

echo ""
echo "=== 9. VERIFYING COMPLETE COMMIT GRAPH & HISTORY ==="
git log --graph --oneline --all
