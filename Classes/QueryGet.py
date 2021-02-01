
class QueryGet:
    def __init__(self,lang,domain,query):
        self.lang=lang
        self.domain=domain
        self.query=query
        self.urls=[]

    def equals(self,lang,domain,query):
        if self.lang==lang and self.domain==domain and  self.query==query :
            return True
        
        return False