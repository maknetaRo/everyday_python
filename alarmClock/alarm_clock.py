"""
Make a program that accepts command line arguments for what time to go off, and when it does it should launch a Youtube video in your browser that will start playing.

The program should read in a text file that contains URLs to different Youtube videos and will randomly choose one and launch it. My command line args were in the form of --hour <hour> --minute <minute> --<pm/am> but you should do whatever you feel is easiest or most convenient for you.
"""

import time, webbrowser, random, argparse

def get_time():
    local_time = time.localtime()
    hour = time.strftime('%H', local_time)
    minute = time.strftime('%M', local_time)
    return hour, minute

def alarm():

    wake_up_time = argparse.ArgumentParser(description="Enter the alarm time (h:m)")
    print(wake_up_time)

    if len(wake_up_time) < 8:
        
        input_hour = wake_up_time[:2]
        input_minute = wake_up_time[3:5]

    return input_hour, input_minute

def get_music():
    f = open('youtube-links.txt', 'r')
    f = f.readlines()
    links = []
    for line in f:
        links.append(line)
    return links

def random_music():
    links = get_music()
    link = random.choice(links)
    return link 

print(random_music())

def start_program():
    input_hour, input_minute = alarm()      

    while True:
        hour, minute = get_time()
        
        if hour == input_hour and minute == input_minute:
            print("Equal")
            link = random_music()
            webbrowser.open(link)
            break


start_program()