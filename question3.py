# PART 1:
# You've freed a number of aliens from captivity, and now need some way to classify them
# Define a class, "alien", with 5 attributes: a name, eye color, antennae number, number of arms, and
# a list of the other aliens they've befriended
#The aliens should have:
#    A) A method to befriend other aliens:
#       def befriend(self,a): accepts another alien as an argument and adds them to a list of friends
#    B) A method to change eye, antenna, and arm characteristics
#         def metamorphosis(self,new_eye,new_ant,new_arm): changes alien physical attributes
#        NOTE: eye color can only be one of the following: ['green','blue','red','yellow','purple']
#        NOTE: Aliens may only have up to 10 antenna and 20 arms

#    C) A method to translate a string to aliens (aliens speak backwards)
#       def translate(self,string): translates string into the aliens language for them to speak i.e., reverse string
#
#    D) A method that returns the list of friends
#    def getfriends(self): returns the list of friends

class alien:
    def __init__(self,name,eye_color,antennae_number,number_of_arms,befriended):
        self.name = name
        self.eye_color = eye_color
        self.antennae_number = antennae_number
        self.number_of_arms = number_of_arms
        self.befriended = befriended
    def befriend(self,a):
        self.befriended.append(a)
    def metamorphosis(self,new_eye,new_ant,new_arm):
        if new_eye != 'green' or new_eye != 'blue' or new_eye != 'red' or new_eye != 'yellow' or new_eye != 'purple':
            return -1
        if new_ant > 10:
            return -1
        if new_arm > 20:
            return -1
        self.eye_color = new_eye
        self.antennae_number = new_ant
        self.number_of_arms = new_arm
    def translate(self,string):
        n = ""
        for i in string:
            n = i + n
        return n

    def getfriends(self):
        return self.befriended

# PART 2: Define a function called ALIENS which receives three parameters: alien1, alien2 and a message and performs the following actions
#   A) Befriends the two aliens, and checks their friendship
#   B) Makes alien1 translates the message parameter
#   C) Returns the alien1, alien2 and the translated message

# ALIENS function
def ALIENS(a1,a2,message):
    a1.befriend(a2)
    a2.befriend(a1)
    trans = a1.translate(message)
    return a1, a2, trans

# Write a function called change which takes the following parameters: alien, eye color, antennae_num, arms_num and changes the characteristics of the alien based on the previous parameters
# the funtion returns the changed alien

def change(alien1, eye_col, antennae_num, arms_num):
    alien1.metamorphosis(alien1.name, eye_col, antennae_num, arms_num)
    return alien1
