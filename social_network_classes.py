# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list

    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self):
        #implement function that creates account here
        username = input("Enter your name: ")
        userage = input("Enter your age: ") 
        p1 = (self, username, userage)
        print("Creating ...")
        print("Welcome", username + "!")
        self.list_of_people.append(p1)
        pass

    def edit_details(self):
        #need to make function that changes all the values of p1 to this?? look at planning doc
        edit_name = input("Enter your new name: ")
        edit_age = input("Enter your new age: ")
        p1 = (self, edit_name, edit_age)
        print("Changing information ...")
        print("Account details changed")
        pass



class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.blocklist = []
    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        #person_object = input("Enter the name of the friend you want to add: ")
        self.friendlist.append(person_object)
        print("Adding ...")
        print(person_object + " is added as a friend!")
    def blocked(self, block_person):
        self.blocklist.append(block_person)
    def send_message(self):
        #implement sending message to friend here
        input("Please type your message: ")
        pass

    def messages(self):
        pass
