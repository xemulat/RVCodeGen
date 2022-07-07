from os import system, path, remove
from urllib.request import urlretrieve
# Don't Remove pls
urlretrieve('https://raw.githubusercontent.com/xemulat/ReVancedPacker/main/integrations.json', 'integrations.json')
from contextlib import suppress
from gc import collect as ccollect, set_threshold
from json import load
from sys import exit
from time import sleep
from colorama import Fore, init
init(autoreset=True)

set_threshold(900, 15, 15)

def gcollect():
    if path.exists('debug.ini'):
        print('Garbage Collected: ', ccollect())
    else:
        ccollect()

with open('integrations.json') as pf:
    INTEGRATIONS = load(pf)


class Printer:
    @staticmethod
    def __clr_print(color: str, text: str, end: str = Fore.WHITE):
        print(color + text + end)

    @classmethod
    def blue(cls, text: str):
        cls.__clr_print(Fore.BLUE, text)

    @classmethod
    def red(cls, text: str):
        cls.__clr_print(Fore.RED, text)

    @classmethod
    def lprint(cls, text: str):
        cls.__clr_print(Fore.RED, f'[S>] {text}')

class CLI:
    __BASE = '{args}'

    def __init__(self):
        self.__corn = []

    def add(self, integration_name: str, args: list[str]):
        rads = input(f"Include {integration_name} [Y/n]: ")
        if rads == 'n':
            self.__corn.extend(args)

    @property
    def command(self):
        return self.__BASE.format(args=' '.join(f'-e {arg}' for arg in self.__corn))


class Downloader:
    @staticmethod
    def __reporter(block_num, block_size, total_size):
        read_so_far = block_num * block_size
        if total_size > 0:
            percent = read_so_far * 1e2 / total_size
            print(f"\r{percent:5.1f}% {read_so_far:{len(str(total_size))}} out of {total_size}", end='')
            if read_so_far >= total_size:
                print()
        else:
            print(f"read {read_so_far}", end='')
    gcollect()

    @classmethod
    def powpow(cls, name: str):
        printer.red(f"Downloading {name}...")
        urlretrieve(FILES[name][1], FILES[name][0], cls.__reporter)
        printer.red(f'{name} Downloaded!')

printer = Printer()
linker = CLI()
downloader = Downloader()


# ==========< Main Function >========== #

system('cls')
printer.lprint("Internet is connected")

print("Welcome, this small Python script will Generate ReVanced Cli commands for You!\n"
      "All credits to ReVanced")
printer.blue("What to do:\n"
             "1. Generate Cli Command\n"
             "99. Exit")
gosever = input("(1/99): ")
print(" ")

if gosever == '1':
    printer.blue("Disable compatibility check: (Use if compilation failed)\n"
                 "1. Disable comp. check\n"
                 "2. Enable comp. check")
    experiment = input("(1/2): ")
    if experiment == '1':
        debug = ' --experimental'
    else:
        debug = ''

    print(" ")
    printer.red("Use All Integrations or include selected Integrations")
    printer.blue("1. Use All")
    printer.blue("2. EXCLUDE Selected")
    integrations = input("(1/2): ")
    if integrations == '2':
        system('cls')
        for integration, args in INTEGRATIONS.items():
            linker.add(integration, args)

    print(" \n"
          "You must name:\n"
          "Cli - RVCLI.jar\n"
          "Patches - patches.jar\n"
          "Integrartions - integrations.jar\n"
          "YouTube - youtube.apk\n")        
    cdmm = "java -jar RVCLI.jar -a " + "youtube.apk" + " -c -o revanced.apk -b patches.jar -m integrations.apk " + linker.command + " -e background-play -e exclusive-audio-playback -e codecs-unlock -e upgrade-button-remover -e tasteBuilder-remover" + debug
    input(f"Generated script: " + cdmm + "\n"
          "Click ENTER to exit\n")
    print(" ")
    exit(sleep(4))
    
if gosever == '99':
    exit(sleep(2))
