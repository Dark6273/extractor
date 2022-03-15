# Import needed library
import view.views as view
from time import sleep
from sys import exit
import requests
from bs4 import BeautifulSoup
import os


def export(): # Save all find link in extractor file
    try : # File exist
        file = open('extractor.txt', 'w+')
    except: # Creat file and open
        os.system('touch extractor.txt' if os.name == 'nt' else 'type nul > extractor.txt')
        file = open('extractor.txt', 'w+')

        
    for i in range(0, 20): # For all layer
        if os.path.exists('data/{}'.format(i)): # File exist
            layer = open('data/{}'.format(i)) # open file
            data = layer.readlines() # Read all data in file
            data = [d.strip() for d in data] # Remove \n in file
            for d in data:
                file.write('{}\n'.format(d)) # Write in extractor file
                
    file.close() 
    
    view.main_banner()
    view.show(1, 'Links were extracted successfully !!')
    sleep(1)
    main()


def clear(): # Remove file exist before
    for file_name in range(0,20):
        if os.path.exists("data/{}".format(file_name)): # If exist remove
            os.system('rm data/{}'.format(file_name))
        else:
            return 0


def optimizer(name): # Remove dublicate links
    file = open("data/{}".format(name)) # Open file
    data = file.readlines() # Read data
    file.close() # close file
    
    data = [t.strip() for t in data] # Remove \n
    
    open("data/{}".format(name), 'w').close() # Clear file
    
    for num in data:
        file = open("data/{}".format(name), 'a+')
        saves = file.readlines()
        saves = [save.strip() for save in saves]
        
        if num not in saves: # If not exist in file write 
            file.write(num + '\n')


def add_in_history(link, count): # Add extrac history
    file = open('data/history', 'a+')
    file.write(link + ',' + str(count) + '\n')


def extract(): # Extract link
    url = view.select('Enter the target site link ') # Get Main url
    
    try:
        layers = int(view.select('Enter the number of penetrations below the links ')) # Count of layer
    except:
        wrong()
        
    clear() # Call clear function for remove file exist
    view.main_banner() # Show main banner
        
    for layer in range(0, layers):
        if layer == 0:
            data = get_link(url) # Get data
            if data != -1:
                add_in_history(url, layers) # Add in history file
                write(data, layer) # Write in file
            else:
                view.show(0, 'There was a problem getting the site information. Try again !!') # Show error
        else:
            links = open('data/{}'.format(layer - 1)) # Read link for extract again
            links = [link.strip() for link in links] # Read all link
            
            for link in links:
                data = get_link(link) # Call get link for extract link
                if data != -1:
                    write(data, layer) # Write data in file name layer
                    view.show(1 ,'layer => ' + str(layer) + ' || link => ({})'.format(link)) # Status code 200
                else:
                    view.show(0 ,'layer => ' + str(layer) + ' || link => ({})'.format(link)) # Status code other
        
        optimizer(layer) # Call optimizer function
        
    export() # Write file in extractor.txt
        

def write(data, code): # Write data
    try :
        file = open('data/{}'.format(code) ,'a+') # If file exist
    except:
        os.system('touch data/{}'.format(code) if os.name == 'nt' else 'type nul > data/{}'.format(code)) # Creat file
        file = open('data/{}'.format(code), 'a+') # Open file
        
    for line in data:
        file.write(line + '\n') # Write data 
    file.close() # Close file
        

def get_link(link): # Extract link
    data = requests.get(link) # Download page Source
    
    if data.status_code == 200:
        data = BeautifulSoup(data.content, 'html.parser') # Change mode to html parser
        urls = data.find_all('a') # Find all a tag in data
        ls = [] # Empty list for append valid link
        
        for url in urls: # Move in all tag
            text = str(url.get('href')) # Extract hyper link
            if text.find('http') != -1 : # If valid link
                ls.append(text) # Add in data list
        
        return ls
    else:
        return -1
            

def history(): # Read history data and show
    with open('data/history') as f:
        data = f.readlines() # Read data
        
    data = [d.strip() for d in data] # Remove \n
    view.history(data) # Show data


def bye(): # Exit from app
    view.bye()
    sleep(1)
    exit()


def wrong(): # Wrong select
    view.wrong()
    sleep(1)
    main()


def main(): # Main function
    view.main() # Show main banner and select list
    
    try:
        select = int(view.select("Enter your desired option ")) # Select option
    except:
        wrong() # Wrong input
        
    
    if select == 1: # Extract data
        extract()
    elif select == 2: # Export data
        export()
    elif select == 3: # History extract
        history()
    elif select == 0: # Exit
        bye()
    else: # Wrong number
        wrong()