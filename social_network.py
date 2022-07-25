#Various import Statements can go here
#from typing_extensions import Self
from  social_network_classes import SocialNetwork,Person
import social_network_ui


def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Sign into an account")
    print("4. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Send a message")
    print("6. <- Go back ")
    return input("Please Choose a number: ")

#Create instance of main social network object
ai_social_network = SocialNetwork()


#username = input("Enter your name: ")
#userage = input("Enter your age: ")
#current_user = (username, userage)

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the Create Account Menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "6":
                    break
                elif inner_menu_choice == "2":
                    print("You are now in the Add Friend Menu")
                    person_object = input("Enter the name of the friend you want to add: ")
                    print(person_object + " is now added as a friend!")
                    for person in ai_social_network.list_of_people:
                        if person.name == person_object:
                            current_user.add_friend(person_object)
                            break
                elif inner_menu_choice == "5":
                    #send_message = input("Type the message that you would like to send: ")
                    print("You are now in the Send Message Menu")
                    friend_name = input("Enter the name of the friend you want to send a message to: ")
                    print #your friends
                    for people in ai_social_network.list_of_people: #change the for loop "ai_social_network.list_of_people" to your friends list
                        if people == friend_name:
                            current_user.send_message(friend_name)

                    send_to_friend = input("Please type your message: ")
                    print("Your message was sent to " + friend_name)
                    break
                elif inner_menu_choice == "1":
                    print("\nYou are now in the Edit Details Menu")
                    #ai_social_network.edit_details()
                    edit_name = input("Enter your new name: ")
                    edit_age = input("Enter your new age: ")
                    print("\nChanging information ...")
                    print("Account details changed!")
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("You are now in the Sign-In Menu")
            login = input("Please enter the username of the account you would like to sign into: ")
            print("You are now signed in as " + login)
            for people in ai_social_network.list_of_people: 
                if people == person_object:
                    ai_social_network.current_user = found_person_object

        elif choice == "4":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
