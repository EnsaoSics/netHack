###################STARTING OF DOCKERFILE INSTALLATION
import subprocess


#########REQUIREMENT INSTALLATION
#Setting up docker network 
net = "docker network create --opt com.docker.network.bridge.name=lig --subnet=192.168.2.0/24 NET " 
subprocess.run(net,shell=True)
print("#"*77)

#install Wireshark
net = "sudo apt install wireshark" 
subprocess.run(net,shell=True)
print("#"*77)


#install progressbar
net = "sudo pip install progressbar" 
subprocess.run(net,shell=True)
print("#"*77)

#install gnome-terminal
net = "sudo apt-get install gnome-terminal" 
subprocess.run(net,shell=True)
print("#"*77)


#########DOCKER CONTAINERS BUILDING
#ARP victim
cmd2= "docker build -t arp_victim ./dockerfiles/arppoisonning/arp_victim "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)

#ARP attacker
cmd5= "docker build -t arp_attacker ./dockerfiles/arppoisonning/arp_attacker "
subprocess.run(cmd5 ,shell=True)
print("#"*77)

#tcpdump
cmd2= "docker build -t tcpdump ./dockerfiles/Tcpdump "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)

#HTTP victim
cmd2= "docker build -t http_victim ./dockerfiles/httpflood/http_victim "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)

#HTTp attacker
cmd5= "docker build -t http_attacker ./dockerfiles/httpflood/http_attacker "
subprocess.run(cmd5 ,shell=True)
print("#"*77)

#SYN victim
cmd2= "docker build -t syn_victim ./dockerfiles/synflood/syn_victim "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)

#SYN attacker
cmd5= "docker build -t syn_attacker ./dockerfiles/synflood/syn_attacker "
subprocess.run(cmd5 ,shell=True)
print("#"*77)

#smurf victim
cmd2= "docker build -t smurf_victim ./dockerfiles/smurf/smurf_victim "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)

#smurf1 victim
cmd2= "docker build -t smurf_victim1 ./dockerfiles/smurf/smurf_victim1 "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)

#smurf attacker
cmd5= "docker build -t smurf_attacker ./dockerfiles/smurf/smurf_attacker "
subprocess.run(cmd5 ,shell=True)
print("#"*77)

#TCP Hijacking client
cmd3= "docker build -t hijack_client ./dockerfiles/TCPhijacking/TCPhijacking_client"
subprocess.run(cmd3 ,shell=True)
print("#"*77)

#TCP Hijacking server
cmd4= "docker build -t hijack_server ./dockerfiles/TCPhijacking/TCPhijacking_server"
subprocess.run(cmd4 ,shell=True)
print("#"*77)

#TCP Hijacking attacker
cmd5= "docker build -t hijack_attacker ./dockerfiles/TCPhijacking/TCPhijacking_attacker"
subprocess.run(cmd5 ,shell=True)
print("#"*77)

#Srst client
cmd9= "docker build -t srst_client ./dockerfiles/Srst/Srst_client"
subprocess.run(cmd9 ,shell=True)
print("#"*77)

#Srst server
cmd10= "docker build -t srst_server ./dockerfiles/Srst/Srst_server"
subprocess.run(cmd10 ,shell=True)
print("#"*77)

#Srst attacker
cmd11= "docker build -t srst_attacker ./dockerfiles/Srst/Srst_attacker"
subprocess.run(cmd11 ,shell=True)
print("#"*77)

#Target server
cmd10= "docker build -t target_server ./dockerfiles/scan/Target"
subprocess.run(cmd10 ,shell=True)
print("#"*77)

#Scanner
cmd13= "docker build -t scan_attacker ./dockerfiles/scan/Scanner"
subprocess.run(cmd13 ,shell=True)
print("#"*77)

# macflood pour la victime
docker_build_cmd = "docker build -t mac_victime ./dockerfiles/mac/mac_victime"
subprocess.run(docker_build_cmd, shell=True)
print("#" * 77)
# macflood pour l'attaquant
docker_build_cmd = "docker build -t mac_attaquant ./dockerfiles/mac/mac_attaquant"
subprocess.run(docker_build_cmd, shell=True)
print("#" * 77)

# ping pour la victime
docker_build_cmd = "docker build -t ping_victime ./dockerfiles/ping/ping_victime"
subprocess.run(docker_build_cmd, shell=True)
print("#" * 77)
# ping pour l'attaquant
docker_build_cmd = "docker build -t ping_attaquant ./dockerfiles/ping/ping_attaquant"
subprocess.run(docker_build_cmd, shell=True)
print("#" * 77)

# icmp pour la victime
docker_build_cmd = "docker build -t icmp_victime ./dockerfiles/icmp/icmp_victime"
subprocess.run(docker_build_cmd, shell=True)
print("#" * 77)
# icmp pour l'attaquant
docker_build_cmd = "docker build -t icmp_attaquant ./dockerfiles/icmp/icmp_attaquant"
subprocess.run(docker_build_cmd, shell=True)
print("#" * 77)

#macspoof_attacker
cmd19= "docker build -t macspoof_attacker ./dockerfiles/Macspoofing/macspoof_attacker"
subprocess.run(cmd19 ,shell=True)
print("#"*77)

#macspoof_victim
cmd20= "docker build -t macspoof_victim ./dockerfiles/Macspoofing/macspoof_victim"
subprocess.run(cmd20 ,shell=True)
print("#"*77)
################## END OF DOCKERFILE INSTALLATION
