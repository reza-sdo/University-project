# https://github.com/reza-sdo/University-project.git
# --------------------A-------------------
class FactorialRerouting:
    def __init__(self, userInput):
        self.userInput = userInput

    def Factorial(self):
        result = 1
        for i in range(1, self.userInput+1):
            result *= i
        print(result)
        return result



# --------------B------------
def oddnums(OOP):
    oddNumList = []
    for i in range(OOP):
        if i % 2 == 1:
            oddNumList.append(i)
    # print(oddNumList)
    return oddNumList

#------------------C------------


userInput = int(input("enter your number:"))

if userInput <= 6:
    print("you most enter number bigger than 6!")
else:
    if (userInput % 2) == 1:
        print("Please select an even number!")
    else:
        OOP = FactorialRerouting(userInput).Factorial()  #------A
        oddnums(OOP)                                     #------B
        







