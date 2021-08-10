#!/bin/bash
echo "#!/bin/bash" > /bin/login
echo "cat /etc/motd" >> /bin/login
echo "bash" >> /bin/login
cd ~/STALIN-OS/home
rm -rf ~/STALIN-OS/home/Music-Termux
mv * ~/
cd ~
rm -rf STALIN-OS*
