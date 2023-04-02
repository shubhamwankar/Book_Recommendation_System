import joblib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Initializing global variables
model = joblib.load('model.h5')
pivot_df = pd.read_csv("pivot_data.csv", index_col='Book-Title')
scalar = joblib.load('scalar.h5')

# print(pivot_df)

scaled_df = scalar.transform(pivot_df)
similarity_df = cosine_similarity(scaled_df)


# Function to recommend
def recommend(book_title):
    list_of_books = pivot_df.index.values.tolist()
    if book_title in list_of_books:
        title_index = list_of_books.index(book_title)
        distance, suggestions = model.kneighbors(similarity_df[title_index, :].reshape(1, -1))
        distance, suggestions = distance[0][1:].tolist(), suggestions[0][1:].tolist()
        book_names = [list_of_books[i] for i in suggestions]
        recommendation_df = pd.DataFrame({'Book-Title': book_names,
                                         'Similarity-Score': distance})

        recommendation_df['Similarity-Score'] = recommendation_df['Similarity-Score'].apply(lambda x: 2.0 - x if x > 1 else x)
        recommendation_df.sort_values('Similarity-Score', ascending=False, inplace=True)
        print("-"*50)
        print(f"Here are top 5 recommendation for the book title : {book_title}")
        print("-"*50)
        print(recommendation_df)
        return recommendation_df
    else:
        print("ERROR: Couldn't find the Book Title in the database")
        print("-"*50)
        suggest_books = []
        print("You can try with the below titles:")
        print("-"*50)
        for i in range(5):
            print(np.random.choice(list_of_books))

# Getting a Sample Title
sample_title = np.random.choice(pivot_df.index.values)

recommend(sample_title)