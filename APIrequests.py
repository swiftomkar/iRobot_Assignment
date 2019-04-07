import requests
import json
import logging
#The APIrequests class is responsible for making the web requests to the provided API. As soon as an object of this
#type is instantiated, the API URL's and credentials are loaded into the memory to be used by member funtions.
#Here, self.config_obj contains the dictionary with URL's and the API key.
class APIrequests:
    def __init__(self):
        logging.basicConfig(filename="APIrequests.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.config = open('keys/foodtofork.json', 'r')
        self.config_obj = json.load(self.config)
        self.config.close()
    #takes available ingredients as an input string and returns the recipe ID of the top rated recipe
    #which contains the ingredients
    def foodSearch(self,ingredients,sortBy):
        ingredients=ingredients.replace(',','%20')
        uriString=self.config_obj['searchUri']+'?'+'key='+self.config_obj['apiKey']+'&'+'q='+ingredients+'&'+'sort='+sortBy[0]
        recipes=requests.get(uriString)
        if not recipes.status_code==200:
            print('There was some error')
            print("Response code was not 2xx, was {}".format(recipes.status_code))
            self.logger.error("Response code was not 2xx, was {}".format(recipes.status_code))
        else:
            if len(recipes.json()['recipes'])>0:
                recipe_id=recipes.json()['recipes'][0]['recipe_id']
                return recipe_id
            else:
                print('No matching recipe found, maybe check for typos?')
                self.logger.error('No matching recipes found for given combination of ingredients')
    #Takes recipe ID as an input and provides complete details about the recipe includng ingredients, name, publisher etc
    #Here only the name and ingredients list is returned as they are used to provide the user with the missing ingredients info
    def getRecipeDetails(self,recipe_id):
        if recipe_id:
            uriString = self.config_obj['recepieUri']+'?'+'key='+self.config_obj['apiKey']+'&'+'rId='+str(recipe_id)
            response = requests.get(uriString)
            if not response.status_code==200:
                print('There was some error')
                self.logger.error("Response code was not 2xx, was {}".format(response.status_code))
            else:
                return {'ingredients': response.json()['recipe']['ingredients'],
                        'name':response.json()['recipe']['title'],
                        'responseBody':response.json()
                        }