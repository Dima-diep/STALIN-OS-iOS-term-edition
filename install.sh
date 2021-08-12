#!/bin/bash
chmod 777 *.py *.sh *.html
apk update
apk upgrade
apk add python termux-api mpv htop-legacy neofetch mc tor libc++ tar wget calc
python3 -m pip install --upgrade pip
python3 -m pip install termcolor
termux-setup-storage
apk remove zsh
apk autoremove
echo "Configuring your system..."
rm -rf ~/.oh-my-zsh
rm -rf ~/.zshrc
mv ~/.bashrc ~/.bashrc.old
cd ~/
mkdir STALIN-OS
cd STALIN-OS
mkdir boot
mkdir chroot
mkdir system
mkdir .initialize
cd boot
mkdir bootanimation
cd ~/STALIN-OS-iOS-term-edition
mv grub.py ~/STALIN-OS/boot
mv *.mp3 ~/STALIN-OS/boot
mv login.py ~/STALIN-OS/boot
mv pass.py ~/STALIN-OS/boot
mv chlogin.py ~/STALIN-OS/chroot
mv chpass.py ~/STALIN-OS/chroot
mv chroot.py ~/STALIN-OS/chroot
mv pacman.py ~/STALIN-OS/chroot
mv setting.py ~/STALIN-OS/system
mv terminal.py ~/STALIN-OS/chroot
mv initialize.* ~/STALIN-OS/.initialize
mv *.html~/STALIN-OS/system
mv uninstall.* ~/STALIN-OS/system
mv boot.tar.gz ~/STALIN-OS/boot/bootanimation
mv boot.py ~/STALIN-OS/boot
mv fordev.html ~/STALIN-OS/system
mv Manifest.json ~/STALIM-OS/system
cd ~/STALIN-OS/boot/bootanimation
tar -xvzf boot.tar.gz
chmod 777 *
cd ~
echo "Move your files into new system..."
mv * ~/STALIN-OS/home
echo "#!/bin/bash" > /bin/login
echo "python3 ~/STALIN-OS/boot/grub.py" >> /bin/login
cd ~/STALIN-OS/chroot
touch contacts.txt
cd ~/STALIN-OS/system
touch .killhist.sh
chmod 777 .killhist.sh
echo "#!/bin/bash" > .killhist.sh
echo "rm -rf ~/.bash_history" >> .killhist.sh
echo "rm -rf ~/.zsh_history" >> .killhist.sh
echo "rm -rf ~/.wget_hsts" >> .killhist.sh
echo "rm -rf ~/.python_history" >> .killhist.sh
echo "rm -rf ~/.sqlite_history" >> .killhist.sh
cd ~/STALIN-OS/home
git clone https://github.com/Dima-diep/Music-Termux
chmod 777 ~/STALIN-OS/home/Music-Termux/*
echo "Your system login is oldlogin"
echo "Your system password is oldpass"
echo "STALIN-OS has been installed. Restart iSH App for starting OS!"
echo "Until reboot, uninstall any zsh plugins from system and change basic shell to bash by run chsh because operating system isn't compatible with zsh"
