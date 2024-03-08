import pandas as pd
import matplotlib.pyplot as plt
#create DataFrame
df1 = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
                   'position': ['G', 'G', 'G', 'F', 'F', 'G', 'G', 'F', 'F', 'F'],
                   'points': [5, 7, 7, 9, 12, 9, 9, 4, 7, 7],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12, 13, 15]})


#create DataFrame
df2 = pd.DataFrame({'team': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points_for': [18, 22, 19, 14, 11, 20, 28],
                   'points_against': [14, 21, 19, 14, 12, 20, 21]})


#calculate mean of points grouped by team and position columns
df=df1.groupby(['team', 'position'])['points'].mean()
#print(df)

#count occurrences of each combination of team and position columns
df=df1.groupby(['team', 'position']).size()

#count number of unique values in 'points' column grouped by 'team' column
df=df1.groupby('team')['points'].nunique()

#display unique values in 'points' column grouped by 'team'
df=df1.groupby('team')['points'].unique()

#count number of unique values in 'points' column grouped by 'team' and 'position'
df=df1.groupby(['team', 'position'])['points'].nunique()

#count number of unique values in 'points' column grouped by 'team' and 'position'
df=df1.groupby(['team', 'position'])['points'].unique()

#find relative frequency of each team name in DataFrame
df=df2.groupby('team').apply(lambda x: x['team'].count() / df.shape[0])

#find max "points_for" values for each team
df=df2.groupby('team').apply(lambda x: x['points_for'].max())

#find max "points_for" values for each team
df=df2.groupby('team').apply(lambda x: (x['points_for'] - x['points_against']).mean())

df3 = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'A',
                            'B', 'B', 'B', 'B', 'B',
                            'C', 'C', 'C', 'C', 'C'],
                   'points': [12, 29, 34, 14, 10, 11, 7, 36,
                              34, 22, 41, 40, 45, 36, 38]})

df=df3.groupby('team')['points'].sum()
df.plot(kind='bar')
#create bar plot with custom aesthetics
df.plot(kind='bar', title='Total Points by Team',
               ylabel='Total Points', xlabel='Team', figsize=(10, 6))


#rotate x-axis ticks vertically
plt.xticks(rotation=0)

plt.show()
print(df)
