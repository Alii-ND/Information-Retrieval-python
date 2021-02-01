import mysql.connector
import Classes.QueryGet as queryRef
import Classes.URL as urlRef

class databaseHandler:
    _tableQueries_contentWithoutAPI = "queries_content_table"
    _tablefiltered_queriesWithoutAPI = "filtered_queries"
    _tableSimilarityURLWithoutAPI = "similarityURL"
    _tableQueries_contentWithAPI = "queries_content_table_with_api"
    _tablefiltered_queriesWithAPI = "filtered_queries_with_api"
    _tableSimilarityURLWithAPI = "similarityURL_with_api"
    _columnId = "id"
    _columnDomain = "domain"
    _columnLang = "lang"
    _columnQuery = "query"
    _columnUrl = "url"
    _columnOld_body = "old_body"
    _columnUrlResultBodyContent = "urlResultBodyContent"
    _columnFiltered_body = "filtered_body"
    _columnIdURL1 = "idURL1"
    _columnIdURL2 = "idURL2"
    _columnTechnique = "technique"
    _columnTechniqueType = "techniqueType"
    _columnScore = "score"
    _columnTimeExec = "timeExec"
    


    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="google_information_retrieval"
        )



    def get_all_url_withoutAPI(self):
        mycursor = self.con.cursor()
        queryText = "SELECT " + databaseHandler._columnId + "," + databaseHandler._columnLang + "," + databaseHandler._columnDomain + "," + databaseHandler._columnQuery + "," \
        + databaseHandler._columnUrl + "," + databaseHandler._columnFiltered_body + " FROM "	+ databaseHandler._tablefiltered_queriesWithoutAPI  \
        + " " \
        + " ORDER BY " + databaseHandler._columnLang	+ "," + databaseHandler._columnDomain + "," + databaseHandler._columnQuery +""
        queryGet=[]
        mycursor.execute(queryText)
       
        myresult = mycursor.fetchall()
        
        
        for row in myresult:
            id=row[0]
            lang=row[1]
            domain=row[2]
            queryCl=row[3]
            urlCl=row[4]
            body=row[5]
            selectedQ=False
            for q in queryGet:
                if q.equals(lang,domain,queryCl) == True:
                    q.urls.append(urlRef.URL(id,urlCl,body))
                    selectedQ=True
                    break
            if selectedQ == False:
                queryNew = queryRef.QueryGet(lang,domain,queryCl)
                queryNew.urls.append(urlRef.URL(id,urlCl,body))
                queryGet.append(queryNew)
        # print(len(queryGet))
        return queryGet
       

    def get_all_Query_withoutAPI(self,query):
        mycursor = self.con.cursor()
        queryText = "SELECT " + databaseHandler._columnId + "," + databaseHandler._columnLang + "," + databaseHandler._columnDomain + "," + databaseHandler._columnQuery + "," \
        + databaseHandler._columnUrl + "," + databaseHandler._columnFiltered_body + " FROM "	+ databaseHandler._tablefiltered_queriesWithoutAPI  \
        + " where  "+ databaseHandler._columnQuery +" = '" + str(query) +"'" \
        + " ORDER BY " + databaseHandler._columnLang	+ "," + databaseHandler._columnDomain + "," + databaseHandler._columnQuery +" "
        queryGet=[]
        mycursor.execute(queryText)
       
        myresult = mycursor.fetchall()
        
        
        for row in myresult:
            id=row[0]
            lang=row[1]
            domain=row[2]
            queryCl=row[3]
            urlCl=row[4]
            body=row[5]
            queryGet.append(urlRef.URL(id,urlCl,body))

        return queryGet



    def get_all_url_withoutAPI2(self,id1,id2):
        mycursor = self.con.cursor()
        queryText = "SELECT " + databaseHandler._columnId + "," + databaseHandler._columnLang + "," + databaseHandler._columnDomain + "," + databaseHandler._columnQuery + "," \
        + databaseHandler._columnUrl + "," + databaseHandler._columnFiltered_body + " FROM "	+ databaseHandler._tablefiltered_queriesWithoutAPI  \
        + " where id = "+ str(id1) +" or id = "+ str(id2) \
        + " ORDER BY " + databaseHandler._columnLang	+ "," + databaseHandler._columnDomain + "," + databaseHandler._columnQuery +" "
        queryGet=[]
        mycursor.execute(queryText)
       
        myresult = mycursor.fetchall()
        
        
        for row in myresult:
            id=row[0]
            lang=row[1]
            domain=row[2]
            queryCl=row[3]
            urlCl=row[4]
            body=row[5]
            selectedQ=False
            for q in queryGet:
                if q.equals(lang,domain,queryCl) == True:
                    q.urls.append(urlRef.URL(id,urlCl,body))
                    selectedQ=True
                    break
            if selectedQ == False:
                queryNew = queryRef.QueryGet(lang,domain,queryCl)
                queryNew.urls.append(urlRef.URL(id,urlCl,body))
                queryGet.append(queryNew)
        # print(len(queryGet))
        return queryGet




