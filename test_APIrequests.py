import unittest
from APIrequests import APIrequests

class testAPI(unittest.TestCase):
    def test_foodSearch(self):
        testSession=APIrequests()
        response=testSession.foodSearch('potato%20rice')
        self.assertEqual(response,'086443')

        response=testSession.foodSearch('chicken%20cheese')
        self.assertEqual(response,'e7fdb2')

    def test_getRecipeDetails(self):
        testSession = APIrequests()
        response = testSession.getRecipeDetails('086443')
        #print(response)
        self.assertEqual(response, {'ingredients': ['1 recipe for chipotle squash skewers', '1 cups cooked brown rice',\
                                                    ' tablespoon olive oil', '1 clove garlic', 'Juice from one lime',\
                                                    'Handful of fresh cilantro, roughly chopped.'], \
                                    'name': 'Chipotle Sweet Potato Skewers with Cilantro Lime Rice'}
                         )




if __name__=="__main__":
    unittest.main()