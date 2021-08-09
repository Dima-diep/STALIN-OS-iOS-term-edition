#!/bin/bash
echo "#!/bin/bash" > /bin/login
echo "cat /etc/motd" >> /bin/login
echo "bash" >> /bin/login
cd ~/Termux-OS/home
rm -rf ~/Termux-OS/home/Termux-OS-iOS
rm -rf ~/Termux-OS/home/Music-Termux
mv * ~/
cd ~
rm -rf Termux-OS
