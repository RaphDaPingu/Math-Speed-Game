#!/usr/bin/env python 3.7
#Raphael Reichrudel, Yair Barak, Leon Slepichev

#שלבים:
#1. Introduction
#2. Timer
#3. Algorithm for Question Making
#4. Question Printout
#5. Check if answer is right or not
#6. If all answers are right, "perfect score" output
#7. Elif none are right, "You should practice more" output
#8. Else, "Better luck next time" output

#Introduction

import time
time.sleep(1)

print ("Welcome to our game, 60 Second Einstein!")

time.sleep(3)

print ("In this game, presented you by Raphael Reichrudel,")

time.sleep(1)

print ("Leon Slepichev,")

time.sleep(1)

print ("and Yair Barak,")

time.sleep(1)

print ("You'll need to answer as many questions as you can in a time span of 60 seconds!")

time.sleep(4)

print ("Side note: if the answer you got isn't a whole number, please round it down.")

time.sleep(4)

print ("Are you ready?")

time.sleep(2)

print ("3")

time.sleep(1)

print ("2")

time.sleep(1)

print ("1")

time.sleep(1)

print ("Go!")

time.sleep(1)

print (" ")

#Timer #קאונטדאון של 60 שניות

from time import *
import threading

def countdown():
    global my_timer

    my_timer = 60

    for x in range(60):
        my_timer -= 1
        sleep(1)

    print("Time's up!")
    

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

#Algorithm for Question Making

from random import randint

score = 0
counter = 0

while my_timer > 0:
    ans = 0
    questionnumber = randint(1, 16)
    a = randint(1, 20)
    b = randint(1, 20)
    c = randint(1, 20)
    ans1 = a + b + c
    ans2 = a + b - c
    ans3 = a + b * c
    ans4 = a + b / c
    ans5 = a - b + c
    ans6 = a - b - c
    ans7 = a - b * c
    ans8 = a - b / c
    ans9 = a * b + c
    ans10 = a * b - c
    ans11 = a * b * c
    ans12 = a * b / c
    ans13 = a / b + c
    ans14 = a / b - c
    ans15 = a / b * c
    ans16 = a / b / c
    counter += 1
    
    if questionnumber == 1:
        ##print (ans1) used for printing correct answer
        print (str(a), " + ", str(b), " + ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans1:
            print ("Correct!")
            score += 1
        print (" ")
        
        if my_timer == 0:
            break        
        
    elif questionnumber == 2:
        ##print (ans2)
        print (str(a), " + ", str(b), " - ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans2:
            print ("Correct!")
            score += 1
        print (" ")
        
        if my_timer == 0:
            break        
        
        
    elif questionnumber == 3:
        ##print (ans3)
        print (str(a), " + ", str(b), " * ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans3:
            print ("Correct!")
            score += 1
        print (" ")

        if my_timer == 0:
            break        
        
    elif questionnumber == 4:
        ##print (int(ans4))
        print (str(a), " + ", str(b), " / ", str(c), "= ") #fix incorrect answers
        ans = int(input("Type your answer: "))
        if ans == int(ans4):
            print ("Correct!")
            score += 1
        print (" ")

        if my_timer == 0:
            break        
        
    elif questionnumber == 5:
        ##print (ans5)
        print (str(a), " - ", str(b), " + ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans5:
            print ("Correct!")
            score += 1
        print (" ")

        if my_timer == 0:
            break        
        
    elif questionnumber == 6:
        ##print (ans6)
        print (str(a), " - ", str(b), " - ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans6:
            print ("Correct!")
            score += 1
        print (" ")

        if my_timer == 0:
            break        
        
    elif questionnumber == 7:
        ##print (ans7)
        print (str(a), " - ", str(b), " * ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == int(ans7):
            print ("Correct!")
            score += 1
        print (" ")

        if my_timer == 0:
            break        

    elif questionnumber == 8:
        ##print (int(ans8))
        print (str(a), " - ", str(b), " / ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == int(ans8):
            print ("Correct!")
            score += 1
        print (" ")

        if my_timer == 0:
            break        
            
    elif questionnumber == 9:
        ##print (ans9)
        print (str(a), " * ", str(b), " + ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans9:
            print ("Correct!")
            score += 1
        print (" ")
            
    elif questionnumber == 10:
        ##print (ans10)
        print (str(a), " * ", str(b), " - ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans10:
            print ("Correct!")
            score += 1
        print (" ")
            
    elif questionnumber == 11:
        ##print (ans11)
        print (str(a), " * ", str(b), " * ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == ans11:
            print ("Correct!")
            score += 1
        print (" ")
        
    elif questionnumber == 12:
        ##print (ans12)
        print (str(a), " * ", str(b), " / ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == int(ans12):
            print ("Correct!")
            score += 1
        print (" ")
        
    elif questionnumber == 13:
        ##print (ans13)
        print (str(a), " / ", str(b), " + ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == int(ans13):
            print ("Correct!")
            score += 1
        print (" ")
        
    elif questionnumber == 14:
        ##print (ans14)
        print (str(a), " / ", str(b), " - ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == int(ans14):
            print ("Correct!")
            score += 1
        print (" ")
        
    elif questionnumber == 15:
        ##print (ans15)
        print (str(a), " / ", str(b), " * ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == int(ans15):
            print ("Correct!")
            score += 1
        print (" ")
        
    elif questionnumber == 16:
        ##print (ans16)
        print (str(a), " / ", str(b), " / ", str(c), "= ")
        ans = int(input("Type your answer: "))
        if ans == int(ans16):
            print ("Correct!")
            score += 1
        print (" ")
            
sleep(2)

#Score Commendantion

if score == 0:
    print ("You didn't answer anything correctly! Better luck next time!")
elif score / counter < 0.5:
    print ("You answered", (score), "out of", (counter), "questions correctly! That's less than half! You should practice more.")
elif score / counter == 0.5:
    print ("You answered half of the questions correctly! Good job!")
elif score / counter > 0.5:
    if score / counter == 1.0:
        print ("You answered everything correctly! Perfect!")
    elif score / counter > 0.5:
        print ("You answered", (score), "out of", (counter), "questions correctly! That's more than half! Incredible!")
