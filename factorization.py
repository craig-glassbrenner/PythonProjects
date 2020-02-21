"""
    Craig Glassbrenner
    CS461, Prime Factorization

    Given an integer greater than 1 this program will return a 
    string representation of what that number equals in terms of 
    its prime factorization.
"""
# Creates the prime factorization dictionary which holds on the info
# needed to create the string
def prime_factorization(a):
    factDict = {}
    i=2
    while( i*i <= a):
        repeatNum = 1
        while(a % i ==0):
            factDict[f'{i}'] = repeatNum
            repeatNum = repeatNum + 1
            a = a / i
        
        i = i + 1
    if(a > 1):
        factDict[f'{int(a)}'] = 1
        
    return factDict

# Creates the string based on the info based via the prime factorization
# dicitionary created in the above function.
def factor_string(b):
    dic = prime_factorization(b)
    keyList = list(dic.keys())
    lastKey = keyList[-1]
    
    toReturn = f"{b} = "
    for key, value in dic.items():
        if key == lastKey:
            if value == 1:
                toReturn = toReturn + f"{key}"
            else:
                toReturn = toReturn + f"{key}" + "^" + f"{value}"
        else:
            if value == 1:
                toReturn = toReturn + f"{key}" + " * "
            else:
                toReturn = toReturn + f"{key}" + "^" + f"{value}" + " * "
    
    return toReturn

def main():
    n = int(input("Enter a positive integer greater than 1: "))
    s = factor_string(n)
    print(s)
    
main()

