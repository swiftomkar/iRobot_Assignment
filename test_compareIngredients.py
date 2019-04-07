import unittest
from compareIngredients import compareIngredients

class testMain(unittest.TestCase):
    def test_diff(self):

        obj1=compareIngredients('potato,cheese',{"ingredients":['potato','onion','bacon','cheese','celery']})
        diff1=obj1.diff()
        self.assertEqual(diff1,['','onion','bacon','','celery'])

        obj2=compareIngredients('potato',{"ingredients":['potato','onion','bacon','cheese','celery']})
        diff2=obj2.diff()
        self.assertEqual(diff2,['','onion','bacon','cheese','celery'])

        obj3=compareIngredients('',{"ingredients":['potato','onion','bacon','cheese','celery']})
        diff3=obj3.diff()
        #print(diff3)
        self.assertEqual(diff3,['potato','onion','bacon','cheese','celery'])

        obj4 = compareIngredients('', {"ingredients": []})
        diff4 = obj4.diff()
        self.assertEqual(diff4, [])



if __name__=="__main__":
    unittest.main()
