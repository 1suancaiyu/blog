## copy
rsync -avzh  ./dir1/*  ./dir2/

tar cvf – /home/src_dir | tar xvf – -C /opt



## install
apt-get update && apt-get install -y openssh-server vim screen proxychains htop zip &&  sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && service ssh enable && service ssh restart



https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile
'\r': command not found - .bashrc / .bash_profile 
sed -i 's/\r$//' filename



screen -S <screen id> -X quit

