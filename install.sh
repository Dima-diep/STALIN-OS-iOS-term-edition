#!/bin/bash
apk add python termux-api mpv htop-legacy neofetch
pip install termcolor
termux-setup-storage
echo "#!/bin/bash" > /bin/login
echo "bash grub.sh && bash" >> /bin/login
cd ~
mkdir Termux-OS
cd Termux-OS
mkdir home
cd ~
echo "Move your files into new system..."
mv * ~/Termux-OS/home
cd ~/Termux-OS
mkdir boot
mkdir chroot
mkdir .initialize
mkdir temp
cd chroot
touch contacts.txt
cd ../home/Termux-OS
mv chroot.py ../../chroot
mv grub.py ../../boot
mv login.py ../../boot
mv pass.py ../../boot
mv initialize.sh ../../.initialize
cd ../home
git clone https://github.com/Dima-diep/Music-Termux
chmod 777 ~/Music-Termux/*
echo "Termux-OS has been installed."
