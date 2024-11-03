#!/bin/sh

git add -N .

git add -p

while ! git commit; do
    echo "Pre-commit hooks failed. Re-running git add and attempting to commit again..."
    # Re-stage any modified files after the pre-commit hooks modify them
    git add -A
done
