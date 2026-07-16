import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("products.csv")

# Fill missing values
df = df.fillna("")

# Clean price
df["price"] = df["price"].astype(str).str.replace("$", "", regex=False)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Create features
df["features"] = (
    df["goods-title-link--jump"] + " " +
    df["rank-sub"] + " " +
    df["selling_proposition"]
)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["features"])

# Similarity
similarity = cosine_similarity(tfidf_matrix)


def recommend_products(search):

    if search.strip() == "":
        return df.head(20)

    matches = df[
        df["goods-title-link--jump"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    if matches.empty:
        return df.head(20)

    index = matches.index[0]

    similarity_scores = list(enumerate(similarity[index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    product_indices = [i[0] for i in similarity_scores[:10]]

    return df.iloc[product_indices]