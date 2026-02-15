import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data={
"title":["Inception","Interstellar","The Dark Knight","Titanic","The Notebook","Avengers","Gravity","La La Land","The Conjuring","Joker"],
"genre":[
"Action Sci-Fi Thriller",
"Adventure Sci-Fi Drama",
"Action Crime Drama",
"Romance Drama",
"Romance Drama",
"Action Superhero Adventure",
"Sci-Fi Space Drama",
"Romance Musical Drama",
"Horror Thriller",
"Crime Drama Thriller"
]}

df=pd.DataFrame(data)

vectorizer=TfidfVectorizer()
tfidf_matrix=vectorizer.fit_transform(df["genre"])

user_input=input("Enter your preferred genres (comma separated): ")
user_vector=vectorizer.transform([user_input])

similarity=cosine_similarity(user_vector,tfidf_matrix)

similar_scores=list(enumerate(similarity[0]))
sorted_movies=sorted(similar_scores,key=lambda x:x[1],reverse=True)

recommendations=[df["title"][i] for i,_ in sorted_movies[:5]]

print("Top Recommended Movies:")
for movie in recommendations:
    print(movie)
