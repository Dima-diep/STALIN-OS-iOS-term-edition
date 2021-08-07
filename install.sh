#!/bin/bash
apk add python termux-api mpv htop-legacy neofetch telegram-cli -yq
pip install termcolor
termux-setup-storage
echo "#!/bin/bash" > /bin/login
echo "bash grub.sh && bash" >> /bin/login
cd /bin
touch grub.sh
echo "#!/bin/bash" > grub.sh
echo "python3 ~/Termux-OS/grub.py" >> grub.sh
touch termuxos.sh
echo "python3 ~/Termux-OS/chroot.py" > termuxos.sh
chmod 777 termuxos.sh
chmod 777 grub.sh
cd -
touch contacts.txt
cd ~
git clone https://github.com/Dima-diep/Music-Termux
echo "GRUB has been installed. If you want run GRUB from loginned system, run 'bash grub.sh' command"
