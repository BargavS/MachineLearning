
# coding: utf-8

# In[40]:


from Precode2 import *
import numpy as np
import matplotlib.pyplot as plt 
import sys 
   
from bokeh.plotting import figure
from bokeh.io import show, output_notebook

data = np.load('AllSamples.npy')
k1,i_point1,k2,i_point2 = initial_S2('')


# In[44]:


# please replace 0111 with your last four digit of your ID
#print(data)

centroid_1 ={}
condition=1
cost = []
def find_clusters(k, centroids):
   print(k)
   print(centroids)
   #initialize array for clusters (k)
   clusters = {}
   for i in range(k):
       clusters[i] = []
   for subset in data:
       euc_dist = []
       for j in range(k):
           euc_dist.append(np.linalg.norm(subset - centroids[j]))
       clusters[euc_dist.index(min(euc_dist))].append(subset)

   return clusters
def find_centroid(k, clusters):
   centro = {}
   for i in range(k1):
       centro[i] = []
   for i in range(k):
       centro[i] = np.average(clusters[i], axis=0)
       
   return centro
   
def graph_plot(centroids):
   # Create a blank figure with labels
   p = figure(plot_width = 600, plot_height = 600, 
              title = 'Clustering',
              x_axis_label = 'X', y_axis_label = 'Y')

   # Add squares glyph
   for i in range(len(data)):
       p.square(data[i][0],data[i][1], size = 12, color = 'red')

   for i in range(len(i_point1)):
       p.square(i_point1[i][0],i_point1[i][1], size = 12, color = 'navy')

   #p.circle(circles_x, circles_y, size = 12, color = 'red')

   # Set to output the plot in the notebook
   output_notebook()
   # Show the plot
   show(p)
def check_condition(centroids, k):
   for i in range(k):
       
       if(centroids[i]== centroid_1[i]):
           condition = 0
def find_cost(k,cluster,centroids):
   val = 0
   for i in range(k):
       for sub in cluster[i]:
           val += np.linalg.norm(sub - centroids[i])**2
   cost.append([centroids, val])
# function to plot the selected centroids 
def plot(data, centroids): 
   plt.scatter(data[:, 0], data[:, 1], marker = '.',  
               color = 'gray', label = 'data points') 
   plt.scatter(centroids[:-1, 0], centroids[:-1, 1],  
               color = 'black', label = 'previously selected centroids') 
   plt.scatter(centroids[-1, 0], centroids[-1, 1],  
               color = 'red', label = 'next centroid') 
   plt.title('Select % d th centroid'%(centroids.shape[0])) 
     
   plt.legend() 
   plt.xlim(-5, 12) 
   plt.ylim(-10, 15) 
   plt.show() 
   
# K Means with k1

def distance(p1, p2): 
   return np.sum((p1 - p2)**2)
def calculate_centroids(k):
   centroids = []
   c={}
   centroids.append(i_point2) 
   plot(data, np.array(centroids)) 
  
   for c_id in range(k - 1): 
         
       dist = [] 
       for i in range(data.shape[0]): 
           point = data[i, :] 
           d = sys.maxsize 
             
           ## compute distance of 'point' from each of the previously 
           ## selected centroid and store the minimum distance 
           for j in range(len(centroids)): 
               temp_dist = distance(point, centroids[j]) 
               d = min(d, temp_dist) 
           dist.append(d) 
             
       ## select data point with maximum distance as our next centroid 
       dist = np.array(dist) 
       next_centroid = data[np.argmax(dist), :] 
       centroids.append(next_centroid) 
       dist = [] 
       plot(data, np.array(centroids)) 
   for l in range(k):
       c[l] = centroids[l]
   return c
centroid = calculate_centroids(k2)
print(centroid)

for i in range(50):
   cluster = find_clusters(k2, centroid)
   cent = find_centroid(k2, cluster)
   centroid = cent
   find_cost(k2,cluster,centroid)
   #check_condition(centroids,k1)   

print(cost)
#centroids = i_point2
#for j in range(100):
   #centroids = [data[np.random.choice(range(data.shape[0]),replace=False)],data[np.random.choice(range(data.shape[0]),replace=False)],data[np.random.choice(range(data.shape[0]),replace=False)],data[np.random.choice(range(data.shape[0]),replace=False)],data[np.random.choice(range(data.shape[0]),replace=False)]]
#for i in range(50):
   #centroid_1 = centroids
   #cluster = find_clusters(k2, centroids)
   #cent = find_centroid(k2, cluster)
   #centroids = cent
   #find_cost(k2,cluster,centroids)
   #check_condtion(centroids,k1)   

#print(cost)


#graph_plot(centroids)


# In[3]:


print(k1)
print(i_point1)
print(k2)
print(i_point2)


# In[26]:


a =[]
a.append(data[np.random.randint( 
            data.shape[0]), :]) 


# In[27]:


print(a)

