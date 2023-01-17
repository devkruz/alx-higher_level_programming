import models.rectangle as Rec

class Test(Rec):
    pass


test = Test(3)
print(test.id)

class Testt(Test):
    def __init__(self, id):
        self.__idd = id * id
        Test.__init__(self, id)
    def getIDD(self):
        return self.__idd


testt = Testt(2)
print(testt.id)
print(testt.getIDD())
