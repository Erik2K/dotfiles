#!/bin/bash

# 1. Install base-devel, git and stow
echo -e "\033[0;36m--- Installing base-devel, git and stow... ---\033[0m"
sudo pacman -S --needed base-devel git stow

# 2. Install Paru (AUR Helper) if not present
if ! command -v paru &> /dev/null; then
    echo -e "\033[1;33m--- Paru not found. Installing Paru from AUR... ---\033[0m"
    git clone https://aur.archlinux.org/paru.git /tmp/paru
    cd /tmp/paru && makepkg -si --noconfirm
    cd - && rm -rf /tmp/paru
fi

# 3. Install official packages
if [ -f "pkglist.txt" ]; then
    echo -e "\033[0;36m--- Installing official packages... ---\033[0m"
    sudo pacman -S --needed - < pkglist.txt
fi

# 4. Install AUR packages
if [ -f "aur_pkglist.txt" ]; then
    echo -e "\033[0;36m--- Installing AUR packages... ---\033[0m"
    paru -S --needed - < aur_pkglist.txt
fi

# 5. Deploy symlinks with Stow
echo -e "\033[0;32m--- Deploying symlinks with Stow ---\033[0m"
stow qtile
stow nvim
stow kitty
stow rofi
stow -t ~ zsh

echo -e "\033[0;32m--- Installation Complete! ---\033[0m"
