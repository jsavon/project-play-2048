#TODO: Import the module that will allow you to use Selenium
#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def play2048( times ):
    #TODO: write code in this function that:
    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    # 4. print the final score after all tries to the screen 
    
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')
    for i in range (times):
        htmlElem = browser.find_element_by_tag_name('html')
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        
    elem = browser.find_element_by_class_name('score-container')
    print ('Your final score is: ')
    print (elem.text)