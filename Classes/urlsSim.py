
class urlsSim:
    def __init__(self,url1,url2,cosine,length,word,domain):
        self.url1=url1
        self.url2=url2
        self.cosine=cosine
        self.length=length
        self.word=word
        self.domain=domain

    def setLabel(self,label):
        self.label=label

    def getList(self):
        return [ self.cosine,self.length, self.word, self.domain]

    def getLabel(self):
        return self.label

