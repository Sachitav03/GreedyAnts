from cgitb import reset
import requests
import urllib.request
from bs4 import BeautifulSoup
import json
from flask import Flask, render_template, jsonify, request, url_for

from flask_cors import CORS


app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route("/", methods=["POST", "GET"])
def search():
    userinput = (request.args.get('ingr'))
    #userinput = 'egg, milk, chocolate'

    #result = {"0": ""}
    #return jsonify(result)
    # ?????
        #pos
    #ingredients = request.form["ingredients"]
    #for debugging
    #print(ingredients)
    #if ingredients == "":
        # print("Error!") 
    #### S PROGRAM STARTS HERE ####
    basis = "https://www.epicurious.com"
    recipe_object_array = []

    class recipe:
        
        def __init__(self, recipe_name, image, ingredients, instructions, link):
            self.recipe_name = recipe_name
            self.image = image
            self.ingredients = ingredients
            self.instructions = instructions
            self.link = link
            

    def createBaseObject(link):
        return recipe("", "", "", "", link)


    html_source = requests.get("https://www.epicurious.com/search/" + userinput).text
    print(userinput)
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
    # for full_link in full_links:
    #     if(("recipes" in full_link) and ("recipes-menus" not in full_link)):
    #         filtered_links.append(full_link)



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

    class recipe_Final:

        def __init__(self, recipe_name, image_link, ingredients, instructions, link):
            self.recipe_name = recipe_name
            self.image_link = image_link
            self.ingredients = ingredients
            self.instructions = instructions
            self.link = link


    for recipe_object in recipe_object_array:
        ingredients_as_one_string = ""
        instructions_as_one_string = ""
        # before using .text have to include the index

        for ingredient in recipe_object.ingredients:
            ingredients_as_one_string += ingredient.text

        for instruction in recipe_object.instructions:
            instructions_as_one_string += instruction.text

        recipe_object_array_final.append(recipe_Final(recipe_object.recipe_name, recipe_object.image['src'], ingredients_as_one_string, instructions_as_one_string, recipe_object.link))

    # name is perfect
    # image_link is done
    # ingredients is done
    # instructions is done
    # link is done

    def create_dict(specified_recipe):
        specified_recipe_dict = {}
        specified_recipe_dict[0] = specified_recipe.recipe_name
        specified_recipe_dict[1] = specified_recipe.image_link
        specified_recipe_dict[2] = specified_recipe.ingredients
        specified_recipe_dict[3] = specified_recipe.instructions
        specified_recipe_dict[4] = specified_recipe.link
        return specified_recipe_dict

    for recipe_object in recipe_object_array_final:
        print(recipe_object.recipe_name)

    with open('test.json', 'w') as f:
        f.write("[")
        for recipe_object in recipe_object_array_final:
            json.dump(create_dict(recipe_object), f)
            if(recipe_object_array_final.index(recipe_object) != len(recipe_object_array_final) - 1):
                f.write(",")
            f.write("\n")
        f.write("]")
        #return test.json
    #return jsonify({"recipes": result})
    #result = ""
    print('AHHHHHHHHHHHHHHHH')
    f = open('test.json')
    result = json.load(f)
    print('AHHHHHHHHHHHHHHHH')
    print(result)
    f.close()

    for recipe in recipe_object_array_final:
        print(recipe.recipe_name)

    return jsonify(result) 
    


if __name__ == "__main__":
    app.run()
