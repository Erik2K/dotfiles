#!/bin/bash

DOTFILES_DIR="$HOME/dotfiles"
cd "$DOTFILES_DIR"

echo "\033[0;32m--- Updating package lists... ---\033[0m"
pacman -Qqen > pkglist.txt
pacman -Qqem > aur_pkglist.txt

git add .

msg="Auto-update: $(date +'%Y-%m-%d %H:%M')"
git commit -m "$msg"

echo -e "\033[0;32m--- Pushing to GitHub... ---\033[0m"
git push origin main
