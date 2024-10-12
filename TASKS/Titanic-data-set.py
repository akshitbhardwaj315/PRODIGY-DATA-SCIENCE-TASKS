import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Akshit\Downloads\titanic\train.csv')


missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])


df['Age'] = df['Age'].fillna(df['Age'].median())
df.drop(columns=['Cabin'], inplace=True)
df.drop(columns=['Ticket', 'Name'], inplace=True)

df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')

print(df.describe(include='all'))

# plt.figure(figsize=(10, 6))
# sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# plt.title('Missing Values Heatmap')
# plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Survived')
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Sex', y='Survived')
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Pclass', y='Survived')
plt.title('Survival Rate by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# corr_df = df.select_dtypes(include=['int64', 'float64']).corr()
# plt.figure(figsize=(10, 6))
# sns.heatmap(corr_df, annot=True, fmt=".2f", cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()

sns.pairplot(df, hue='Survived')
plt.show()

df.to_csv('cleaned_titanic.csv', index=False)
