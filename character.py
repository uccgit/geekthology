# Basic Character Setup

name = raw_input("What is your name?")
health = 100
money = None
inventory = []

location = { 'store' :['content1', 'content2'],
             'cost'  :[1, 2],
             'introduction' :'This is the area', 
             'exit'  :'I am outta here'
}

stats = {
         'strength' :[5, 2, 3, 4],
         'max health' :health
 
         }

# print location['introduction']
# print location['exit']
# print stats

def look():
    """Look around"""
    print "You are looking at something"
    
def move():
    """Move the player Up Down East West"""
    print "You are moving here or there"
    
def pickup():
    """Player Picks Up Something"""
    pass

def use():
    """Player Uses Something"""
    pass

def talk():
    """Player Talks To Something"""
    pass

def die():
    """Player Dies"""
    pass




    
