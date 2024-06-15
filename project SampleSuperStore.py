#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[20]:


import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# In[21]:


df=pd.read_csv("SampleSuperstore.csv",encoding='ISO-8859-1')


# In[22]:


df.head()


# In[5]:


df.info()


# In[6]:


#changing data type 
if df.duplicated().sum()>0:
    print("Duplicate exist")
else:
    print("Doesn't exist")


# In[23]:


df.head(100)


# In[24]:


# types of customers 



types_of_customers= df['Segment'].unique()
print(types_of_customers)


# In[25]:


number_of_customers= df['Segment'].value_counts().reset_index()


# In[26]:


number_of_customers=number_of_customers.rename(columns={'Segment'  : 'Type of Customers'})


# In[27]:


print(number_of_customers)


# In[31]:


plt.pie(number_of_customers['count'], labels=number_of_customers['Type of Customers'],autopct='%1.1f%%')


# In[43]:


sales_per_segment= df.groupby('Segment')['Sales'].sum().reset_index()
sales_per_segment=sales_per_segment.rename(columns={'Segment' : 'Type of customers' ,'Sales': 'Total Sales'})


print(sales_per_segment)


# In[44]:


plt.bar(sales_per_segment['Type of customers'],sales_per_segment['Total Sales'])


# In[46]:


plt.pie(sales_per_segment['Total Sales'] ,labels=sales_per_segment['Type of customers'] ,autopct='%1.1f%%')


# In[47]:


df.head(3)


# In[54]:


customers_order_frequency = df.groupby(['Customer ID','Customer Name','Segment'])['Order ID'].count().reset_index()
customers_order_frequency.rename(columns = {'Order ID': 'Total Orders'} , inplace = True)
repeat_customers = customers_order_frequency[customers_order_frequency['Total Orders'] >= 1]
repeat_customers_sorted = repeat_customers.sort_values(by='Total Orders', ascending = False)


# In[55]:


print(repeat_customers_sorted)


# In[56]:


customer_sales = df.groupby(['Customer ID','Customer Name','Segment'])['Sales'].sum().reset_index()


# In[57]:


top_spenders = customer_sales.sort_values(by='Sales' ,ascending = False)


# In[61]:


print(top_spenders.head(10).reset_index(drop=True))


# In[62]:


types_of_customers = df['Ship Mode'].unique()


# In[63]:


print(types_of_customers)


# In[64]:


df.head(10)


# In[65]:


shipping_model = df['Ship Mode'].value_counts().reset_index()
shipping_model = shipping_model.rename(columns={'index':'Use Frequency', 'Ship Mode':'Mode Of Shipment', 'count' : 'Use Frequency'})
print(shipping_model)


# In[68]:


plt.pie(shipping_model['Use Frequency'],labels=shipping_model['Mode Of Shipment'],  autopct='%1.1f%%')


# In[73]:


state = df['State'].value_counts().reset_index()
state = state.rename(columns={'index' : 'State' ,'State' : 'Number of Customers'})


# In[74]:


print(state.head(20))


# In[75]:


city = df['City'].value_counts().reset_index()
print(city.head(20))


# In[76]:


state_sales = df.groupby(['State'])['Sales'].sum().reset_index()


# In[80]:


top_sales = state_sales.sort_values(by ='Sales' , ascending = False)


# In[81]:


print(top_sales.head(10).reset_index(drop=True))


# In[84]:


city_sales = df.groupby(['City'])['Sales'].sum().reset_index()


# In[85]:


top_city_sales = city_sales.sort_values(by = 'Sales' , ascending = False)


# In[86]:


print(top_city_sales.head(10).reset_index(drop= True))


# In[87]:


state_city_sales = df.groupby(['State', 'City'])['Sales'].sum().reset_index()
print(state_city_sales.head(20))


# In[89]:


products = df['Category'].unique()
print(products)


# In[90]:


df.head(100)


# In[91]:


product_subcategory = df['Sub-Category'].unique()
print(product_subcategory)


# In[93]:


subcategory_count = df.groupby('Category')['Sub-Category'].nunique().reset_index()
subcategory_count = subcategory_count.sort_values(by='Sub-Category', ascending = False)
print(subcategory_count)


# In[95]:


subcategory_count_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
subcategory_count_sales = subcategory_count_sales.sort_values(by='Sales', ascending = False)    


# In[96]:


print(subcategory_count_sales)


# In[97]:


product_category = df.groupby(['Category'])['Sales'].sum().reset_index()
top_product_category = product_category.sort_values(by='Sales', ascending = False)
print(top_product_category.reset_index(drop=True))


# In[98]:


plt.pie(top_product_category['Sales'], labels=top_product_category['Category'], autopct='%1.1f%%')


# In[99]:


subcategory_count_sales = subcategory_count_sales.sort_values(by='Sales', ascending = True)
plt.barh(subcategory_count_sales['Sub-Category'], subcategory_count_sales['Sales'])
     


# In[110]:


df['Order Date'] = pd.to_datetime(df['Order Date'])
yearly_sales = df.groupby(df['Order Date'].dt.year)['Sales'].sum()
yearly_sales = yearly_sales.reset_index()
yearly_sales = yearly_sales.rename(columns={'Order Date' : 'Year', 'Sales': 'Total Sales'})

print (yearly_sales)


# In[111]:


plt.bar(yearly_sales['Year'], yearly_sales['Total Sales'])


# In[112]:


df.head(10)


# In[113]:


plt.plot(yearly_sales['Year'], yearly_sales['Total Sales'], marker='o', linestyle='-')


# In[147]:


df['Order Date'] = pd.to_datetime(df['Order Date'])
year_sales = df[df['Order Date'].dt.year == 2017]
quarterly_sales = year_sales.resample('QE', on='Order Date')['Sales'].sum()
quarterly_sales = quarterly_sales.reset_index()
quarterly_sales = quarterly_sales.rename(columns = {'Order Date': 'Quarter', 'Sales' : 'Total Sales'})
print(quarterly_sales)


# In[148]:


plt.plot(quarterly_sales['Quarter'], quarterly_sales['Total Sales'], marker = 'o', linestyle = '--')

plt.tight_layout()
plt.xticks(rotation=75)
plt.show()


# In[144]:


df['Order Date'] = pd.to_datetime(df['Order Date'])
yearly_sales = df[df['Order Date'].dt.year == 2017]
monthly_sales = yearly_sales.resample('ME', on = 'Order Date')['Sales'].sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales = monthly_sales.rename(columns={'Order Date':'Month', 'Sales' : 'Total Monthly Sales'})

print (monthly_sales)


# In[145]:


plt.plot(monthly_sales['Month'], monthly_sales['Total Monthly Sales'], marker = 'o', linestyle = '--')


# In[ ]:




