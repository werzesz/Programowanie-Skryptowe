import unittest
from term import Term
from term import Day


class Test(unittest.TestCase):
    #nie działa - jakoś dziwnie nakładają się zmienne 
    
    
    def testEndTime(self):
        self.assertEqual(term1.endTime(), 'Wtorek 11:15 [90]')
         
   
    def testMinuteDifference(self):
        self.assertEqual(term1.minuteDifference(term2), 'Wtorek 9:45 [30]')
    
   
  

if __name__ == '__main__':
    term1 = Term(Day.TUE, 9, 45)
    term2 = Term(Day.WED, 10, 15)
    unittest.main()
