# everything function imports
import json
import requests
from bs4 import BeautifulSoup


from flask import Flask

class recipe:
    
    def __init__(self, recipe_name, image, ingredients, instructions, link):
        self.recipe_name = recipe_name
        self.image = image
        self.ingredients = ingredients
        self.instructions = instructions
        self.link = link

class recipe_Final:

    def __init__(self, recipe_name, image_link, ingredients, instructions, link):
        self.recipe_name = recipe_name
        self.image_link = image_link
        self.ingredients = ingredients
        self.instructions = instructions
        self.link = link

def createBaseObject(link):
    return recipe("", "", "", "", link)

# def create_dict(specified_recipe):
#     specified_recipe_dict = {}
#     specified_recipe_dict[0] = specified_recipe.recipe_name
#     specified_recipe_dict[1] = specified_recipe.image_link
#     specified_recipe_dict[2] = specified_recipe.ingredients
#     specified_recipe_dict[3] = specified_recipe.instructions
#     specified_recipe_dict[4] = specified_recipe.link
#     return specified_recipe_dict

def everything(user_input):
    basis = "https://www.epicurious.com"
    recipe_object_array = []

    # tomato for testing
    html_source = requests.get("https://www.epicurious.com/search/" + user_input).text
    html = BeautifulSoup(html_source, 'lxml')
    link_headers = html.find_all('h4', class_="hed")

    actual_links = []
    recipe_names = []
    for link_header in link_headers:
        actual_links.append(link_header.a['href'])
        recipe_names.append(link_header.a.text)

    full_links = []
    for actual_link in actual_links:
        full_links.append(basis + actual_link)

    filtered_links = []
    filtered_recipe_names = []

    for i in range(0, len(full_links)):
        if(("recipes" in full_links[i]) and ("recipes-menus" not in full_links[i])):
            filtered_links.append(full_links[i])
            filtered_recipe_names.append(link_headers[i].a.text)


    for filtered_link in filtered_links:
        recipe_object_array.append(createBaseObject(filtered_link))

    for i in range(0, len(recipe_object_array)):
        recipe_object_array[i].recipe_name = filtered_recipe_names[i]

    for recipe_object in recipe_object_array:
        specific_recipe_page_request = requests.get(recipe_object.link).text
        specific_recipe_page_html = BeautifulSoup(specific_recipe_page_request, 'lxml')
        images = specific_recipe_page_html.find_all('img')
        recipe_object.image = images[1]

        ingredients = specific_recipe_page_html.find_all('div', class_="BaseWrap-sc-TURhJ BaseText-fFzBQt Description-dSNklj eTiIvU feJvcP")
        instructions = specific_recipe_page_html.find_all('div', class_="BaseWrap-sc-TURhJ BaseText-fFzBQt InstructionBody-hvjmoZ eTiIvU icSUzh fVMfdN")
        recipe_object.ingredients = ingredients
        recipe_object.instructions = instructions


    recipe_object_array_final = []


    for recipe_object in recipe_object_array:
        ingredients_as_one_string = ""
        instructions_as_one_string = ""
    

        for ingredient in recipe_object.ingredients:
            ingredients_as_one_string += ingredient.text

        for instruction in recipe_object.instructions:
            instructions_as_one_string += instruction.text

        recipe_object_array_final.append(recipe_Final(recipe_object.recipe_name, recipe_object.image['src'], ingredients_as_one_string, instructions_as_one_string, recipe_object.link))


    # for recipe_object in recipe_object_array_final:
    #     print(recipe_object.recipe_name)

    return recipe_object_array_final[0].recipe_name


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello" + str(everything())

        self.image_link = image_link
        self.ingredients = ingredients
        self.instructions = instructions
        self.link = link

def createBaseObject(link):
    return recipe("", "", "", "", link)

# def create_dict(specified_recipe):
#     specified_recipe_dict = {}
#     specified_recipe_dict[0] = specified_recipe.recipe_name
#     specified_recipe_dict[1] = specified_recipe.image_link
#     specified_recipe_dict[2] = specified_recipe.ingredients
#     specified_recipe_dict[3] = specified_recipe.instructions
#     specified_recipe_dict[4] = specified_recipe.link
#     return specified_recipe_dict

def everything(user_input):
    basis = "https://www.epicurious.com"
    recipe_object_array = []

    # tomato for testing
    html_source = requests.get("https://www.epicurious.com/search/" + user_input).text
    html = BeautifulSoup(html_source, 'lxml')
    link_headers = html.find_all('h4', class_="hed")

    actual_links = []
    recipe_names = []
    for link_header in link_headers:
        actual_links.append(link_header.a['href'])
        recipe_names.append(link_header.a.text)

    full_links = []
    for actual_link in actual_links:
        full_links.append(basis + actual_link)

    filtered_links = []
    filtered_recipe_names = []

    for i in range(0, len(full_links)):
        if(("recipes" in full_links[i]) and ("recipes-menus" not in full_links[i])):
            filtered_links.append(full_links[i])
            filtered_recipe_names.append(link_headers[i].a.text)


    for filtered_link in filtered_links:
        recipe_object_array.append(createBaseObject(filtered_link))

    for i in range(0, len(recipe_object_array)):
        recipe_object_array[i].recipe_name = filtered_recipe_names[i]

    for recipe_object in recipe_object_array:
        specific_recipe_page_request = requests.get(recipe_object.link).text
        specific_recipe_page_html = BeautifulSoup(specific_recipe_page_request, 'lxml')
        images = specific_recipe_page_html.find_all('img')
        recipe_object.image = images[1]

        ingredients = specific_recipe_page_html.find_all('div', class_="BaseWrap-sc-TURhJ BaseText-fFzBQt Description-dSNklj eTiIvU feJvcP")
        instructions = specific_recipe_page_html.find_all('div', class_="BaseWrap-sc-TURhJ BaseText-fFzBQt InstructionBody-hvjmoZ eTiIvU icSUzh fVMfdN")
        recipe_object.ingredients = ingredients
        recipe_object.instructions = instructions


    recipe_object_array_final = []


    for recipe_object in recipe_object_array:
        ingredients_as_one_string = ""
        instructions_as_one_string = ""
    

        for ingredient in recipe_object.ingredients:
            ingredients_as_one_string += ingredient.text

        for instruction in recipe_object.instructions:
            instructions_as_one_string += instruction.text

        recipe_object_array_final.append(recipe_Final(recipe_object.recipe_name, recipe_object.image['src'], ingredients_as_one_string, instructions_as_one_string, recipe_object.link))


    # for recipe_object in recipe_object_array_final:
    #     print(recipe_object.recipe_name)

    return recipe_object_array_final[0].recipe_name


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello" + str(everything())

