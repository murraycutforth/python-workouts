import unittest


def mysum(*args):
    result = args[0]
    for x in args[1:]:
        result += x
    return result

class TestMySum(unittest.TestCase):
    def test_small(self):
        x = mysum(1, 2, 3)
        self.assertEqual(x, 6)

    def test_large(self):
        x = mysum(*range(1, 100))
        self.assertEqual(x, 99 * 50)



if __name__ == "__main__":
    print(mysum("abc", "def"))
    print(mysum("abc"))
    unittest.main()



