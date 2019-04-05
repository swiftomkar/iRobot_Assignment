# iRobot_Assignment
This repo consists of the assignment which is a part of the interview process for the cloud software team

##Manual: end user:
1. 

##Manual: internal:

###APIrequests.py:
1. This class is responsible to make all API requests to the food2fork API. 
2. The instantiation of an object of APIrequests type automatically loads data from the specified json file in the keys directory.
3. Once the file is loaded, it is available for all methods.
4. Each method of this class is responsible to make a single API request.
5. Currently it has 2 member functions; foodSearch and getRecipeDetails.
6. example: foodSearch
```python
session=APIrequests() 
topRatedRecipeId=session.foodSearch('potato%20cabbage%20rice')
```
   This will return the recipe ID for the top rated recipe with the given ingredients as input parameters
7. Example: getRecipeDetails
```python
session=APIrequests() 
recipeDetails=session.getRecipeDetails('xyZ123')
```
   This will return the details for recipe with the given recipe ID

###main.py:
1. Main execution code responsible to take user input, make requests to the food2fork API and then generate the list of the missing recipes
2. main.py imports APIrequests
3. This code is also responsible for providing the user with information in an organised and informative mannar.
4. The diff function:
```python
diff=main.diff(['potato','cheese'],['potato','onion','bacon','cheese','celery'])
```
5. This function returns a list with the available ingredients replaced with an empty string ""

