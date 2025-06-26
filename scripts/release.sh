#!/bin/bash

# Usage: ./release.sh 1.2.3
# Assumes version is set in pyproject.toml or setup.cfg

set -e

VERSION=$1

if [[ -z "$VERSION" ]]; then
  echo "❌ Error: No version number supplied."
  echo "👉 Usage: ./release.sh 1.2.3"
  exit 1
fi

TAG="v$VERSION"

# Confirm version bump is in code
echo "📦 Preparing release: $TAG"
grep "$VERSION" pyproject.toml || {
  echo "❌ Version $VERSION not found in pyproject.toml. Did you forget to bump it?"
  exit 1
}

# Commit the version bump
git add -A
git commit -m "Release $TAG"

# Create tag
git tag "$TAG"

# Push commit and tag
git push origin main
git push origin "$TAG"

echo "✅ Release $TAG pushed! GitHub Actions will handle the rest."
