import math
#
# PROBLEM #1
#

var = '010000000111111010111001'
#010000000111111010111001

#If string is less than 64 digits long add 0s until it reaches 64
if len(var) < 64:
    i = len(var)
    while i < 64:
        var = var + '0'
        i = i+1



#Find S to check for negative or positive based on first digit
if var[0] == '0':
    s = 0
else:
    s = 1

#Finding c using the next 11 digits
#t keeps track of which iteration the for loop is on
t = 0
t2 = 0
c = 0
f = 0
for i in var:
    #skip first number
    if t != 0:
        if var[t] == '1':
            if t < 12:
                c = c + ((1*(2**((10-t+1)))))
            else:
                t2 = t2 + 1
                f = f + pow(.5, t2)
        elif t > 11:
            t2 = t2 + 1
    t = t+1

final = (pow(-1, s))*(pow(2, (c-1023)))*(1+f)
print(final)
print('')

#
# PROBLEM #2
# 
    
#Convert to Normalized form
finalString = str(final)
t = 0
normString = ''
decimalSpot = 9999999
for i in finalString:
    
    if finalString[t] == '.':
        decimalSpot = t
    t = t+1

t = 0
for i in finalString:
    if t == 0:
        normString = normString + '.'
        normString = normString + finalString[t]
    elif t == (decimalSpot):
        t = t+1
        normString = normString + finalString[t]
    elif t == len(finalString):
        exit
    else:
        normString = normString + finalString[t]
    
    t = t+1
exponentNum = decimalSpot

#With the now normalized string 'normString' perform 3 digit chop
chopNum = 3
chopStr = ''
for i in range(0, len(normString)):
    if i < (chopNum + 2): #+1 for decimal, +1 extra for rounding purposes
        chopStr = chopStr + normString[i]

#Unnormalize?
blankString = ''
t=0
for i in range(0, len(chopStr)-1):
    if t == 0:
        blankString = blankString + chopStr[1] #skip decimal
    elif t == 1:
        blankString = blankString + '.'
    else:
        blankString = blankString + chopStr[t]
    t = t+1
choppedStr = float(blankString)
print(choppedStr/10)
print('')

#
# PROBLEM #3
#
#Take the normalized string and round instead

roundNum = 3
roundStr = chopStr
doWeRound = 0

if roundStr[roundNum+1] == '5' or '6' or '7' or '8' or '9': 
    doWeRound = 1
    cutStr = roundStr[0:4]
        

#convert string number to integer number so that we can add with it again
#which is useful for rounding
numCut = float(cutStr)
if doWeRound == 1:
    numCut = numCut + (pow(10, ((-1)*(roundNum))))
    numm = float(numCut)
    print(numm)
print('')

#
# PROBLEM #4
#

#Computer absolute and relative error with answer from #1 and #3
properAnswer = float(final)/1000
roundedAnser = numCut

#normalize both
#find absolute error
absErr = properAnswer - roundedAnser
if absErr < 0:
    absErr = absErr * (-1)
print(absErr)

#find relative error
relErr = absErr/properAnswer
print(relErr)
print('')

#
# PROBLEM #5
#

#Compute min num of items needed to compute f(1) with error less than 10^(-4)

#infinite series function is:
k = 1
x = 1

#view the first few terms of the series
while(k<6):
    seriesfunc = pow(-1, k)*(pow(x, k)/pow(k, 3))
    #print(seriesfunc)
    k = k + 1

#evalFunc = 1/(pow((n+1),3))
errorTol = pow(10, 4)
step1 = pow(errorTol, (1/3))
step2 = step1 - 1
ans = step2
#Round up answer to nearest whole number
strAns = str(ans)
roundUp = 0
for i in range(0, len(strAns)):
    if strAns[i] == '.':
        if strAns[i+1] == '5' or '6' or '7' or '8' or '9':
            roundUp = 1


if roundUp == 1:
    ans = ans + 1
    

strAns = str(ans)
finalStrAns = ''
ext = 0
for i in range(0, len(strAns)):
    
    if strAns[i] == '.':
        ext = 1
        
    if ext == 1:
        exit
    else:
        finalStrAns = finalStrAns + strAns[i]
        
print(finalStrAns)
print('')

#
# PROBLEM #6
#

#Determine number of iterations needed to solve f(x) = x^3 + 4x^2 - 10 = 0
#with accuracy 10^-4, using a = -4 and b=7
#A) Using the bisection method
#B) Using the newton Raphson method

#bisection formula
a = -4
b = 7
#n = 'n'
#form1 = (b-a)/(pow(2, n))4
errTol = pow(10, -4)
n = (4 + math.log(11, 10))/math.log(2, 10)
strn = str(n)
roundUp = 0
for i in range(0, len(strn)):
    if strn[i] == '.':
        if strn[i+1] == '5' or '6' or '7' or '8' or '9':
            roundUp = 1
if roundUp == 1:
    n = n+1
fstrn = str(n)
finalN = ''
ext = 0
for i in range(0, len(fstrn)):
    if fstrn[i] == '.':
        ext = 1
        
    if ext == 1:
        exit
    else:
        finalN = finalN + fstrn[i]


print(finalN)
print('')


#Newton Raphson 
initAprox = 1.2
iterations = 0

equ = (pow(x, 3))+(4*pow(x,2))-10
derv = 3*(pow(x, 2))+(8*x)

form1 = equ/derv
approximation = initAprox - form1
if approximation < 0:
    approximation = approximation * -1



while(abs(form1) > errTol):
    x = initAprox
    equ = (pow(x, 3))+(4*pow(x,2))-10
    derv = 3*(pow(x, 2))+(8*x)
    form1 = equ/derv
    initAprox = initAprox - form1
    iterations = iterations + 1
    
print(iterations)










