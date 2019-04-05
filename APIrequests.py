import requests
import json
#The APIrequests class is responsible for making the web requests to the provided API. As soon as an object of this
#type is instantiated, the API URL's and credentials are loaded into the memory to be used by member funtions.
#Here, self.config_obj contains the dictionary with URL's and the API key.
class APIrequests:
    def __init__(self):
        self.config = open('keys/foodtofork.json', 'r')
        self.config_obj = json.load(self.config)
    #takes available ingredients as an input string and returns the recipe ID of the top rated recipe
    #which contains the ingredients
    def foodSearch(self,ingredients):
        uriString=self.config_obj['searchUri']+'?'+'key='+self.config_obj['apiKey']+'&'+'q='+ingredients+'&'+'sort=r'
        recipes=requests.get(uriString)
        if not(200<=recipes.status_code<300):
            print("Response code was not 2xx, was {}".format(recipes.status_code))
        else:
            if len(recipes.json()['recipes'])>0:
                recipe_id=recipes.json()['recipes'][0]['recipe_id']
                return recipe_id
            else:
                print('No matching recipe found')
    #Takes recipe ID as an input and provides complete details about the recipe includng ingredients, name, publisher etc
    #Here only the name and ingredients list is returned as they are used to provide the user with the missing ingredients info
    def getRecipeDetails(self,recipe_id):
        if recipe_id:
            uriString = self.config_obj['recepieUri']+'?'+'key='+self.config_obj['apiKey']+'&'+'rId='+str(recipe_id)
            response = requests.get(uriString)
            if not (200 <= response.status_code < 300):
                print("Response code was not 2xx, was {}".format(response.status_code))
            else:
                return {'ingredients': response.json()['recipe']['ingredients'],
                        'name':response.json()['recipe']['title']
                        }