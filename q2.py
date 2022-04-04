class ClockTime:
    #default constructor
    def init(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    #set hours
    def setHours(self, hours):
        self.hours = hours
    #set minutes
    def setMinutes(self, minutes):
        self.minutes = minutes
    #set seconds
    def setSeconds(self, seconds):
        self.seconds = seconds
    #set time in hours minutes seconds
    def setTime(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    #prints out the time you set
    def showTime(self):
        print("%d:%d:%d" % (self.hours, self.minutes, self.seconds))

#prompts user to key in value for hour minutes and seconds
h = int(input("Enter value for hour: "))
m = int(input("Enter value for minutes: "))
s = int(input("Enter value for seconds: "))

#creates a clock object
object = ClockTime(h, m, s)

#sets the time
object.setTime(h, m, s)
object.showTime()


