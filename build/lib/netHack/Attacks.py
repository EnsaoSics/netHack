from distutils.util import copydir_run_2to3
import subprocess



#==================================================ARP CACHE POISONNING===================================================
def ARPpoisonning() : 

        #Victim(192.168.2.10)
        cmd1=' gnome-terminal -- bash -c " docker run -it --rm -h "--Victim--" --name Victim --network=NET --ip 192.168.2.10 arp_victim bash" '
        
        #Attacker(192.168.2.20)
        cmd2=' gnome-terminal -- bash -c "docker run -it --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.20 arp_attacker bash" '
        #Wireshark to visualize the traffic
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--wireshark--" --privileged --cap-add=NET_ADMIN --name Sniffing --net=host tcpdump -i lig -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
