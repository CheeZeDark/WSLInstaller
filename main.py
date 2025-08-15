import os
import ctypes
from time import sleep
def Main():
    choose_wsl = input("Pls Write Mode to Download WSL: ")
    if(choose_wsl == "install-wsl"):
        os.system("wsl --install")
        print("Succesfully installed Windows Subsystem Linux!!! \nPlease Restart PC to Take Changes!!! \nCreated by CheeZeDark(Rikko Matsumato)!!!")
        os._exit(210)
    elif (choose_wsl == "installwsl-ubuntu"):
        os.system("wsl --install -d Ubuntu")
        print("Succesfully Installed Ubuntu!!! \nCreated by CheeZeDark(Rikko Matsumato)!!!")
        os._exit(443)
    else:
        print("Unknown Mode!!! Pls Choose Mode Again After Launching My Script.")
        sleep(14)
        os._exit(115)

if __name__ == "__main__":

    Main()
