# iRobot_Assignment
This repo consists of the assignment which is a part of the interview process for the cloud software team

## Manual: end user:
1. Goto the project forlder
2. to to dist
3. open the command line window
4. Run main.exe (windows: .\main.exe) 
5. Once asked, provide the names of the available ingredients seperated by spaces.
6. The result will be displayed in the window

1. To build executable for mac/linux, go to the directory with the main.py script, open the cmd, type: chmod +x main.py
2. Now, on the cmd, run the script by typing ./main.py

## Manual: internal:

### UML:

![alt text](https://github.com/swiftomkar/iRobot_Assignment/blob/master/uml.PNG)
### APIrequests.py:
1. This class is responsible to make all API requests to the food2fork API. 
2. The instantiation of an object of APIrequests type automatically loads data from the specified json file in the keys directory.
3. Once the file is loaded, it is available for all methods.
4. Each method of this class is responsible to make a single API request.
5. Currently it has 2 member functions; foodSearch and getRecipeDetails.
6. example: foodSearch
```python
session=APIrequests() 
if session.checkConnectivity():
    topRatedRecipeId=session.foodSearch('potato,cabbage,rice')
```
   This will return the recipe ID for the top rated recipe with the given ingredients as input parameters
7. Example: getRecipeDetails
```python
session=APIrequests() 
if session.checkConnectivity():
    recipeDetails=session.getRecipeDetails('xyZ123')
```
   This will return the details for recipe with the given recipe ID

### compareIngredients.py
1. This class is responsible to compare between user input and the suggested recipe.
2. In it's current state, It supports a diff function which creates a diff of the required ingredients minus the available ingredients.
3. Example:
```python
toCompare=compareIngredients(availIngredients,recipeDetails)
missingIngredients=toCompare.diff()
```

### main.py:
1. Main execution code responsible to take user input, make requests to the food2fork API and then generate the list of the missing recipes
2. main.py imports APIrequests and compareIngredients
3. This code is also responsible for providing the user with information in an organised and informative mannar.
4. In an ideal case, the API key should not be added to the repository and should be set as an env variable/input by the user. However, for convenience of execution, the API keys have been added to the repo here.


