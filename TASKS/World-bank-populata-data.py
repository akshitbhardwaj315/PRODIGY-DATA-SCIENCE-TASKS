import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Akshit\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_31753\m.csv')

print("Columns in the DataFrame:", df.columns)

if 'Country Code' in df.columns:
    df.dropna(subset=['Country Code'], inplace=True)
    df = df.rename(columns={'Country Code': 'Code'})

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

categorical_columns = [col for col in df.columns if df[col].dtype == 'object']

for column in categorical_columns:
    plt.figure(figsize=(10, 6))
    value_counts = df[column].value_counts()
    sns.barplot(x=value_counts.index, y=value_counts.values)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

print(df.columns)
