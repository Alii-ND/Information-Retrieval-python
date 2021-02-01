import databaseHandler as dbHandler
import urllib.parse
from cosineSimilarity2 import get_cosine_similarity
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from matplotlib import pyplot

from sklearn.cluster import AgglomerativeClustering

from sklearn.cluster import SpectralClustering
class WithoutAPI:
    def __init__(self):
        self.db = dbHandler.databaseHandler()
        
    def collectionData(self):
        return

    def dataPreProssessing(self):
        return

    def calculateSimilaraty(self):
        return





    def calculateSimilaraty2(self):
        listOfQuerys=self.db.get_all_url_withoutAPI()
        listCosine=[]
        listDist=[]
        for query in listOfQuerys:
            for firtUrl in query.urls:
                for secondUrl in query.urls:
                    if(firtUrl.id != secondUrl.id):
                        # print(get_result(firtUrl.contentText,secondUrl.contentText))
                        cosineSim=get_cosine_similarity(firtUrl.contentText,secondUrl.contentText)
                        listCosine.append(cosineSim)
                        dist=abs(len(firtUrl.contentText.split(" "))-len(secondUrl.contentText.split(" ")))
                       
                        #print(cosineSim)
                        #print(dist)
                        listDist.append(dist)

        return listCosine, listDist               


    def ToCSV(self):
        listOfQuerys=self.db.get_all_url_withoutAPI()
        listCosine=[]
        listWeb1=[]
        listWeb2=[]
        listDist=[]
        listLength=[]
        listofDomain=[]
        for query in listOfQuerys:
            ListIdentity=[]
            for firtUrl in query.urls:
                ListIdentity.append(firtUrl.id)
                for secondUrl in query.urls:
                    if(firtUrl.id != secondUrl.id and secondUrl.id not in ListIdentity):
                        cosineSim=get_cosine_similarity(firtUrl.contentText,secondUrl.contentText)
                        listCosine.append(cosineSim)
                        dist=abs(len(firtUrl.contentText.split(" "))-len(secondUrl.contentText.split(" ")))
                        listDist.append(dist)
                        length=abs(len(firtUrl.contentText)-len(secondUrl.contentText))
                        listLength.append(length)
                        listWeb1.append(firtUrl.id)
                        listWeb2.append(secondUrl.id)
                        sameDomain=(urllib.parse.urlparse(firtUrl.url).netloc==urllib.parse.urlparse(secondUrl.url).netloc)
                        listofDomain.append(sameDomain)
                        
        data = {
            'web1':listWeb1,
            'web2':listWeb2,
            'cosine': listCosine,
            'len': listLength,
            'word':listDist,
            'sameDomain':listofDomain
        }

        df = pd.DataFrame(data, columns= ['web1', 'web2','cosine','len','word','sameDomain'])

        df.to_csv (r'export.csv', index = True, header=True)

        #print (df)     

    def countWord(self,id1,id2):
        listOfQuerys=self.db.get_all_url_withoutAPI2(id1,id2)
        for query in listOfQuerys:
            ListIdentity=[]
            for firtUrl in query.urls:
                ListIdentity.append(firtUrl.id)
                for secondUrl in query.urls:
                    if(firtUrl.id != secondUrl.id and secondUrl.id not in ListIdentity):
                        cosineSim=get_cosine_similarity(firtUrl.contentText,secondUrl.contentText)
                        dist=abs(len(firtUrl.contentText.split(" "))-len(secondUrl.contentText.split(" ")))
                        length=abs(len(firtUrl.contentText)-len(secondUrl.contentText))
                        print("cosine : ",cosineSim)
                        print("len : ",length)
                        print("count word diff : ",dist)
                        print("id : ",firtUrl.id,", count : ",len(firtUrl.contentText.split(" ")),", len : ",len(firtUrl.contentText))
                        print("id : ",secondUrl.id,", count : ",len(secondUrl.contentText.split(" ")),", len : ",len(secondUrl.contentText))
                        return
                              