input = [33,46,25,89,96,14,56,73,54,23]

#Find the pair of numbers that add up to 100


def findPair(params):
    number1 = 0
    number2 = 0

    for i in range(len(params)):
        for j in range(i + 1, len(params)):
            if (params[i] + params[j] == 100):
                number1 = params[i]
                number2 = params[j]
                return (number1,number2)


    return "No pairs found"


print(findPair(input))
