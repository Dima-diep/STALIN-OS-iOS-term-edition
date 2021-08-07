#!/bin/bash
apk add python termux-api mpv htop-legacy neofetch
pip install termcolor
termux-setup-storage
echo "#!/bin/bash" > /bin/login
echo "bash grub.sh && bash" >> /bin/login
cd /bin
touch grub.sh
echo "#!/bin/bash" > grub.sh
echo "python3 ~/Termux-OS-iOS/grub.py" >> grub.sh
touch termuxos.sh
echo "#!/bin/bash" > termuxos.sh
echo "python3 ~/Termux-OS-iOS/chroot.py" >> termuxos.sh
chmod 777 termuxos.sh
chmod 777 grub.sh
cd -
touch contacts.txt
cd ~
git clone https://github.com/Dima-diep/Music-Termux
chmod 777 ~/Music-Termux/*
echo "GRUB has been installed. If you want run GRUB from loginned system, run 'bash grub.sh' command"
