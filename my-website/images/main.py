# -*- coding: utf-8 -*-
import time
#This is a comment
def zack():
    print("Zach Lakeman is a smart detective from Ohio. His life is going nowhere until he meets Helen Parker, a stunning woman with a passion for law.")
    time.sleep(2)
    print('(Playing as zack) You are at your office at the police station')
    time.sleep(2)
    print('Suddenly a woman opens the door with a stern look on her face')
    time.sleep(2)
    print('Z: “hi, whomst are you"')
    time.sleep(2)
    print('H: “yes, hello i’m helen and i think you are a bad detective.”')
    time.sleep(2)
    print('Z “gasp! How dare you, i hate you. Now if you will excuse me i must leave”')
    time.sleep(2)
    choice=raw_input(' you have to get to your car a couple of blocks away. Take the shortcut through the back alley(1) or go the long way on the sidewalk(2)')
    if choice == '2':
        print('you get to your car and go home, never to see that stoopid helen again')
        time.sleep(1)
        print('end')
        return
    else:
        print('you encounter a strange man')
        time.sleep(1)
        print('Man:“hello(he says creepily) i am the mass murderer you’ve been investigating for months and im going to kill you now”')
        time.sleep(2)
        print('He charges at you with a knife')
    time.sleep(1)
    choice=raw_input('run away(1) or stay still frozen with fright(2)')
    while choice != '1' and choice !='2':
        choice=raw_input('Invalid Answer. Try again(1/2)')
    if choice == '1':
        print('you weren’t fast enough, he stabs you and die')
        time.sleep(1)
        print('end')
        return
    else: 
        print('out of nowhere helen comes out and knocks out the murderer!')
        time.sleep(2)
        print('Z: “thank you! You saved me, and i now see you’re not so bad after all”')
        time.sleep(2)
        print('H: “no problem. Hey do you want to get some coffee or something?”')
        time.sleep(2)
        choice=raw_input('do you accpet her offer(1) or do you decline(2)')
        while choice != '1' and choice != '2':
            choice=raw_input('Invalid Answer.Try again. (1/2)')
        if choice == '2':
            print('Z: "nah bruh, im good lol bye."')
            time.sleep(2)
            print('You leave the alley without arresting the murderer for some reason.')
            time.sleep(1)
            print('You really are a bad detective.')
            time.sleep(1)
            print('later on you hear that another murder has taken place, presumably by the same murderer.')
            choice=raw_input('do you own up to your mistake, regardless the consequences(1) or do you dip to the nearest airport, book a ticket to tibet and never return(2)')
            while choice != '1' and choice != '2':
                choice=raw_input('Invalid Answer.Try again. (1/2)')
            if choice == '2':
                print('youve evaded the law but can you evade the weight of your crimes on your conscience?')
                time.sleep(1)
                print('you become very paranoid and depressed, ultimately becoming a hermit outside of a small village never to return to regular society.')
                time.sleep(1)
                print('end')
                return
            else:
                print('the town finds out about your crime and constantly ridicule you.')
                time.sleep(1)
                print('you go to court and the lawyer that represents you is helen and its very awkward')
                time.sleep(1)
                print('the jury finds you guilty and the judge sends you to jail for 10 years.')
                print('end')
                return
        else:
            print('Z: "yea sure my treat"')
        time.sleep(2)
        print('fast foward a few months')
        time.sleep(1)
        print('Helen has gotten very busy at the law firm(because of the mass murderer case) and so she doesn’t have that much time for your relationship anymore.')
        print(' You notice she’s been getting texts from a certain Shane.')
        time.sleep(4)
        print('Z: “He’s stealing my girl!”')
        choice=raw_input(' do you let it happen and slowly let the relationship die(1) or burst into her office without investigating the situation find shane and beat him up(2)')
        while choice != '1' and choice != '2':
            choice=raw_input('Invalid Answer.Try again. (1/2)')
        if choice == '1':
            print('you cry all the time now, wondering about what could have been with helen, who is now very successful and happy with that stupid dumb-dumb-face SHANE.')
            time.sleep(1)
            print('end')
            return
        else: 
            print('you burst into her office and scream for shane to show his stupid face')
        time.sleep(2)
        print('H: “what are you doing?! This isnt a good time for your shenanigans. Would you please get out of my office and go home?”')
        time.sleep(3)
        print('Z: “NO! I wont leave until the shane thats been texting your phone shows himself so i can go beat him up in the back alley.”')
        time.sleep(3)
        print('H: “Shane? But he-”')
        print('She is interrupted by her office door opening. A tall muscular man walks in.')
        time.sleep(2)
        print('S: “It is I, SHANE! Who has been asking for a fight with me?”')
        time.sleep(2)
        choice=raw_input('You fearlessly say that it was you(1) or you deny asking for a fight but do ask why he has been texting your girlfriend(2)')
        while choice != '1' and choice != '2':
            choice=raw_input('Invalid Answer.Try again. (1/2)')
        if choice == '1':
            print('S: "Oh yeah?!Lets go man, ill beat you up."')
            time.sleep(2)
            for you in ['kicks','punches','dropkicks']:
                print('He '+you+' you and never misses')
            time.sleep(2)
            print('you get your butt handed to you by this behemoth of a man and run away for five years too ashamed to face helen again.')
            time.sleep(1)
            print('end')
            return
        else:
            print('shane calms down and starts explaining to you why he was texting helen')
            time.sleep(2)
            print('S:“Ok, first of all, I’m gay so you dont have to worry about me stealing your girl.”')
            time.sleep(3)
            print('Z: “But then why were you texting Helen?”')
            time.sleep(2)
            print('H: “Because he was asking me for help on the case he was working on. Nothing else!”')
            time.sleep(3)
            print('S: “Also, why did you automatically assume she was cheating on you? Seems like you have a bad case of toxic masculinity and your ego can’t handle your girlfriend talking to any other guys.”')
            time.sleep(4)
            print('Z: “But I-”')
            print('H: “Zip it Zack. We’re over. Now please leave.”')
            time.sleep(2)
            print('She points to the door and you leave with your head down, ashamed of what you’ve done.')
            time.sleep(2)
            print('Helen eventually becomes very successful and never talks to you again.')
            time.sleep(1)
            print('The End :) ')
            return