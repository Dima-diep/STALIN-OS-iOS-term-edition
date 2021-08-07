#!/bin/bash
rm -rf /bin/grub.sh
rm -rf /bin/termuxos.sh
echo "#!/bin/bash" > /bin/login
echo "cat /etc/motd" >> /bin/login
echo "bash" >> /bin/login
rm -rf ~/Termux-OS-iOS
rm -rf ~/Music-Termux
