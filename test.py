import Classes.urlsSim as urlsim
listOfSimilarURl=[
    urlsim.urlsSim('1','2',0,0,0,0),
    urlsim.urlsSim('1','3',0,0,0,0),
    urlsim.urlsSim('5','3',0,0,0,0),
    urlsim.urlsSim('4','5',0,0,0,0),
    urlsim.urlsSim('6','7',0,0,0,0),
    urlsim.urlsSim('7','8',0,0,0,0),
    urlsim.urlsSim('1','9',0,0,0,0),
    urlsim.urlsSim('1','8',0,0,0,0),
    urlsim.urlsSim('1','8',0,0,0,0),
    urlsim.urlsSim('11','12',0,0,0,0),
    urlsim.urlsSim('13','14',0,0,0,0),

]

# 1,2,3,9,8,6,7
# 4,5


listSimilarity=[]
for i in range(len(listOfSimilarURl)):

    if len(listSimilarity)==0:
        listSimilarity.append([listOfSimilarURl[i].url1.strip(),listOfSimilarURl[i].url2.strip()])
    else:
        count=0
        currentItem=[]
        for item in listSimilarity:
           
            count1=0
            count2=0
            if listOfSimilarURl[i].url1.strip() in item:
                count1=count1+1
            if listOfSimilarURl[i].url2.strip() in item:
                count2=count2+1
        
            if count1>0 or count2>0:
                count=count+1
                if count>1 :
                    rang=range(len(item))
                    for v in rang:
                        x=item.pop()
                        if x not in currentItem:
                            currentItem.append(x)
                    #count=0
                    continue
                    
                currentItem=item
                if count1>0 and count2>0:
                    continue
                elif count1>0:
                    item.append(listOfSimilarURl[i].url2.strip())
                elif count2>0:
                    item.append(listOfSimilarURl[i].url1.strip())
                continue

                
        if count==0:
            listSimilarity.append([listOfSimilarURl[i].url1.strip(),listOfSimilarURl[i].url2.strip()])
    for item in listSimilarity:
        if len(item)==0:
            listSimilarity.remove(item)
#show urls group
print('-----------------')
for i in range(len(listSimilarity)):
    print("Similal group ",i+1," : ",listSimilarity[i])
    print('-----------------')
# print(len(listSimilarity))