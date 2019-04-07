
class compareIngredients:
    def __init__(self,available,detailedRecipe):
        self.availableIngredients=available.split(',')
        self.recepieDetails=detailedRecipe

    def diff(self):
        requiredIngredients=self.recepieDetails['ingredients']
        for i in range(len(requiredIngredients)):
            for j in range(len(self.availableIngredients)):
                if self.availableIngredients[j] in requiredIngredients[i]:
                    requiredIngredients[i] = ''
                    break
        return requiredIngredients
