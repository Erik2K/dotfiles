#!/bin/bash

DOTFILES_DIR="$HOME/dotfiles"
cd "$DOTFILES_DIR"

echo "Actualizando listas de paquetes..."
pacman -Qqen > pkglist.txt
pacman -Qqem > aur_pkglist.txt

git add .

msg="Auto-update: $(date +'%Y-%m-%d %H:%M')"
git commit -m "$msg"

echo "Subiendo a GitHub..."
git push origin main
