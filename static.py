# staticmethod
class S:
    @ staticmethod
    def printgood(string):
        print("this="+string)
        return
S.printgood("hi")