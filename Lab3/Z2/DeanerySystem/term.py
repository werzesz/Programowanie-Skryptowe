from DeanerySystem.day import Day


class Term:
    derutation = 90
    def __init__(self, hour, minute,day, duraction = None):
        self.day = day      
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
      
        return self.hour < t.hour or (self.hour == t.hour and self.minute < t.minute)
    
    # >=
    def __ge__(self, t):
        return (self.hour == t.hour and self.minute >= t.minute) or (self.hour >= t.hour) 
    # 
    def __le__(self, t):
          return (self.hour == t.hour and self.minute <= t.minute) or (self.hour <= t.hour)
          
    def __sub__(self, t):
          
          
          return f"{t.hour}:{t.minute} [{60*(self.hour-t.hour-1)+self.minute+t.minute+t.duraction}]"
       #term1 = Term(8, 30),  term2 = Term(9, 45, 30) , term3 = Term(9, 45, 90)


class Lesson(Term):
    
    term = Term
    name = str(None)
    teacherName = str(None)
    year = 0
    full_time = bool(None)
    
    def __init__(self, term, name, teacherName, year, full_time):
        
        self.minute = term.minute 
        self.hour = term.hour
        self.day = term.day
        self.duraction = term.duraction
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.full_time = full_time
       
    

    def earlierTime(localTerm1):
    
        #STUDIA STACJONARNE
        
        if localTerm1.full_time == True:     
            #Jeślie pon-pt - cały tydzień początek o 8          
            localTerm2 = Term(8,0,Day.MON,90)


        #STUDIA NIESTACJONARNE
        else:
            #Jeśli pt
            if localTerm1.day.value == 5:
                localTerm2 = Term(17,0,Day.FRI,90)
            
            #Jeśli sob lub niedz
            elif localTerm1.day.value == 6 or localTerm1.day.value == 7:
                localTerm2 = Term(8,0,Day.FRI,90)
            else:
                return False
                

        a = localTerm1.duraction + localTerm1.minute
        while a >= 60:
            a = a - 60
            localTerm2.hour = localTerm2.hour + 1
        
        localTerm2.minute = a            
        
        return localTerm1 >= localTerm2

   
    
    def laterTime(localTerm1):
    
        #STUDIA STACJONARNE
        
        if localTerm1.full_time == True: 
            # PT 
            if localTerm1.day.value == 5:
                localTerm2 = Term(17,0,Day.FRI,90)
            
            # PN - CZW
            else:
                localTerm2 = Term(20,0,Day.MON,90)
              
        #STUDIA NIESTACJONARNE
        else: 
            # PT -ND
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




