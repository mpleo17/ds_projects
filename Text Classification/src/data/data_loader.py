from sklearn.datasets import fetch_20newsgroups
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

def train_data():
    """
    Fetch the train dataset.
    """
    data = fetch_20newsgroups(
        subset='train',
        categories=None,
        shuffle=True,
        random_state=42,
        remove=('headers', 'footers', 'quotes')
    )
    return data

def test_data():
    """
    Fetch the test dataset.
    """
    data = fetch_20newsgroups(
        subset='test',
        categories=None,
        shuffle=True,
        random_state=42,
        remove=('headers', 'footers', 'quotes')
    )
    return data

def get_top_words(data: str, top_n: int) -> list:
  """
  Function to get top top n words occuring int a text chunk by frequency.
  """

  wordcloud = WordCloud(stopwords=STOPWORDS)
  processed_words = wordcloud.process_text(data)
  top_n_wordlist_w_freq = sorted(processed_words.items(),
                            key=lambda item: item[1],
                            reverse=True)[:top_n]
  top_n_wordlist = [item[0] for item in top_n_wordlist_w_freq]

  return top_n_wordlist_w_freq, " | ".join(top_n_wordlist)

def data_transformed(data):
    """
    Dedicated function for newsgroups data only.
    Outputs additional columns leading to a fixed schema.
    """
    train = list(zip(data.target, data.data))
    df = pd.DataFrame(train, columns=['Target', 'Text'])
    df['Target Article Category'] = df['Target'].apply(lambda x: data.target_names[x])
    df['Article Length'] = df['Text'].apply(lambda x: len(x))
    return df

if __name__ == '__main__':
    
    newsgroups_train = train_data()
    newsgroups_test = test_data()

    newsgroups_train_trnsfrmd = data_transformed(data = newsgroups_train)
    newsgroups_test_trnsfrmd = data_transformed(data = newsgroups_test)