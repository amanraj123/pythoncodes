class TooYoung(Exception):
    def __init__(self,msg):
        self.msg = msg


class TooOld(Exception):
    def __init__(self,msg):
        self.msg = msg


age = int(input("enter no of age : "))
if age > 60:
    raise TooOld("wait some more time")
elif age < 18:
    raise TooYoung("why so late")
else:
    print("Thanks for registration")
