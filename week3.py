
# coding: utf-8

# In[209]:


import numpy
import scipy.io
import math
import geneNewData

def main():
    myID=''
    geneNewData.geneData(myID)
    Numpyfile0 = scipy.io.loadmat('digit0_stu_train'+myID+'.mat')
    Numpyfile1 = scipy.io.loadmat('digit1_stu_train'+myID+'.mat')
    Numpyfile2 = scipy.io.loadmat('digit0_testset'+'.mat')
    Numpyfile3 = scipy.io.loadmat('digit1_testset'+'.mat')
    
    train0 = Numpyfile0.get('target_img')
    train1 = Numpyfile1.get('target_img')
    test0 = Numpyfile2.get('target_img')
    test1 = Numpyfile3.get('target_img')
    print([len(train0),len(train1),len(test0),len(test1)])
    print('Your trainset and testset are generated successfully!')
    def extractFeature(dataset):
        feature_2d = []
        dataset = dataset.reshape(dataset.shape[0], dataset.shape[1]*dataset.shape[2])
        #feature_2d[:] = numpy.array([numpy.mean(dataset[:]), numpy.std(dataset[:])])
        for i in range(len(dataset)-1):
            feature_2d[i:] = [[numpy.mean(dataset[i]), numpy.std(dataset[i])]]
        return numpy.array(feature_2d)
    def calculateMeanVariance(dataset): 
        mean1 = numpy.mean([item[0] for item in dataset])
        var1 = numpy.var([item[0] for item in dataset])
        mean2 = numpy.mean([item[1] for item in dataset])
        var2 = numpy.var([item[1] for item in dataset])
        return numpy.array([mean1, var1, mean2, var2])
            
    train0_featureX = extractFeature(train0)
    train1_featureX = extractFeature(train1)
    test0_featureX = extractFeature(test0)
    test1_featureX = extractFeature(test1)
    mean_var_features_0 = calculateMeanVariance(train0_featureX)
    mean_var_features_1 = calculateMeanVariance(train1_featureX)
    def gaussian_distribution(test_data_features, mean_var_feature_x):
        x_var_sqr1 = pow((test_data_features[0]-mean_var_feature_x[0]),2)/(2*mean_var_feature_x[1])
        numerator_feature1 = math.exp(-x_var_sqr1)
        denominator_feature1 = math.sqrt(2*3.14*mean_var_feature_x[1])
        
        x_var_sqr2 = pow((test_data_features[1]-mean_var_feature_x[2]),2)/(2*mean_var_feature_x[3])
        numerator_feature2 = math.exp(-x_var_sqr2)
        denominator_feature2 = math.sqrt(2*3.14*mean_var_feature_x[3])
        
        probabilty_y = (numerator_feature1/denominator_feature1)*(numerator_feature2/denominator_feature2)
        return probabilty_y 
     #prob_digit0 = prior_digit0(0.5)* prob(features of digit0/digit0)
    #prob_digit1 = prior_digit1(0.5)* prob(features of digit1/digit1)
    #prob_digit0
    probabilty_digit_0 = []
    probabilty_digit_00 = []
    probabilty_digit_1 = []
    probabilty_digit_11 = []
    for i in range(len(test0_featureX)-1):
        probabilty_digit_0.append(gaussian_distribution(test0_featureX[i], mean_var_features_0))
        probabilty_digit_1.append(gaussian_distribution(test0_featureX[i], mean_var_features_1))
    for i in range(len(test1_featureX)-1):
        probabilty_digit_00.append(gaussian_distribution(test1_featureX[i], mean_var_features_0))
        probabilty_digit_11.append(gaussian_distribution(test1_featureX[i], mean_var_features_1))
        
    count_0=0
    count_1=0
    a0 =0
    a1 = 0
    for i in range(len(probabilty_digit_0)-1):
        if probabilty_digit_0 > probabilty_digit_1:
            count_0 += 1
        else:
            count_1 += 1
    for i in range(len(probabilty_digit_11)-1):
        if probabilty_digit_00 > probabilty_digit_11:
            a0 += 1
        else:
            a1 += 1
    print(a1/len(test1_featureX))
        
    print(mean_var_features_0)
    print(mean_var_features_1)
if __name__ == '__main__':
    main()


# ## 
