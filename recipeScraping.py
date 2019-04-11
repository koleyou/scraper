# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:39:52 2019

@author: koley
"""

from bs4 import BeautifulSoup
import requests
import time
#allrecipes.com
allrecipespath = ['https://www.allrecipes.com/recipe/19205/chococonut-chip-cookies/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=9842%20referringContentType%3Drecipe','https://www.allrecipes.com/recipe/246841/spicy-lime-avocado-soup/?internalSource=streams&referringId=201&referringContentType=Recipe%20Hub&clickId=st_recipes_mades']
#path = 'https://www.allrecipes.com/recipe/255263/sicilian-roasted-chicken/?clickId=right%20rail1&internalSource=rr_feed_recipe_sb&referringId=9842%20referringContentType%3Drecipe'
#foodNetworkPath = 'https://www.foodnetwork.com/recipes/rachael-ray/macaroni-and-cheddar-cheese-recipe-2131153'
foodNetworkPath = ['https://www.foodnetwork.com/recipes/food-network-kitchen/pita-pizzas-recipe-1973601']
def recipeFormater(name, ingredients, directions):
    recipe = name + '\n-----------------------------------\n'
    recipe += 'Ingredients\n----------------------------------\n'
    for ingredient in ingredients:
        recipe += ingredient + '\n'
    recipe += '\nDirections\n------------------------------------\n'
    for direction in directions:
        recipe += direction +'\n\n'
    return recipe
def allRecipesScraper(paths):
    results = []
    for path in paths:
        source = requests.get(path).text
        soup = BeautifulSoup(source,'lxml')
        name = soup.find('h1',id='recipe-main-content').text.strip()
        ingredients = []
        for ingredient in soup.find_all('span',itemprop='recipeIngredient'):
            ingredients.append(ingredient.text.strip())
    
        directions = []
        for instruction in soup.find_all('span',class_='recipe-directions__list--item'):
            directions.append(instruction.text.strip())
        
        results.append(recipeFormater(name,ingredients,directions))
        time.sleep(1)
    return results
    
def foodNetworkScaper(paths):
    results = []
    for path in paths:
        source = requests.get(path).text
        soup = BeautifulSoup(source,'lxml')
        name = soup.find('section',class_='o-AssetTitle').h1.span.text.strip()
        ingredients = []
        for ingredient in soup.find_all('p',class_='o-Ingredients__a-Ingredient'):
            ingredients.append(ingredient.text.strip())
        directions = []
        for instruction in soup.find_all('li',class_='o-Method__m-Step'):
            directions.append(instruction.text.strip())
        
        results.append(recipeFormater(name,ingredients,directions))
        time.sleep(1)
    return results


for result in allRecipesScraper(allrecipespath):
    print(result)
#foodNetworkScaper(foodNetworkPath)
#path = 'https://www.epicurious.com/recipes/food/views/classic-chicken-pho-ph-ga'
#source = requests.get(path).text
#soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())