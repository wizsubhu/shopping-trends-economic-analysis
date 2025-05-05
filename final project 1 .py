
# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# In[2]:


# Load the dataset
df = pd.read_csv('shopping_trends.csv')


# In[3]:


# Check data structure
display(df.head(10))


# In[4]:


df.info()


# In[5]:


# Pair Plot: Visualizing relationships between numerical variables
numeric_columns = ['Age', 'Purchase Amount (USD)', 'Previous Purchases']
if 'Price' in df.columns:
    numeric_columns.append('Price')
sns.pairplot(df[numeric_columns])
plt.show()


# In[6]:


age_bins = [0,18,25,35,45,55,65,100]
age_labels = ["0-18","19-25","26-35","36-45","46-55","56-65","65+"]
df["Age_group"] = pd.cut(df["Age"],bins=age_bins,labels=age_labels,right=False)
age_category_group = df.groupby(["Age_group","Category"])["Customer ID"].count().reset_index()
pivot_table = age_category_group.pivot(index="Age_group",columns="Category", values="Customer ID").fillna(0)
print(pivot_table)


# In[7]:


colors=["#006BA6","#FEC0AA","#BBADFF","#C1EEFF"]
pivot_table.plot(kind='bar',stacked=True,figsize=(10, 6),color=colors)
plt.title('Product Category Preferences by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Category')
plt.show()


# In[8]:


# Select the 'Payment Method' column for the pie chart
payment_method_counts = data['Payment Method'].value_counts(normalize=True)

# Plot the pie chart
plt.figure(figsize=(8, 6))
plt.pie(payment_method_counts, 
        labels=payment_method_counts.index,  # Use the unique payment method names as labels
        autopct='%1.1f%%', 
        startangle=140, 
        colors=sns.color_palette('pastel', len(payment_method_counts)))

# Add title and ensure circular aspect ratio
plt.title('Distribution of Payment Methods')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()


# In[9]:


# Heatmap: Correlation between numerical variables
corr_matrix = df[numeric_columns].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Correlation Heatmap of Economic Variables')
plt.show()


# In[10]:


# Engel's Law: Regression model to analyze spending vs. previous purchases
X = df[['Previous Purchases']]
y = df['Purchase Amount (USD)']
model = LinearRegression()
model.fit(X, y)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Previous Purchases'], y=df['Purchase Amount (USD)'], label='Data')
plt.plot(df['Previous Purchases'], model.predict(X), color='red', label='Trend Line')
plt.title("Engel's Law: Spending vs. Previous Purchases")
plt.xlabel('Previous Purchases')
plt.ylabel('Purchase Amount (USD)')
plt.legend()
plt.show()


# In[11]:


print(f'Regression Coefficient (Slope): {model.coef_[0]:.2f}')
print(f'Intercept: {model.intercept_:.2f}')


# In[12]:


# Consumer Spending Behavior: Spending by Payment Method
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Payment Method'], y=df['Purchase Amount (USD)'])
plt.xticks(rotation=45)
plt.title('Consumer Spending by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Purchase Amount (USD)')
plt.show()


# In[13]:


# Violin Plot: Distribution of Purchase Amount by Payment Method
plt.figure(figsize=(10, 5))
sns.violinplot(x=df['Payment Method'], y=df['Purchase Amount (USD)'], inner='quartile')
plt.xticks(rotation=45)
plt.title('Distribution of Purchase Amount by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Purchase Amount (USD)')
plt.show()

