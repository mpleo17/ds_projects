from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from ..data.data_loader import get_top_words, train_data, test_data
from scipy.sparse import hstack, csr_matrix
import pandas as pd


def build_X(x_input, augment: bool = False, x_augment = None): 
    """
    Builds X train for modeling.
    Feature augmentation is possible.
    """
    
    vectorizer = TfidfVectorizer(stop_words='english',
                                 max_features=5000,
                                 min_df=1, 
                                 ngram_range=(1, 2)
                                )
    X_tfidf = vectorizer.fit_transform(x_input)

    if augment:
        result = hstack([X_tfidf, x_augment.values.reshape(-1,len(x_augment.columns))])
    else:
        result = X_tfidf
    return result
    

if __name__ == '__main__':
    
    newsgroups_train = train_data()
    newsgroups_test = test_data()
    
    train = list(zip(newsgroups_train.target, newsgroups_train.data))
    df = pd.DataFrame(train, columns=['Target', 'Text'])
    df['Target Article Category'] = df['Target'].apply(lambda x: newsgroups_train.target_names[x])
    df['Article Length'] = df['Text'].apply(lambda x: len(x))

    X = df['Text']
    y = df['Target']

    build_X(x_input = X, augment = False, x_augment = df['Article Length'])