# Book_Recommendation_Service

## Overview
A book recommendation system is a type of recommendation system that uses data analysis and machine learning algorithms to provide personalized book recommendations to users. These systems can be used by online bookstores, libraries, and other organizations that provide book-related services to their users.

The goal of a book recommendation system is to provide users with recommendations that are tailored to their interests and preferences. This can be accomplished by analyzing user data such as past purchases, browsing history, and ratings of books. The system can also take into account other factors such as genre, author, and publication date to provide more relevant recommendations.

## Methodology
In this project, we will be following methodology mentioned below:

- Data collection: Collect data on book ratings from users. This data can be obtained from a variety of sources such as online bookstores, library systems, or social media platforms.

- Data preprocessing: Clean and preprocess the data to ensure that it is in a usable format. This may involve removing duplicates, handling missing data, and transforming the data into a matrix or other format that can be used by the recommendation algorithm.

- User similarity calculation: Calculate the similarity between users based on their book ratings. There are several methods for calculating similarity, such as Pearson correlation or cosine similarity.

- Neighborhood selection: Identify a set of similar users (known as the "neighborhood") for each user in the dataset. This can be done by setting a threshold similarity score or selecting a fixed number of neighbors.

- Prediction calculation: Predict the rating that a user would give to a particular book by taking a weighted average of the ratings given to that book by the user's neighbors. The weights can be based on the similarity between the user and their neighbors.

- Recommendation generation: Generate a list of recommended books for each user based on their predicted ratings. The number of recommended books can be customized based on user preferences.

- Evaluation: Evaluate the performance of the recommendation system using metrics such as precision, recall, and mean absolute error. These metrics can be used to fine-tune the system and improve its performance.

## Business Segment
1. Retail
2. E-Commerce

## Dataset
Book Recommendation System - [Link](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

## Instructions
In order to use the model. Follow the below steps.

1. Clone the repository using the command below.
```
git clone https://github.com/shubhamwankar/Book_Recommendation_System
```
2. Install the requirements using command below.
```
pip install -r requirements.txt
```
3. Run the load_predict.py file to load the Book Recommender System.

> **Note: The recommendation system only works for the books present in the dataset. In order to customize the model, please reach out to me @ shubhamwankar23@gmail.com**
