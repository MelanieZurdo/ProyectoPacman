import unittest

from Main.Model.Direction import Direction
class TestDirection(unittest.TestCase):

    def test_singleton(self):
        self.assertEqual(Direction.left(), Direction.left())
        self.assertNotEqual(Direction.left(),Direction.right())
        self.assertNotEqual(Direction.left(),Direction.down())
        self.assertNotEqual(Direction.left(),Direction.up())

        self.assertEqual(Direction.right(), Direction.right())
        self.assertNotEqual(Direction.right(),Direction.left())
        self.assertNotEqual(Direction.right(),Direction.down())
        self.assertNotEqual(Direction.right(),Direction.up())

        self.assertEqual(Direction.down(), Direction.down())
        self.assertNotEqual(Direction.down(),Direction.left())
        self.assertNotEqual(Direction.down(),Direction.right())
        self.assertNotEqual(Direction.down(),Direction.up())

        self.assertEqual(Direction.up(), Direction.up())
        self.assertNotEqual(Direction.up(),Direction.left())
        self.assertNotEqual(Direction.up(),Direction.right())
        self.assertNotEqual(Direction.up(),Direction.down())
       

            
   

    
if __name__ == '__main__':
    unittest.main()