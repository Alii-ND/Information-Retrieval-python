
#import WithAPI  as withAPI
import WithoutAPI  as withoutAPI
import databaseHandler as dbHandler
import classification as clf
import prediction as pred


#db = dbHandler.databaseHandler()
#infoRet= withAPI.WithAPI();
infoRet= withoutAPI.WithoutAPI();


#listOfScoreCosine=db.get_all_score_cosine_withoutAPI()


#infoRet.ToCSV()

# Decision Tree
clf.classificationDesionTree()

# SVM
#clf.classificationSVM()

# Gaussian Naive Bayes
#clf.classificationGaussianNaiveBayes()

# Multinomial Naive Bayes
#clf.classificationMultinomialNaiveBayes()

# Complement Naive Bayes
#clf.classificationComplementNaiveBayes()

# Bernoulli Naive Bayes
#clf.classificationMultinomialNaiveBayes()

#  Categorical Naive Bayes
#clf.classificationComplementNaiveBayes()

# Random Forest
#clf.classificationRandomForest()

query='ادوات البيانات الضخمة'
#what is internet of things
#ادوات البيانات الضخمة

#pred.getPrediction(query)