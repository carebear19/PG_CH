import pyautogui as pg
import time
import webbrowser

points = 0

#Question goes here
answer = pg.prompt(
"""
Which would you rather do?

a) Play Basketball
b) Eat Burger King
c) Go to clubs

"""
    )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


#Question goes here
answer = pg.prompt(
"""
What is your favorite food?

a) Pizza
b) Anything
c) Burgers

"""
    )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
Where would you rather be?

a) Califorina 
b) Home
c) Parties

"""
    )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
How many kids would you want?

a) 4
b) 2
c) 0

"""
    )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
Where would you want to live?

a) Los Angeles
b) Ohio
c) Just lucky to have a house

"""
    )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
How many hours do you get of sleep?

a) 8hrs
b) 10hrs
c) Would sleep all day

"""
    )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


#END OF SURVEY
pg.alert("OK, here's your character...")
#Lenyy
if points <7:
    pg.alert("You are Lenny!")
    webbrowser.open("https://www.google.com/search?q=lenny+for+grown+ups&rlz=1C1GCEA_enUS752US752&tbm=isch&source=lnms&sa=X&ved=0ahUKEwjKkO-Apu7YAhXhSd8KHQSmDNcQ_AUICigB&biw=1083&bih=677&dpr=0.9#imgrc=-Sji2cBZhsZcbM:")

#Erik
elif points >=7 and points <=3:
    pg.alert("You are Eric")
    webbrowser.open("https://www.google.com/search?q=eric+from+grown+ups&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjE8du7pu7YAhWIv1MKHRyJBlgQ_AUICigB&biw=1083&bih=677#imgrc=dV3HysdD6tieDM:")

#Higens
elif points >=10:
    pg.alert("You are Higgens!")
    webbroswer.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1083&bih=677&tbm=isch&sa=1&ei=SkdnWtnWMIjq_AbpypPgCQ&q=higgins+from+grown+ups&oq=higens+from+grown+ups&gs_l=psy-ab.1.0.0i13k1.67647.73974.0.75436.10.10.0.0.0.0.84.611.10.10.0....0...1c.1.64.psy-ab..0.4.281...0i7i5i30k1j0i7i30k1.0.OX77_opd_K8#imgrc=EphZsjzarSLb0M:")
