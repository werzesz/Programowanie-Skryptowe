import unittest

from DeanerySystem.term import Term
from DeanerySystem.term import Lesson
from DeanerySystem.day import Day

class Test_TestIncrementDecrement(unittest.TestCase):

    def testLaterTime(self):
        self.assertEqual(Lesson.laterTime(Lesson(Term(19, 35, Day.MON, 90), "Programowanie skryptowe", "Stanisław Polak", 2, True)), False)
        self.assertEqual(Lesson.laterTime(Lesson(Term(8, 35, Day.SUN, 90), "Programowanie skryptowe", "Stanisław Polak", 1, False)), True)
        
    def testEarlierDay(self):
        self.assertEqual(Lesson.earlierTime(Lesson(Term(19, 35, Day.TUE, 90), "Programowanie skryptowe", "Stanisław Polak", 2, True)), True)
        self.assertEqual(Lesson.earlierTime(Lesson(Term(8, 35, Day.SUN, 90), "Programowanie skryptowe", "Stanisław Polak", 1, False)), False)
        
    def testEarlierTime(self):
        self.assertEqual(Lesson.earlierTime(Lesson(Term(19, 35, Day.MON, 90), "Programowanie skryptowe", "Stanisław Polak", 2, True)), True)
        self.assertEqual(Lesson.earlierTime(Lesson(Term(8, 35, Day.SUN, 90), "Programowanie skryptowe", "Stanisław Polak", 1, False)), False)
        
    def testLaterDay(self):
        self.assertEqual(Lesson.laterDay(Lesson(Term(19, 35, Day.MON, 90), "Programowanie skryptowe", "Stanisław Polak", 2, True)), True)
        self.assertEqual(Lesson.laterDay(Lesson(Term(8, 35, Day.SUN, 90), "Programowanie skryptowe", "Stanisław Polak", 1, False)), False)
        
  



if __name__ == '__main__':
    unittest.main()
