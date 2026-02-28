import os
import time  
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_effect(string, speed=0.1998, lead_delay=0.5, tail_delay=0.5):
    """
    Print with a cool type writer effect
    
    Args:
        string (_String_): What you want typed
    
        speed (_Float_): how fast the text goes. default is 0.1998
        
        lead_delay (_Float_): The pause before the text starts displaying. default is 0.5
        
        tail_delay (_Float_): The pause after the text displays. default is 0.5"""
        
      
    time.sleep(lead_delay)
        
    for i in string:
        time.sleep(speed)
        print(i, end="", flush=True)
    time.sleep(tail_delay)
    print()
    
