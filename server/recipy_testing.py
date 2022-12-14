from flask import jsonify
import recipy
from requests_html import HTMLSession
import time
import os
import pandas as pd
import bcrypt
import json

# REMEMBER INSTALL DEPENDENCIES : pip install -r requirements.txt

# Use this file for testing calls of recipy functions.
# By running things here you are running the program entirely locally
# cd server
# Run with py recipy_testing.py

"""
Code attempts to follow javadoc style
This is a javadoc style.

@param param1: this is a first param
@param param2: this is a second param
@return: this is a description of what is returned
@raise keyError: raises an exception
"""

## Filter Testing ##
#  Filters out ingredients from ingredient portion
def filter_out_ingredients():
    return

## Filter Testing ##
#  Filters out ingredients from ingredient portion
def load_query():
    return



def simplyRecipes(query):

    session = HTMLSession()
    #Simplyrecipes = 'https://www.simplyrecipes.com/search?q=?'
    #Example Link: https://www.simplyrecipes.com/search?q=onion
    #
    #  Structure of Search
    # "https://www.simplyrecipes.com/search?q=" + query 
    #
    
    # Simplyrecipes.com Exploitation [INSERT UNDERHERE]

    ingredients = query
    ingredients = ingredients.split(sep=",")
    simplyRecipes_searchLink = recipy.build_link(ingredients,type="simplyrecipes")
    print(simplyRecipes_searchLink)
    #Inlude ingredients exploitation


    #test = session.get('https://www.simplyrecipes.com/search?q=onion')

    #print(test.html.links) 
    #prints all the links on a webpage

    test = session.get(simplyRecipes_searchLink)

    #recipe with lowercase is html element. 
    #Recipe with uppercase is data value.
    #  
    
    recipe_titles =test.html.find('.card__content') # List of recipe short titles
    print(len(recipe_titles))
    print(recipe_titles)
    recipe_descriptions =[""]*len(recipe_titles) # List of recipe short decriptions [NOT GIVEN IN Simplyrecipes.com]
    print(len(recipe_descriptions))
    print(recipe_descriptions)
    recipe_link =test.html.find('.comp card') # List of recipe links
    print(recipe_link)
    print("Break?")
    Recipe_TITLES = list()
    Recipe_DESCRIPTION = list()
    Recipe_LINK = list()
    Recipe_INGREDIENTS= list()
    Recipe_DIRECTIONS= list()
    #Tests list from allrecipe.com
    
    for i in range(len(recipe_titles)):
        start_time= time.time()
        #print("RECIPE TITLE")
        Recipe_TITLES.append(recipe_titles[i].text)
        #print("RECIPE DESCRIPTION")
        Recipe_DESCRIPTION.append(recipe_descriptions[i])
        #print("RECIPE LINK")
        Recipe_LINK.append(str(recipe_link[i].links)[2:-2])
        #print("INGREDIENTS")
        
        print(recipe_titles[i].text)
        print(recipe_descriptions[i])
        print((recipe_link[i].links)[2:-2]) 

        """#Enters a the website page that stores the websites
        sub_test=session.get(str(recipe_link[i].links)[2:-2]) 
        
        #Uses selector to parse out each ingredient with ".ingredients-item" class 
        ingredients = sub_test.html.find(".ingredients-item")
        for i in range(len(ingredients)):
            #ingredients stores all information
            ingredients[i]=ingredients[i].text
        Recipe_INGREDIENTS.append(ingredients)

       
        #finish_time = time.time()
        #selector val: .paragraph
        directions = sub_test.html.find(".paragraph")
        for i in range(len(directions)):
            #direction stores all information
            directions[i]=directions[i].text
        Recipe_DIRECTIONS.append(directions)"""
        #print("Took:"+str((finish_time-start_time))+" seconds")

#Enter Search Entry Here:
#ingredients ="onion,chicken"
#dict =recipy.query_sites(ingredients)

#simplyRecipes(ingredients)


#########################
##  Password Validation ##
#########################

# Test with  this sample user Jane Smith
user='Jane Smith'
password ='test'

# Test 1  Creates salt encrypted password. Decodes the hash. 
# Saves to a file. Run Read portion to read.

# WRITE PORTION
"""salt =bcrypt.gensalt()

encryted_pass = bcrypt.hashpw(password.encode('utf-8'),salt)
print(encryted_pass)

# decode as string and then encode
encryted_pass = encryted_pass.decode('utf-8')

# save as file in decoded form
with open("test.txt",'w') as f:
    f.write(encryted_pass)"""

# READ PORTION
"""
encryted_pass = open("test.txt",'r').read()
encryted_pass = encryted_pass.encode('utf-8')

# 
print("Password Check Valid Attempt")
print(bcrypt.checkpw(password.encode('utf-8'),encryted_pass))
print("Password Check Invalid Attempt")
print(bcrypt.checkpw("password".encode('utf-8'),encryted_pass))
"""

# https://www.makeuseof.com/encrypt-password-in-python-bcrypt/

print("userdata exists?")
print(recipy.userdata_exists())
if not recipy.userdata_exists():
    recipy.build_userdata()
if not recipy.access_userdata(user): # Check if user exists indata base
    recipy.add_user(user,password)
    
print("User Created?")
print(recipy.access_userdata(user))


print(recipy.get_password(user))

print("Password Check Valid Attempt")
print(recipy.login(user,password))
print("Password Check inValid Attempt")
print(recipy.login(user,"password"))

print("Should be true")
print(recipy.login(user,password))
print("Should be false")
print(recipy.login(user,'password'))
userdata=recipy.get_userdata(user,2)
print(userdata)

"""
#Paths to user data files
for file in userdata:
    print(os.path.join(recipy.build_user_path(user),file))
for i in range(3):
    print(get_userdata(user,i))
"""
#########################################
###  Loads Json data and converts it  ###
#########################################

# Ingredient Json loader

"""# Timing Start
start_time = time.time()
path=os.getcwd()
path=os.path.join(path,'datasets')
path=os.path.join(path,'ingredient_data2.json')
path= open(path)
ingredients= json.load(path)

#ingredients= pd.read_csv(path,encoding='latin-1')
#ingredients=ingredients.to_dict()
# Timing End
end_time = time.time()
print("Time taken to retrieve:")
print(end_time-start_time)

newdict = dict()
for ingredient in ingredients["Sheet1"]:
    newdict[ingredient['name'].strip()]= ingredient

with open("ingredient_data.json2", "w") as outfile:
    json.dump(newdict, outfile)"""
