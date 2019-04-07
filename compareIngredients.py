import logging
class compareIngredients:
    def __init__(self,available,detailedRecipe):
        logging.basicConfig(filename="compareIngredients.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        if available!='':
            self.availableIngredients=available.split(',')
        else:
            self.availableIngredients=[]
        self.recepieDetails=detailedRecipe

    def diff(self):
        self.logger.debug('diff entered')
        requiredIngredients=self.recepieDetails['ingredients']
        for i in range(len(requiredIngredients)):
            for j in range(len(self.availableIngredients)):
                if self.availableIngredients[j] in requiredIngredients[i]:
                    requiredIngredients[i] = ''
                    break
        return requiredIngredients