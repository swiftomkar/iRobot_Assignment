#!/usr/bin/env python3
import APIrequests
import time
from compareIngredients import compareIngredients

if __name__=='__main__':
    print("Please provide all the ingredients available with you seperated by comas:")
    availIngredients=input()
    start=time.time()
    availIngredientsList=availIngredients.split(',')
    session=APIrequests.APIrequests()
    apiReqStart=time.time()
    topRatedRecipeId=session.foodSearch(availIngredients,'rating')
    recipeDetails=session.getRecipeDetails(topRatedRecipeId)
    totalAPIreqTime=time.time()-apiReqStart
    if recipeDetails:
        toCompare=compareIngredients(availIngredients,recipeDetails)
        missingIngredients=toCompare.diff()
        print("Here are the ingredients you will need to make",recipeDetails['name'],':')
        for i in missingIngredients:
            if i!='':
                print(i)
    totalTime=time.time()-start
    print("Total execution time including API calls:", totalTime,'s')
    print("Total execution time excluding API calls:", totalTime-totalAPIreqTime,'s')


