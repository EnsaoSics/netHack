#!/usr/bin/python3
import click
import datetime
import pyfiglet
from pyfiglet import Figlet
import time
import progressbar
from colorama import Fore,init
from pathlib import Path


from netHack.Attacks import ARPpoisonning


# Print name of Tools using pyfiglet 
print(Fore.GREEN  + '\n')
f = Figlet(font='standard')
init(autoreset=True)
print(f.renderText("   net - H 4  k  R  "))

print('    v1.0')
init(autoreset=True)
print(Fore.BLUE + '    https://github.com/gil01karougbe ')
print('   ',Fore.GREEN  + str(datetime.datetime.now()))
print('\n')




# Print Progress Bar :
def animated_marker(x):
    widgets = [Fore.GREEN + 'Loading :  ', progressbar.AnimatedMarker()]
    init(autoreset=True)
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(x):
        time.sleep(0.1)
        bar.update(i)       
# Driver's code
animated_marker(5)
print('\n')


# For Option : using click library 
@click.command()
@click.option("--name", prompt=Fore.GREEN  + """[+] Please enter attack number : 
                 \n\t1  - ARPpoisonning
                 \n\t2  - MACflooding 
                 \n\t3  - DHCPstarvation
                 \n\n --> Attack  """

, help="""Provide your attacks number : \t\n
                 1  - ARPpoisonning  \n
                 2  - MACflooding \n
                 3  - DHCPstarvation \n
          """)
#main function
def main(name):
    print('')
    time.sleep(0.4)


    if name == '1' :
        ARPpoisonning()

    elif name == '2' :
        MACflooding()

    elif name == '3' :
        DHCPstarvation()

    else : 
        print('\nPlease enter a Correct number attack , Show help for more details ( --help )')
