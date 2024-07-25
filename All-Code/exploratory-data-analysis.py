import pandas as pd
import numpy as np
import matplotlib.pylab as plt

plt.style.use('ggplot')
pd.options.display.max_columns = 6

df = pd.read_csv('../fulldataset.csv')

#Basic info

numauthors = df.drop_duplicates(subset=['author']).count()
print("Number of authors: ", numauthors)

#Null Values:

print("Missing values:")

authordf = df[['author']].copy()
nullauthor = authordf.isna().sum()
print("missing", nullauthor)

typedf = df[['type']].copy()
nulltype = typedf.isna().sum()
print("missing", nulltype)

titledf = df[['poem name']].copy()
nulltitle = titledf.isna().sum()
print("missing", nulltitle)

#Duplicated Values:

duplepoem = df.duplicated(subset=['poem name']).sum()
print("Duplicated poems:", duplepoem)




"""
#Graph: Age Distribution

ax = df['age'].value_counts().plot(kind='bar', title='Age Distribution')

ax.set_xlabel('Age')
ax.set_ylabel('Number of Poems Included')
plt.show()

#Graph: Authorship Distribution

ax = df['author'].value_counts().plot(kind='bar', title='Authorship Distribution')

ax.set_xlabel('Author Name')
ax.set_ylabel('Number of Poems Included')
plt.show()

#Graph: Thematic Distribution

ax = df['type'].value_counts().plot(kind='bar', title='Thematic Distribution')

ax.set_xlabel('Theme')
ax.set_ylabel('Number of Poems Included')
plt.show()
"""
