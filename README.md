#INSTALLATION STEPS
#####Check python vervion(NEED python3)
python3 --version

#####Install python3 pip module
sudo apt-get install python3-pip

#####Ugrade pip
python3 -m pip install pip --upgrade

#####Install python3 libraries
python3 -m pip install -r requirements.txt

#####Install netHack
python3 -m pip install -e .

#GIVE RIGHTS MAY NEED
sudo usermod -aG docker $USER
sudo usermod -aG tcpdump $USER
====>Log out and Log in again
sudo chmod 777 /usr/bin/dumpcap

