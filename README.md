WEEK3.PY:
DENSITY ESTIMATION AND CLASSIFICATION
The project consists of implementation of the Naïve Bayes classifier that
assumes that the features are independent of each other. Given 10000 training
examples, 5000 handwritten digit zero and 5000 handwritten digits one, the
algorithm has to model a classifier based on the training set and determines
whether the given image is a 0 or 1.

Mathematical modelling and defining variables:
The given images of the 10000 samples are defined by a 28x28 vector. The
feature of the images is considered to be the brightness of the pixels and the
deviation of brightness of pixels from the mean. The Mean and distribution of
the brightness of the entire image for each label is then calculated and
visualized as a Gaussian distribution with two means and variance.

Results
(No.1) Mean of feature1 for digit0 - 44.14111343
(No.2) Variance of feature1 for digit0 115.50482373
(No.3) Mean of feature2 for digit0 87.36453556
(No.4) Variance of feature2 for digit0 102.17048578]
(No.5) Mean of feature1 for digit1 19.37864435
(No.6) Variance of feature1 for digit1 30.8808238
(No.7) Mean of feature2 for digit1 61.39433494
(No.8) Variance of feature2 for digit1 80.83307837
Accuracy for Digit 0 - 0.92777
Accuracy for Digit 1 – 0.92343


UTF8_STRATEGY1:
K-MEANS UNSUPERVISED CLASSIFIER
The project consists of implementation of the K means clustering algorithm on a 2 Dimensional data points. The K Means clustering is an unsupervised algorithm that basically involves clustering of data based on the Euclidean distance of
the points to the cluster centroids.
Mathematical modelling and defining variables: The algorithm follows an iterative approach by initialising the cluster centroids. The number of clusters is however chosen by looking at the data and intuitively deciding the best for the kind of data that is being used for clustering. In the program, the number of Clusters are given as k=3,k=5. The Euclidean norm or distance between each sample data and all the clusters are calculated and the index of the cluster that has the minimum distance is assigned to the data. Using all the data that is now in the cluster, the mean is calculated for each cluster, which forms the new centroids. This process is repeated until the mean converges or stays constant for the
interations.
RESULTS:
(No.1) Centroid for K=3, centeriod1 = [[4.84461158,
7.30111158],| 3.34467115, 2.618687281,1 7.3773277 ,
2.37886035]]
(No.2) cost1 = 1338.133047467403
(No.3) Centroid2 for K=5, centeriod2 = [[ 3.21257461, 2.496580871,[7.75648325, 8.556689281,[ 2.51976116,
7.02028909],[7.25262683, 2.40015826],[ 5.29629878,
6.64908797]]
(No.4) cost2 = 613.98662860666343

UTF8_STRATEGY2:
The algorithm follows an iterative approach by initialising
the cluster centroids. The only difference between the
previous algorithm and this is the initialisation of the
variable. The initial centroid is randomly chosen. The next
centroid is chosen as the furthest data point from the
available sample set and so on by calculating the maximum
distance from the data point and the centroid.
The number of clusters is however chosen by looking at the
data and intuitively deciding the best for the kind of data that
is being used for clustering. In the program, the number of
Clusters are given as k=4,k=6. The Euclidean norm or
distance between each sample data and all the clusters are
calculated and the index of the cluster that has the minimum
distance is assigned to the data. Using all the data that is now
in the cluster, the mean is calculated for each cluster, which
forms the new centroids. This process is repeated until the
mean converges or stays constant for the interations.

Results
{0: array([ 7.75648325, 8.55668928]), 1:
array([ 3.14506148, 0.90770655]), 2:
array([ 2.52382885, 7.02897469]), 3:
array([ 7.41419243, 2.32169114]), 4: array([ 3.502455
, 3.62870476]), 5: array([ 5.46427736, 6.83771354])},
476.29657052696626]]
(No.1) Centroid for K=4, centeriod1 = [[ 3.21257461,
2.49658087],[ 7.13560727, 7.91651726],[ 3.39262114,
6.8928815 ],[ 7.22707673, 2.52234361]]
(No.2) cost1 = cost1 = 797.9601840
(No.3) Centroid2 for K=6, centeriod2 = [[ 7.75648325,
8.55668928],[ 3.14506148, 0.90770655], [ 2.52382885,
7.02897469],[ 7.41419243, 2.32169114],[ 3.502455 ,
3.62870476],[ 5.46427736, 6.83771354]]
(No.4) cost2 = 476.29657052696626
