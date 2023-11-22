import numpy as np
import pandas as pd
import matplotlib.pyplot as pit
import seaborn as sns
df = pd.read_csv("D:\\data analysis project/Expanded_data_with_more_features.csv")

#print(df.describe())
print(df.info())
print(df.isnull().sum())
#drop unnnamed column
df = df.drop("Unnamed: 0", axis = 1) 
print(df.head())
pit.figure(figsize = (5,4))
ax =sns.countplot(data = df,x = "Gender")
ax.bar_label(ax.containers[0])

#pit.show()
#from the above chart we have analysed that:
#the number of females in the data is more than the number of males
gb = df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)
pit.figure(figsize=(4,4))
#sns.heatmap(gb,annot=True )
pit.title(" relationship between parent education impact on child score")
#pit.show()
 #from the above chart we have analysed that:
 #parent education we have concluded parent education have good impact on their child scores
 
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb1)
pit.figure(figsize=(4,4))
#sns.heatmap(gb1,annot=True )
pit.title("relation between parent's martial status effect on child score")
#pit.show()

 #from the above chart we have analysed that:
 #parent martial status   have negligiable or no impact on their child scores
a = sns.boxplot(data = df,x ="MathScore")
print(a)
pit.show()
 