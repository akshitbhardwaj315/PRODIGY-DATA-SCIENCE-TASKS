import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Akshit\Downloads\AccidentsBig.csv\AccidentsBig.csv', low_memory=False)
print(df.head())
print(df.columns)

missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

df.dropna(subset=['Date', 'Time', 'Road_Surface_Conditions', 'Weather_Conditions'], inplace=True)

duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

df.drop_duplicates(inplace=True)

df['Date Time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M')
df['Hour'] = df['Date Time'].dt.hour
df['Weekday'] = df['Date Time'].dt.day_name()

print("Data types:\n", df.dtypes)

print("Unique values in Road_Surface_Conditions:\n", df['Road_Surface_Conditions'].unique())
print("Unique values in Weather_Conditions:\n", df['Weather_Conditions'].unique())

road_conditions = df['Road_Surface_Conditions'].value_counts()
weather_conditions = df['Weather_Conditions'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=road_conditions.index, y=road_conditions.values)
plt.title('Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=weather_conditions.index, y=weather_conditions.values)
plt.title('Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

hourly_accidents = df['Hour'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x=hourly_accidents.index, y=hourly_accidents.values, marker='o')
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.xticks(range(24))
plt.grid()
plt.show()

weekday_accidents = df['Weekday'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=weekday_accidents.index, y=weekday_accidents.values)
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x='longitude', y='latitude', data=df, alpha=0.1)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
