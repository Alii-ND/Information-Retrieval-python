# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
from pickle import load
import urllib.parse
from cosineSimilarity2 import get_cosine_similarity
import Classes.urlsSim as urlsim
import Classes.URL as url
import databaseHandler as dbHandler


def getPrediction(query):
    db = dbHandler.databaseHandler()
    #get data from data base (urls of query)
    listURL=db.get_all_Query_withoutAPI(query)
    listSim=[]

    # extract feature from urls
    ListIdentity=[]
    for firtUrl in listURL:
        ListIdentity.append(firtUrl.id)
        for secondUrl in listURL:
            if(firtUrl.id != secondUrl.id and secondUrl.id not in ListIdentity):
                cosineSim=get_cosine_similarity(firtUrl.contentText,secondUrl.contentText)
                length=abs(len(firtUrl.contentText)-len(secondUrl.contentText))
                dist=abs(len(firtUrl.contentText.split(" "))-len(secondUrl.contentText.split(" ")))
                sameDomain=(urllib.parse.urlparse(firtUrl.url).netloc==urllib.parse.urlparse(secondUrl.url).netloc)

                listSim.append(urlsim.urlsSim(firtUrl.url,secondUrl.url,cosineSim,length,dist,sameDomain))
    #print(len(listURL))
    #print(len(listSim))

    # get test set ( all url is test set in this case)
    X_test=[]
    for url in listSim:
        X_test.append(url.getList())

    # load the model
    model = load(open('model.pkl', 'rb'))

    # make predictions
    y_pred = model.predict(X_test)

    # make predict lable to urls 
    for i in range(len(listSim)):
        listSim[i].setLabel(y_pred[i])
    
    listOfSimilarURl =[]
    listOfNotSimilarURl =[ss.url for ss in listURL]
    #list of urls similar (object of urlsim)
    for i in range(len(listSim)):
        if listSim[i].getLabel() == 1:
            listOfSimilarURl.append(listSim[i])

    #group of urls
    # dic=dict()
    # for i in range(len(listOfSimilarURl)):
    #     #print(listOfSimilarURl[i].url1," ",listOfSimilarURl[i].url2)
    #     listOfNotSimilarURl =[ss for ss in listOfNotSimilarURl if ( ss !=listOfSimilarURl[i].url1 and  ss != listOfSimilarURl[i].url2 )]
    #     if listOfSimilarURl[i].url1.strip()  in dic or listOfSimilarURl[i].url2.strip() in dic:
    #         if listOfSimilarURl[i].url1.strip()  in dic:
    #             dic[listOfSimilarURl[i].url1.strip()].append(listOfSimilarURl[i].url2.strip())
    #         else:
    #             dic[listOfSimilarURl[i].url2.strip()].append(listOfSimilarURl[i].url1.strip())
    #     else:
    #          dic[listOfSimilarURl[i].url1.strip()]=[listOfSimilarURl[i].url2.strip()]

    # new_dic=dict()
    # selectedKey=[]
    # for key,items in dic.items():
    #     if key in selectedKey:
    #         continue
    #     new_dic[key]=[]
    #     for item in items:
    #         new_dic[key].append(item)
    #         if item in dic:
    #             selectedKey.append(item)
    #             for ss in dic[item]:
    #                 dic[key].append(ss)

    #end of group of urls


    #show urls group
    # for key,items in dic.items():
    #     print("Similal to ", key," : ",items)
    #     print('-----------------')
          


    listSimilarity=[]
    for i in range(len(listOfSimilarURl)):
        #print(listOfSimilarURl[i].url1," ",listOfSimilarURl[i].url2)
        listOfNotSimilarURl =[ss for ss in listOfNotSimilarURl if ( ss !=listOfSimilarURl[i].url1 and  ss != listOfSimilarURl[i].url2 )]
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
    # print(len(listOfSimilarURl))
    print('-----------------')
    print("Other sites : ")
    print(listOfNotSimilarURl)
   