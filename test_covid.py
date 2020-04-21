import unittest
import covid

class TestCovid(unittest.TestCase):
    def test_read_csv(self):
        res = covid.read_csv('covid.csv')
        self.assertEqual(len(res), 2564)

    def test_get_value(self):
        data = [{'name':

if __name__ == '__main__':
    unittest.main()
else:
    print('loading')
