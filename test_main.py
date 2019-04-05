import unittest
import main

class testMain(unittest.TestCase):
    def test_diff(self):
        diff=main.diff(['potato','cheese'],['potato','onion','bacon','cheese','celery'])
        self.assertEqual(diff,['','onion','bacon','','celery'])

        diff=main.diff(['potato'],['potato','onion','bacon','cheese','celery'])
        self.assertEqual(diff,['','onion','bacon','cheese','celery'])

        diff=main.diff([],['potato','onion','bacon','cheese','celery'])
        self.assertEqual(diff,['potato','onion','bacon','cheese','celery'])

        diff = main.diff([], [])
        self.assertEqual(diff, [])



if __name__=="__main__":
    unittest.main()
