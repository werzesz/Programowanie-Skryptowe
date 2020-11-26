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
    duraction = 90
    def __init__(self, day, hour, minute):

        self.__day = Day(day).value
        self.minute = minute
        self.hour = hour

    def __str__(self):
        days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        return (f"{days[self._Term__day-1]} {self.hour}:{self.minute} [{Term.duraction}]")


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

    def minuteDifference(term1, term2):
        days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        hour1 = term1.hour
        minute1 = term1.minute
        hour2 = term2.hour 	
        minute2 = term2.minute
        
        
        if hour1 == hour2:
            x = minute1-minute2           
        else:
            x = 60*(hour2-hour1) -  minute1 + minute2


        time = x
        return (f"{days[term1._Term__day-1]} {hour1}:{minute1} [{time}]")


    def endTime(term):
        days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        endminute = term.duraction + term.minute
        endhour = term.hour
        
        while endminute >= 60:
            endhour = endhour + 1
            endminute = endminute - 60

        	
        return (f"{days[term._Term__day-1]} {endhour}:{endminute} [{Term.duraction}]")

def main():

    t1 = Term(Day.TUE, 9, 45)
    t2 = Term(Day.WED, 10, 15)

    term_1 = t1.minuteDifference(t2)
    print(term_1)
    term_2= t1.endTime()
    print(term_2)


if __name__ == '__main__':
    main()










