import string
def isValidValue(n):
    for i in n:
        if i not in string.digits:
            return False
    return True
def printFinal(name,domain):
    for i in range(len(name)):
        print("Username:%s and Domain:%s"%(name[i],domain[i]))
        print()
print("-----------------------")
print("WELCOME TO EMAIL SLICER")
print("-----------------------")
print()
n=input("How many emails do you want to get sliced: ")
name=[]
domain=[]
if isValidValue(n):
    if n=="0":
        print()
    else:
        '''this block input the emails and checks if they
        are valid emails or not after the input it slices
        the emails as name and domain and stores them '''
        for i in range(int(n)):
            email=input("Enter Email %d: "%(i+1))
            if "@" not in email:
                print("Sorry you did not enter a valid Email")
            else:
                name.append(email.split("@")[0])
                domain.append((email.split("@")[1]).upper())
        print()        
        print("After Slicing")
        print()
        printFinal(name,domain)
else:
    print()
    print("Sorry but U entered an Invalid value of number of emails")
    print()
print("-----------------------")
print("Thank You For Visiting ")
print("-----------------------")
            
