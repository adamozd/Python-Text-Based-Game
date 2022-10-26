from time import timezone

# This is a zombie apocalypse text-based adventure game.
# In this adventure game, users will face with a couple of situations.
# Users have to be careful with the options available and choose the most logical option available. However, if the user enters an answer which is NOT related to the options, user will be forcely returned to the starting point.
# There are various endings for each choices available but only one of them results in surviving through the zombie apocalypse.
# After each wrong choice, the user will have the chance to return to the starting point.
# The story belongs to the creator of this text-based adventure game: Adem Ozdemir.


def main():
    import time
    # Import time is a module that provides many ways of representing time in code.

    def displayIntro():
        print('')
        time.sleep(3)
        print("Welcome to the apocalypse v1.0.0 text-based adventure game.")
        print('')
        # Time sleep functions are widely used in this work. It basically suspends the execution of the code for the given number of seconds.
        time.sleep(3)
        print("In this zombie apocalypse simulation, you have to trust your survival instincts and be try to be logical. Think about the choices provided and enter your answer. ")
        print('')
        time.sleep(3)
        print("After each situation, you'll have the chance to enter your answer, and depending on your answer you'll be alive or not. However, after each answer, if you've chosen the wrong path, you'll have the chance to return to the starting point. ")
        print('')
        print("Now, If you're ready, enter 'start' for the simulation to begin or 'quit' to exit: ")
        print('')
    displayIntro()
    choice_1 = input("Will you start the simulation?    ")
    if choice_1 == ('no'):
        time.sleep(1)
        print("You decided not to test your survival instincts. Remember, without fear life is meaningless.")
        return main()
    elif choice_1 == ('start'):
        print('')
        print("Simulation begins.")
        print('')
    else:
        print("Check your inputs. Use 'start' to start the simulation or 'no' to exit.")
        return main()
    while choice_1 == ('start'):
        time.sleep(1)
        print("While you were watching the evening news on TV, suddenly a last minute news was entered and you learned that the zombie invasion has begun, you immediately decided to grab your phone and call your best friend.")
        choice_2 = str(input(
            "'A': I'll make a plan to meet at any of us' house. 'B': Before the number of zombies increases, I will urgently make a plan to meet somewhere outside.   "))
        if choice_2 == ('A'):
            print('')
            time.sleep(1)
            print("You made a smart decision and met at someone's house.  ")
            print('')
            time.sleep(2)
            print("You are both nervous about the situations.  ")
            print('')
            print("What will you do now? ")
        elif choice_2 == ('B'):
            print('')
            print("You decided to meet outside, but you couldn't find each other because of the sudden booming phone networks and you became the prey of the zombies.")
            print('')
            time.sleep(1)
            print("You died.")
            print('')
            choice_2b = str(
                input("Do you want to start again? 'yes' to start "))
            if choice_2b == ('yes'):
                print("You've chosen 'yes'. Starting again. ")
                # Return main function, sends the user to the starting point.
                return main()
            else:
                print("Returning to the start. ")
                return main()
        else:
            # The else statements are for the users in case they type something which is not related to given options.
            print("'This wasn't even an option!. ")
            choice_2c = str(
                input("Do you want to start again? Check your inputs and type 'yes' to start "))
            if choice_2c == ('yes'):
                print("You've chosen 'yes'. Starting again.")
                return main()
            else:
                print("Returning to the start. ")
                return main()
        while choice_2 == ('A'):
            choice_3 = str(input(
                "'A': My decision is we shouldn't leave the house until morning comes up. 'B': Without wasting any time, I'll tell that we have to go out and get away from the city.   "))
            if choice_3 == ('A'):
                time.sleep(2)
                print(
                    "Your friend agreed with you and decided to stay until the morning.")
                print('')
                time.sleep(2)
                print("You woke up with the first rays of the sun.")
                time.sleep(2)
                print('')
                print("You realised you were trapped inside because of the increasing number of zombies outside the door until the morning and you died of hunger.")
                print('')
                choice_3b = str(
                    input("Do you want to start again? 'yes' to start "))
                if choice_3b == ('yes'):
                    print("You've chosen 'yes'. Starting again. ")
                    return main()
                else:
                    print("Returning to the start.")
                    return main()
            elif choice_3 == ('B'):
                print('')
                time.sleep(1)
                print("Your logic and instincts didn't let you fail.")
                print('')
                time.sleep(2)
                print("Your friend found the idea of to get away from the city good.")
                print('')
                time.sleep(3)
                print("Your friend is asking how will we go now?")
                print('')
            else:
                # Else statements are for the users in case they enter an answer which is not related to the provided options.
                print('')
                time.sleep(3)
                print(
                    "'I can't understand. What is wrong with you? Stop acting weird.' - Your friend")
                choice_3b = str(
                    input("Do you want to start again? 'yes' to start "))
                if choice_3b == ('yes'):
                    print("You have chosen 'yes'. Starting again. ")
                    return main()
                else:
                    print("Wrong input. Returning to the start.")
                    return main()
            choice_4 = str(input(
                "'A': We definitely need a car. We can steal one. 'B': We can escape with our bicycles.   "))
            if choice_4 == ('A'):
                print('')
                time.sleep(1)
                print("You got lucky and found your neigbours car with the keys on it.")
                print('')
                time.sleep(2)
                print("You're stuck in a traffic jam created by those trying to escape from the city and you couldn't escape from the zombies.")
                print("You died")
                print('')
                choice_4b = str(
                    input("Do you want to start again? 'yes' to start "))
                if choice_4b == ('yes'):
                    print("You've chosen 'yes'. Starting again. ")
                    return main()
                else:
                    print("Wrong input. Returning to the start.")
            elif choice_4 == ('B'):
                print('')
                time.sleep(1)
                print("'Uh. Smart choice.' - Your friend.")
                print('')
                time.sleep(2)
                print("You took a couple of important things with you.")
                print('')
                time.sleep(3)
                print("Where are we going now?")
                print('')
            else:
                print('')
                print("'Stop messing around. We gotta be fast!' -Your friend.")
                print('')
                time.sleep(1)
                print("Returning to the starting point again.")
                time.sleep(2)
                return main()
            choice_5 = str(input(
                "'A': We can go to a mountain house. 'B': I have heard the announcement on the radios that there is a safe place somewhere nearby. We'll go there.  "))
            if choice_5 == ('A'):
                time.sleep(1)
                print('')
                print("Great decision.")
                print('')
                time.sleep(1)
                print("A long way awaits you.")
            elif choice_5 == ('B'):
                print('')
                time.sleep(3.5)
                print("When you entered the safe zone, you realized that everyone who heard the announcement came there and turned into zombies. ")
                print('')
                time.sleep(1.5)
                print("It's too late to run away now.")
                print('')
                choice_5b = str(
                    input("Do you want to try again? 'yes' to start  "))
                if choice_5b == ('yes'):
                    print("You've chosen 'yes'. Starting again. ")
                    return main()
                else:
                    print("Wrong input. Returning to the starting point.")
                    return main()
            else:
                print('')
                print(
                    "'Wait, this isn't an option. OH ITS RIGHT BEHIND YOU!!' -Your friend")
                print('')
                time.sleep(3)
                print(
                    "Your incorrect and unrelated decisions wasted your time and resulted in your death.")
                print('')
                print("You died.")
                print('')
                choice_5c = str(
                    input("Do you want to try again? 'yes' to start "))
                if choice_5c == ('yes'):
                    print("You've chosen 'yes'.Starting again. ")
                    return main()
                else:
                    print("Wrong input. Returning to the starting point.")
                    return main()
            if choice_5 == ('A'):
                print('')
                time.sleep(2)
                print("Just before reaching to the mountain house, you decided to stock up on food for a month or two. You're passing by a small market and it looks like it has been looted. ")
                print('')
                time.sleep(3)
                print("What will you do?")
                print('')
            # For choice_6, there are 3 options for the user to choose from. Two of them will result in continuing to the adventure.
            choice_6 = str(input("'A': I suggest one of us go inside and be careful and quick whilst the other one keep watch on outside. 'B': I suggest we both go in at the same time. 'C': I suggest that the food we take with us is enough for now and hopefully we can find more in the mountain house. No need to stop.  "))
            if choice_6 == ('A'):
                print('')
                time.sleep(2)
                print(
                    "You decided to watch out and your friend decided to enter the market.")
                print('')
                time.sleep(1)
                print("While your friend is inside and you're outside alone and vulnerable, an unexpected zombie group has attacked and took down you both.")
                print('')
                print('You turned into a zombie.')
                print('')
                time.sleep(2)
                print('Simulation over.')
                print('')
                choice_6b = str(
                    input("Do you want to try again? 'yes' to start  "))
                if choice_6b == ('yes'):
                    print("You've chosen 'yes'. Starting again. ")
                    return main()
                else:
                    print("Returning to the starting point.")
                    return main()
            elif choice_6 == ('B'):
                print('')
                print("You have undeniable sense to make critique decisions. ")
                print('')
                time.sleep(2)
                print("Both of you has entered to the market.")
                print('')
                print(
                    "You made the correct choice and everything seems under control for now.")
                print('')
            elif choice_6 == ('C'):
                print('')
                print("You have chosen 'C'.")
                print('')
                time.sleep(2)
                print("Your friend agreed with you and you're continuing your way.")
                print('')
                print(
                    "'I hope we made the right decision. We better find some food left in the mountain house.' - Your Friend")
                print('')
                time.sleep(2)
                print("You have to respond to your friend:")
                print('')
                choice_6c = str(input(
                    "'A': Don't worry we'll get this through. 'B': You're talking too much! You're gonna get us killed! Shut up and move on or let's split and continue our ways like that. "))
                if choice_6c == ('A'):
                    print('')
                    time.sleep(0.7)
                    print(
                        "'Thanks man, feeling lucky to have you around. I trust you.' - Your friend")
                    print('')
                    time.sleep(2)
                    print(
                        "This little chat heightened both of yours morale. Both of you are now more confident. 'We will make it' - You")
                    print('')
                    time.sleep(3)
                    print("Against all odds you made it to the mountain house.")
                elif choice_6c == ('B'):
                    print('')
                    print(
                        "'What is wrong with you? What is this anger for? Okay. I'll be quiet but you'll regret.' - Your friend ")
                    print('')
                    time.sleep(2)
                    print(
                        "You damaged your relationship with your friend. This behaviour will cost you during the harder situations. ")
                    print('')
                    print("Against all odds you made it to the mountain house.")
                    print('')
                else:
                    print('')
                    print("Wrong OPTION CHOICE. Returning to the starting point.")
                    return main()
            else:
                print('')
                print("Wrong input. Returning to the start.")
                return main()
            if choice_6 == ('B'):
                time.sleep(3)
                print(
                    "You walked in at the same time. While checking the shelves, one of you noticed a zombie.")
                print('')
                time.sleep(4)
                print("You made a little plan and successfully neutralized the zombie.")
                print('')
                time.sleep(5)
                print(
                    "After getting enough food stock, you saw and checked the car standing next to the market.")
                print('')
                time.sleep(3)
                print("What will you do now? ")
                choice_6ba = str(input(
                    "'A': No need to risk. We'll continue to our ways with bicycles. 'B': The owner may be the zombie inside the grocery store, we'll take the risk again and go inside to check their pockets for the key.  "))
                if choice_6ba == ('A'):
                    print('')
                    time.sleep(2)
                    print(
                        "Just because you spent so much time in market, you didn't notice how has time passed .")
                    print('')
                    time.sleep(3)
                    print("However you decided not to take a risk and continue to your way with the food stocks on your bags, but since the time is late and the road is dark, you didn't notice the zombie group coming out of the forest on the way to the mountain house.")
                    print('')
                    time.sleep(4)
                    print(
                        "Since the bikes are defenseless, you fell down easily and became the prey of the zombies.")
                    print('')
                    time.sleep(1)
                    print("You died.")
                    choice_6bab = str(
                        input("Do you want to try again? 'yes' to start "))
                    if choice_6bab == ('yes'):
                        print("Starting again. ")
                        return main()
                    else:
                        print('')
                        print("Wrong input. Returning to the start.")
                        print('')
                        return main()
                elif choice_6ba == ('B'):
                    print('')
                    time.sleep(2)
                    print("If you don't risk anything, you risk even more.")
                    print('')
                    time.sleep(3)
                    print(
                        "'Bullseye! Keys are in his right pocket! I can't believe we got lucky this time' - Your friend")
                    print('')
                    time.sleep(4)
                    print("Your friend found the keys. You got in the car. You have a food stock that will be enough for at least 5 months. Everything is good except you are still hearing distant screams of innocent people. ")
                    print('')
                    time.sleep(5)
                    print(
                        "Against all odds, you made it to a village located next to the mountain house.")
                    print('')
                else:
                    print('')
                    print("Wrong input. Returning to the starting point. ")
                    print('')
                    return main()
            elif choice_6 == ('C'):
                if choice_6c == ('A'):
                    time.sleep(2)
                    print(
                        "You are about to enter a village located next to the mountain house.")
                    print('')
                    time.sleep(3)
                    print("You warned your friend to be quiet and calm.")
                    print('')
                    time.sleep(4)
                    print(
                        "'Nobody is around. They probably ran away after hearing the news.' - You")
                    print('')
                    time.sleep(4.5)
                    print("Your friend found an abondened mountain house. You suggested and decided to enter and your friend volunteered to keep watch on outside until you call him inside. ")
                    print('')
                    time.sleep(4)
                    print(
                        "Once you got in you noticed there isn't any food left around. ")
                    print('')
                    time.sleep(5)
                    print("Your friend offered to stay there for a day or two. ")
                    print('')
                    print("You agreed with your friend and decided to stay there. ")
                    print('')
                    time.sleep(5)
                    print(
                        "Since there isn't any food left by the villagers, you and your friend didn't last a week. ")
                    print("Simulation over. ")
                    print('')
                    choice_6ccc = str(
                        input("Do you want to try again? 'yes' to return "))
                    if choice_6ccc == ('yes'):
                        print("Starting again.")
                        return main()
                    else:
                        print('')
                        print("Returning to the start.")
                        return main()
            # The code here simply depends on the users choices. If both of the choice_6 and choice_6c are correct for the input by the user, then the statement will accept the code and continue.
            if choice_6 == ('C'):
                if choice_6c == ('B'):
                    time.sleep(1)
                    print(
                        "You're about to enter a village located next to the mountain house. ")
                    print('')
                    time.sleep(2)
                    print("You warned your friend to be quiet and calm. ")
                    print('')
                    time.sleep(3)
                    print(
                        "'Nobody is around. They probably ran away after hearing the news.' - You ")
                    print('')
                    time.sleep(4)
                    print(
                        "You realized your friend didn't even listened and responded to you and kept looking around. ")
                    print('')
                    time.sleep(5)
                    print(
                        "After a while your friend found an abondened mountain house, you suggested him to stay outside and you to enter. ")
                    print('')
                    time.sleep(5)
                    print("Your friend did not agree with you. 'No way I am going to stay outside while you're inside safe. I'm not a fool.' - Your friend ")
                    print('')
                    time.sleep(6)
                    print("You have to respond to your friend: ")
                    choice_6bb = str(input(
                        "'A': I think it's better to split up, you're not helping. 'B': What is wrong with you? "))
                    if choice_6bb == ('A'):
                        time.sleep(1)
                        print(
                            "'OH YEAH? WISE CHOICE. I'M USELESS. FROM NOW ON YOU'RE ON YOUR OWN.' - Your friend ")
                        print('')
                        time.sleep(2)
                        print("Your friend shouted so loud. Something is wrong. ")
                        print('')
                        time.sleep(3)
                        print(
                            "You noticed you weren't alone and heard sudden runnings of zombies towards you. ")
                        time.sleep(4)
                        print("'OH GOD! THEY'RE COMING! RUN! RUN!' - Your friend ")
                        print('')
                        time.sleep(5)
                        print("Your friend managed to find and enter a house and locked the door inside. All of a sudden, you saw a group of zombies coming towards you. You have to say something to your friend to open the door or you'll be dead within seconds: ")
                        print('')
                        choice_6bbb = str(input(
                            "'A': LET ME IN. IT'S HERE. WITHOUT ME YOU COULDN'T EVEN MAKE IT TO HERE! 'B': OPEN UP THE DOOR I'M SORRY!  "))
                        if choice_6bbb == ('A'):
                            print('')
                            time.sleep(2)
                            print("' I can't. I'm sorry.' - Your friend ")
                            print('')
                            print("You died")
                            time.sleep(3)
                            print(
                                "Your friend didn't open the door and managed to stay alive by escaping from the zombies but couldn't make it without the food stocks and died of hunger. ")
                            print('')
                            time.sleep(2.5)
                            print("Returning to the start. ")
                            return main()
                        elif choice_6bbb == ('B'):
                            print('')
                            time.sleep(2)
                            print(
                                "Not a smart move. Your friend decided to open the door and you instantly got in but couldn't resist a group of zombies pushing the door. ")
                            print('')
                            time.sleep(4)
                            print("This move resulted in both of yours death. ")
                            print('')
                            print("Returning to the start.")
                            print('')
                            return main()
                        else:
                            print("Wrong input. Returning to the start. ")
                            print('')
                            return main()
                    elif choice_6bb == ('B'):
                        print('')
                        time.sleep(1)
                        print("'Are you really asking this?' - Your friend ")
                        print('')
                        time.sleep(2)
                        print("You have to do something.")
                        choice_6bbh = str(input(
                            "'A': Say 'sorry' to your friend. Both of you are going through hard time. 'B': Say 'I have no time for these. We're splitting up and that's it.' "))
                        if choice_6bbh == ('A'):
                            print('')
                            time.sleep(2)
                            print(
                                "Your friend wants to split up. 'It'll be better like this' - Your friend. ")
                            print("You accepted the idea to split up.")
                            print('')
                            time.sleep(3)
                            print(
                                "After splitting up, you noticed you weren't alone in the village. It's too late to change things now. ")
                            print("Both of you has died.")
                            print('')
                            time.sleep(5)
                            print("Returning to the start.")
                            return main()
                        elif choice_6bbh == ('B'):
                            print('')
                            print(
                                "Your friend agreed with you and decided to split up. ")
                            print('')
                            time.sleep(3)
                            print(
                                "After splitting up you noticed you weren't alone in the village. It's too late to change things now.")
                            print("Both of you has died.")
                            return main()
                        else:
                            print("Wrong input. Returning to the start.")
                            print('')
                            return main()
                    else:
                        print("Wrong input. Returning to the starting point. ")
                        print('')
                        return main()
            if choice_6 == ('B'):
                if choice_6ba == ('B'):
                    # From now on there aren't any choices provided for the users. The simulation successfully ends here.
                    time.sleep(2)
                    print("You're about to enter a village located next to the mountain house. You gently parked the car and helped your friend carry the food stocks from the baggage. ")
                    print('')
                    time.sleep(5)
                    print("Your friend found an abondened house. Once you got in, you noticed there aren't any food left over. 'Such a smart path we've followed! We made it here!!' - Your friend. ")
                    print('')
                    time.sleep(5)
                    print("You noticed you weren't alone in the village. You told your friend to be quiet and calm and help you put a couple of things to cover the doors and windows. ")
                    print('')
                    time.sleep(6)
                    print("You've covered the doors and found a half-loaded weapon in the bedroom. You have a food stock that will be enough for at least 4 months and zombies can not notice you in the mountain house. Thanks to the right decisions you have made from the beginning, now you can hope that the apocalypse will pass within months. ")
                    print('')
                    time.sleep(7)
                    print("You've successfully completed the simulation. Your wise and cold blooded decisions has brought you here and you've managed to stay alive with your friend! ")
                    print('')
                    time.sleep(5)
                    print("Thank you for trying the simulation. ")
                    print('')
                    print(
                        "Now, if you want you can return to the starting point and try the other endings for fun! ")
                    # Last choice is for the users that successfully completed the simulation and wants to try out the other endings of the simulation.
                    choice_last = str(input(
                        "Do you want to see the other endings and choices? 'yes' in order to return to the starting point.  "))
                    if choice_last == ('yes'):
                        print('')
                        print(
                            "You've wanted to try the other endings. Returning to the starting point. ")
                        return main()
                    else:
                        print("Finishing the simulation. ")
                        # Return ending will basically send the user to the end of the code where it's not possible to input codes.
                        return ending

    displayIntro()


main()


def ending():
    ending
