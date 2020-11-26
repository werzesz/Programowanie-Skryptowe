from DeanerySystem.day import Day
#from DeanerySystem.day import Day

class Term:
    derutation = 90
    
    def __init__(self, hour, minute,day, duraction = None):
        self.__hour = hour
        self.__minute = minute
        self.__day = day
        

        if duraction is not None:         # Gdy nie podamy długości zajęć tworzoąc klasę 
            self.duraction = duraction
        else:
            self.duraction = 90


############## 
    def set_hour(self, hour):
        self.__hour = hour
    
    def get_hour(self):
        return self.__hour

    def set_minute(self, minute):
        self.__minute = minute
    
    def get_minute(self):
        return self.__minute

    def set_day(self, day):
        self.__day = day
    
    def get_day(self):
        return self.__day

    def set_duraction(self, duraction):
        self.__duraction = duraction
    
    def get_duraction(self):
        return self.__duraction
##############



    # <
    def __lt__(self, t):
        return self.hour < t.hour or (self.hour == t.hour and self.minute < t.minute)

    # ==
    def __eq__(self, t):
        return self.hour == t.hour and self.minute == t.minute and self.duraction == t.duraction

    # >
    def __gt__(self, t):     
        return self.hour < t.hour or (self.hour == t.hour and self.minute < t.minute)
    
    # >=
    def __ge__(self, t):
        return (self.hour == t.hour and self.minute >= t.minute) or (self.hour >= t.hour) 

    # <=
    def __le__(self, t):
          return (self.hour == t.hour and self.minute <= t.minute) or (self.hour <= t.hour)

    # -       
    def __sub__(self, t):       
          return f"{t.hour}:{t.minute} [{60*(self.hour-t.hour-1)+self.minute+t.minute+t.duraction}]"
      

class Lesson(Term):
    
    term = Term
    name = str(None)
    teacherName = str(None)
    year = 0
    full_time = bool(None)
    
    def __init__(self, term, name, teacherName, year, full_time):
        
        self.__minute = term._Term__minute 
        self.__hour = term._Term__hour
        self.__day = term._Term__day
        self.__duraction = term.duraction
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__full_time = full_time

##################               
    
    def set_term(self, term):
        self.__minute = term.minute 
        self.__hour = term.hour
        self.__day = term.day
        self.__duraction = term.duraction

    def get_term(self):
        return self.__hour, self.__minute, self.__day, self.__duraction

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_teacherName(self, teacherName):
        self.__teacherName = teacherName
    
    def get_teacherName(self):
        return self.__teacherName
  
    def set_year(self, year):
        self.__year = year
    
    def get_year(self):
        return self.__year

    def set_full_time(self, full_time):
        self.__full_time = full_time
    
    def get_full_time(self):
        return self.__full_time

###################

    #Dziedziczymy przeciążoną funkcje >=  

    def earlierTime(localTerm1):
        #STACJONARNE
        if localTerm1.full_time == True:     
            #Jeślie pon-pt - cały tydzień początek o 8
          
            localTerm2 = Term(8,0,Day.MON,90)


        #NIESTACJONARNE
        else:
            #Jeśli pt
            if localTerm1.day.value == 5:
                localTerm2 = Term(17,0,Day.FRI,90)
            
            #Jeśli sob lub niedz
            elif localTerm1.day.value == 6 or localTerm1.day.value == 7:
                localTerm2 = Term(8,0,Day.FRI,90)
            else:
                return 0 # Poprawić na (jakiś break)

        a = localTerm1.duraction + localTerm1.minute
        while a >= 60:
            a = a - 60
            localTerm2.hour = localTerm2.hour + 1
        
        localTerm2.minute = a            
        
        return localTerm1 >= localTerm2

    #Dziedziczymy przeciążoną funkcje <= 
    def laterTime(localTerm1):
        #STACJONARNE
        if localTerm1.full_time == True: 
            #Jelśli pt 
            if localTerm1.day.value == 5:
                localTerm2 = Term(17,0,Day.FRI,90)
            
            #Jeśli pn-czw
            else:
                localTerm2 = Term(20,0,Day.MON,90)
              
        #NIESTACJONARNE
        else: 
            #Jeśli pt-nd
            localTerm2 = Term(20,0,Day.FRI,90)

        a = localTerm1.duraction + localTerm1.minute

        while a >= 60:
            a = a - 60
            localTerm1.hour = localTerm1.hour + 1
        
        localTerm1.minute =  a            
        return localTerm1 <= localTerm2

    def earlierDay(localTerm1):
        #STACJONARNE
        if localTerm1.full_time == True: 
            if localTerm1.day.value > 1 and localTerm1 <= 5:
                return True
            else:
                return False

        #NIESTACJONARNE
        else: 
            if localTerm1.day.value > 5 and localTerm1.day.value <= 7:
                return True
            else:
                return False


    def laterDay(localTerm1):
        #STACJONARNE
        if localTerm1.full_time == True: 
            if localTerm1.day.value >= 1 and localTerm1.day.value < 5:
                return True
            else:
                return False

        #NIESTACJONARNE
        else: 
            if localTerm1.day.value >= 5 and localTerm1.day.value < 7:
                return True
            else:
                return False



