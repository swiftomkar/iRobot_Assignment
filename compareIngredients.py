
class compareIngredients:
    def __init__(self,available,required):
        self.availableIngredients=available.split(',')
        self.requiredIngredients=required['ingredients']

    def diff(self):
        for i in range(len(self.requiredIngredients)):
            for j in range(len(self.availableIngredients)):
                if self.availableIngredients[j] in self.requiredIngredients[i]:
                    self.requiredIngredients[i] = ''
                    break
        return self.requiredIngredients
