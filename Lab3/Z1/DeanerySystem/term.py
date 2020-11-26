
from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


class Term:

    def __init__(self, hour, minute, duraction = None):
        self.minute = minute
        self.hour = hour

        if duraction is not None:
            self.duraction = duraction
        else:
            self.duraction = 90


    # <
    def __lt__(self, t):
        return self.hour < t.hour or (self.hour == t.hour and self.minute < t.minute)

    # ==
    def __eq__(self, t):
        return self.hour == t.hour and self.minute == t.minute and self.duraction == t.duraction

    # >
    def __gt__(self, t):
        return self.hour > t.hour or (self.hour == t.hour and self.minute > t.minute)

    # >=
    def __ge__(self, t):
        return self.hour >= t.hour or (self.hour == t.hour and self.minute >= t.minute)

    # <=
    def __le__(self, t):
          return self.hour <= t.hour or (self.hour == t.hour and self.minute <= t.minute)

    # -
    def __sub__(self, t):
          return f"{t.hour}:{t.minute} [{60*(self.hour-t.hour-1)+self.minute+t.minute+t.duraction}]"



    def __str__(self):
    
        return (f"{self.hour}:{self.minute} [{self.duraction}]")


    def earlierThan(self, termin):

        if self._Term__day < termin._Term__day:
            return True
        elif self._Term__day == termin._Term__day:
            if self.hour < int(termin.hour):
                return True
            elif self.hour == int(termin.hour):
                if self.minute < int(termin.minute):
                    return True
        else:
            return False


    def laterThan(self, termin):

        if self._Term__day > termin._Term__day:
            return True
        elif self._Term__day == termin._Term__day:
            if self.hour > int(termin.hour):
                return True
            elif self.hour == int(termin.hour):
                if self.minute > int(termin.minute):
                    return True
        else:
            return False


    def equals(self, termin):

        if self.hour == int(termin.hour) and self.minute == int(termin.minute) and self._Term__day ==termin._Term__day:
            return True
        else:
            return False

    def minuteFifference(self, term):
        days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

        if self.hour == int(termin.hour):
            Term.derucation = self.minute-int(termin.minute)
       
        else:
            Term.derucation = 60*self.hour-int(termin.hour)+self.minute-int(termin.minute)

        
        return (f"{days[self._Term__day-1]} {self.hour}:{self.minute} [{Term.duraction}]")

    def endTime():
        if Term.derutation > 60:
            self.hour = self.hour + 1
            self.minute = self.minute + derutation








