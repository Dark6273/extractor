# Import needed library
from colorama import Fore
from os import system, name
from time import sleep



# Main logo
def main_banner():
    system('cls' if name == 'nt' else 'clear') # Clear Screen
    print(Fore.RED + """
          
          
    ███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗ ██████╗ ██████╗ 
    ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
    █████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   ██║   ██║██████╔╝
    ██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   ██║   ██║██╔══██╗
    ███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║
    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                           
        
          """)

    
# Print menu
def menu():
    sleep(0.05)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose one of the options below\n")
    sleep(0.05)
    print(Fore.YELLOW + ' [1] Start extraction')
    sleep(0.05)
    print(Fore.MAGENTA + ' [2] Export all link')
    sleep(0.05)
    print(Fore.GREEN + ' [3] History')
    sleep(0.05)
    print(Fore.RED + ' [0] Exit...' + Fore.RESET)
    

# Select user   
def select(text):
    sleep(0.03) # 0.03s sleep
    try:
        # Print input text and turn it into number and return base
        return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Extractor "+ Fore.GREEN + "~ " + Fore.BLUE + "Select" + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] "+ Fore.YELLOW + text + Fore.RESET + " ")
    except:
        # In the event of incoming number
        return -1
    
    
def show(color, text):
    if color == 0: # Red color
        print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Extractor "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.RED + text)
    else: # Green color
        print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Extractor "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.GREEN + text)   
    
    
# Show history extract
def history(data):
    main_banner() # Show main banner and clear screen
    
    count = 0 # For color show
    for i in data:
        if count % 2 == 0: # Yellow text
            print(Fore.GREEN + " [" + str(count + 1) + "] " + Fore.YELLOW + i)
        else: # Red text
            print(Fore.GREEN + " [" + str(count + 1) + "] " + Fore.RED + i)
        count += 1
    

# Print Good Bye :)
def bye():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Extractor "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "!" + Fore.RED +"] " + Fore.YELLOW + 'We hope you enjoy the Extractor')


# Wrong Input
def wrong():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Extractor "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'The input structure has not been observed !!')


# Main Menu
def main():
    main_banner()
    menu()
    