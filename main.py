#!/usr/bin/env python
import APIrequests
import time

def diff(availabelIngredients,requiredIngredients):
    for i in range(len(requiredIngredients)):
        for j in range(len(availabelIngredients)):
            if availabelIngredients[j] in requiredIngredients[i]:
                requiredIngredients[i]=''
                break
    return requiredIngredients
if __name__=='__main__':
    print("Please provide all the ingredients available with you seperated by comas:")
    availIngredients=input()
    start=time.time()
    availIngredientsList=availIngredients.split(',')
    availIngredients=availIngredients.replace(',','%20')
    session=APIrequests.APIrequests()
    apiReqStart=time.time()
    topRatedRecipeId=session.foodSearch(availIngredients,'rating')
    recipeDetails=session.getRecipeDetails(topRatedRecipeId)
    totalAPIreqTime=time.time()-apiReqStart
    if recipeDetails:
        missingIngredients=diff(availIngredientsList,recipeDetails['ingredients'])
        print("Here are the ingredients you will need to make",recipeDetails['name'],':')
        for i in missingIngredients:
            if i!='':
                print(i)
    totalTime=time.time()-start
    print("Total execution time including API calls:", totalTime,'s')
    print("Total execution time excluding API calls:", totalTime-totalAPIreqTime,'s')
    while True:
        time.sleep(1)


