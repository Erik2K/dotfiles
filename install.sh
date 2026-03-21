#!/bin/bash

# 1. Install base-devel, git and stow
echo -e "\033[0;36m--- Installing base-devel, git and stow... ---\033[0m"
sudo pacman -S --needed base-devel git stow

# 2. Install Oh My Zsh & Powerlevel10k (if not present)
if [ ! -d "$HOME/.oh-my-zsh" ]; then
    echo -e "\033[0;36m--- Installing Oh My Zsh... ---\033[0m"
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
fi

if [ ! -d "$HOME/.oh-my-zsh/custom/themes/powerlevel10k" ]; then
    echo -e "\033[0;36m--- Installing Powerlevel10k... ---\033[0m"
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
fi

# 3. Install Paru (AUR Helper)
if ! command -v paru &> /dev/null; then
    echo -e "\033[1;33m--- Installing Paru from AUR... ---\033[0m"
    git clone https://aur.archlinux.org/paru.git /tmp/paru
    cd /tmp/paru && makepkg -si --noconfirm
    cd - && rm -rf /tmp/paru
fi

# 4. Install packages
echo -e "\033[0;36m--- Installing all packages from lists... ---\033[0m"
sudo pacman -S --needed - < pkglist.txt
paru -S --needed - < aur_pkglist.txt

# 5. Deploy symlinks
echo -e "\033[0;32m--- Deploying symlinks with Stow ---\033[0m"
stow qtile
stow nvim
stow kitty
stow rofi
stow picom
stow gtk
stow -t ~ zsh
stow -t ~ x11

echo -e "\033[0;32m--- Búnker deployed successfully! ---\033[0m"
