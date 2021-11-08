a = list(map(int, input("Enter the list (use space to seperate): ").split())) 
n = int(input('Enter number to multiply: ')) 
print([n*i for i in a])


def wordList(arrayOfWords):
    outputArray = []

    for i, word1 in enumerate(arrayOfWords):
        for j, word2 in enumerate(arrayOfWords):
            if i == j:
                pass
            else:
                outputArray.append(word1+ " " +word2)

        return outputArray