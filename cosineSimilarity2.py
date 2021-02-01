import math

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def get_cosine_similarity(f1,f2):

    wordlist=[]
    wordlist2=[]

    for word in f1.split():
         wordlist.append(word)


    for word in f2.split():
        wordlist2.append(word)

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    worddictionary2 = {}
    for word in wordlist2:
        if word in worddictionary2:
            worddictionary2[word] += 1
        else:
            worddictionary2[word] = 1

    # Create a combined dictionary
    # combined_dictionary = {}
    # all_word_set = set(worddictionary.keys()) | set(worddictionary2.keys())
    # for word in all_word_set:
    #     combined_dictionary[word] = [0,0]
    #     if word in worddictionary:
    #         combined_dictionary[word][0] = worddictionary[word]
    #     if word in worddictionary2:
    #         combined_dictionary[word][1] = worddictionary2[word]

    # wordlfreq=[]
    # wordlfreq2=[]
    # for word in combined_dictionary:
    #     wordlfreq.append(combined_dictionary.get(word)[0])
    #     wordlfreq2.append(combined_dictionary.get(word)[1])

    # print(worddictionary)
    # print(worddictionary2)
    # print(wordlfreq)
    # print(wordlfreq2)


    return get_cosine(worddictionary,worddictionary2)
