#!/bin/sh

git add -N .

git add -p

if ! git commit; then
    echo "Pre-commit hooks failed. Please fix the issues and try again."
    exit 1
fi
