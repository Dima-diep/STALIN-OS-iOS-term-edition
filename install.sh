#!/bin/bash
apk add python termux-api mpv htop-legacy neofetch mc
apk remove zsh
apk autoremove
pip install --upgrade pip
pip install termcolor
termux-setup-storage
echo "#!/bin/bash" > /bin/login
echo "python3 ~/Termux-OS/boot/grub.py" >> /bin/login
cd ~
mkdir Termux-OS
cd Termux-OS
mkdir home
cd ~
echo "Move your files into new system..."
mv * ~/Termux-OS/home
echo "Configuring your system..."
cd ~/Termux-OS
mkdir boot
mkdir chroot
mkdir .initialize
mkdir temp
mkdir system
cd chroot
touch contacts.txt
cd ../home/Termux-OS-iOS
mv chroot.py ../../chroot
mv grub.py ../../boot
mv login.py ../../boot
mv pass.py ../../boot
mv *.mp3 ../../boot
mv pacman.py ../../chroot
mv initialize.sh ../../.initialize
mv terminal.py ../../chroot
mv setting.py ../../system
mv help.html ../../system
mv uninstall.sh ../../system
mv initialize.py ../../.initialize
cd ../home
git clone https://github.com/Dima-diep/Music-Termux
chmod 777 ~/Music-Termux/*
echo "Your login is oldlogin"
echo "You password is oldpass"
echo "Please, uninstall zsh plugins until reboot"
echo "Termux-OS has been installed. Restart iSH app for starting Termux-OS"
