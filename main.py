#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas to read dataset
import pandas as pd
#importing seaborn
import seaborn as sb
#reading file
rf=pd.read_csv("file.csv")
print(rf.info())
rf.isnull().any()
sb.scatterplot(data=rf,x="gdp_cap",y="life_exp",hue="continent",size="population",alpha=0.4,palette='viridis')
plt.show()
sb.heatmap(rf.corr())
plt.show()
sb.pairplot(rf,hue="continent")
plt.show()