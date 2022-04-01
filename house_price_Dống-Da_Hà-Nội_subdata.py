#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
#%%
df = pd.read_csv('house_price_Dống-Da_Hà-Nội_subdata.csv')
df

# %%
df_p = df[['price', 'property_type']]
df_p = df_p.dropna()
df_p.property_type.unique()
#%%
fig, axis = plt.subplots(1, 2, figsize=(16, 6))
sns.boxplot(data = df_p[df_p.property_type=='trong ngo'], ax=axis[0])
sns.boxplot(data = df_p[df_p.property_type=='mat pho'], ax=axis[1])

# %%
df_p.groupby(by=['property_type']).count()

# %%
condition = ((df_p.property_type=='trong ngo') & (df_p.price<45000)) | ((df_p.property_type=='mat pho') & (df_p.price<90000))
df_p = df_p[condition]
df_p.groupby(by=['property_type']).count()

# %%
fig, axis = plt.subplots(1, 2, figsize=(16, 6))
sns.boxplot(data=df_p, y='price', x='property_type', ax=axis[0])
sns.pointplot(data=df_p, y='price', x='property_type', ax=axis[1])

# %%
sns.kdeplot(data=df_p, x="price", hue="property_type", multiple="stack")

# %%
df_p.property_type.unique()
statistics, p_value = scipy.stats.ttest_ind(df_p[df_p['property_type']=='mat pho']['price'], df_p[df_p['property_type']=='trong ngo']['price'])
print("statistics, p_value", statistics, p_value)

# %%
statistics_2, p_value_2 = scipy.stats.ttest_ind(df_p[df_p['property_type']=='mat pho']['price'], df_p[df_p['property_type']=='trong ngo']['price'])
statistics_1, p_value_1 = scipy.stats.ttest_ind(df_p[df_p['property_type']=='mat pho']['price'], df_p[df_p['property_type']=='trong ngo']['price'], alternative="greater")

print("two side statistics_2, p_value_2", statistics_2, p_value_2)
print("one side statistics_1, p_value_1", statistics_1, p_value_1)

# %%
print("Kết luận: Do p_value << alpha và statistic>0, nên Bác bỏ Ho, chấp nhận H1 là nhà mặt phố có giá trung bình cao hơn nhà trong ngõ")

# %%
df_2 = df[['price', 'land_certificate']]
df_2 = df_2.dropna()
df_2.land_certificate.unique()

# %%
fig, axis = plt.subplots(1, 2, figsize=(16, 6))
sns.boxplot(data = df_2[df_2.land_certificate=='So do'], ax=axis[0])

# %%
df_2.groupby(by=['land_certificate']).count()

