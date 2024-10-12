import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Akshit\Downloads\twitter_validation.csv")
print(df.columns)

# Rename the columns
df = df.rename(columns={'3364': 'ID', 'Facebook': 'Platform', 'Irrelevant': 'Relevance', 
                        'I mentioned on Facebook that I was struggling for motivation to go for a run the other day, which has been translated by Tom’s great auntie as ‘Hayley can’t get out of bed’ and told to his grandma, who now thinks I’m a lazy, terrible person 🤣': 'Tweet'})

# Create a new column 'Sentiment'
df['Sentiment'] = ['Positive' if 'great' in tweet or 'good' in tweet else 'Negative' for tweet in df['Tweet']]

# Plot the sentiment distribution
sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Distribution')
plt.axis('equal')
plt.show()