import re
import json
import shelve
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from status import Status

class InvertedIndex:
    """
    Inverted Index class.
    """

    def __init__(self):
        self.index = dict()

    stop_words = set(stopwords.words('english'))
    snowball_stemmer = SnowballStemmer('english')
    """get initial movie data from json file"""

    # def get_file(self, file):

    # 	return init_movie

    def __repr__(self):
        return str(self.index)

    def index_document(self, idx, movie):
        """
        Process a given document, save it to the DB and update the index.
        """
        # Remove punctuation from the text.
        # In above code, we are substituting(re.sub) all NON[alphanumeric characters(\w) and spaces(\s)] with empty string.
        clean_title = re.sub(r'[^\w\s]', '', str(movie['Title']))
        clean_text = re.sub(r'[^\w\s]', '', str(movie['Text']))
        words = clean_title.split(' ')
        words = words + clean_text.split(' ')

        stop_words = set(stopwords.words('english'))
        snowball_stemmer = SnowballStemmer('english')

        # get rid of stop word

        words = [w for w in words if not w in stop_words]

        # stem all word
        words = list(set([snowball_stemmer.stem(w) for w in words]))

        cur_dict = dict()
        # Dictionary with each term and the frequency it appears in the text.
        for word in words:
            word_frequency = cur_dict[word].frequency if word in cur_dict else 0
            # renew the value of key:term
            cur_dict[word] = Status(idx, word_frequency + 1)

        # Update the inverted index
        update_dict = {key: [status] if key not in self.index else self.index[key] + [status] for (key, status) in
                       cur_dict.items()}
        self.index.update(update_dict)

    # Add the document into the database

    def get_index(self, file):
        with open(file, 'r') as f:
            init_movie = json.load(f)
        i = 1
        while True:
            # len(init_movie)
            if i > 10:
                break
            idx = str(i)
            movie = init_movie[idx]
            self.index_document(idx, movie)
            i += 1

        a = shelve.open('index_file', flag='c', protocol=None, writeback=False)
        for (key, value) in self.index.items():
            a[key] = value
        a.close()

    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances.
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        a = shelve.open('index_file')
        return {term: a[term] for term in query if term in a}

    def dict_keys(self):
        a = shelve.open('index_file')
        return list(a.keys())

t = InvertedIndex()
t.get_index('2018_movies.json')
# a = shelve.open('index_file')
# b = list(a.values())[0:100]
# print(type(b))
# print(b)
# c = list(a.keys())[0:100]
# print(type(c))
# print(c)
# print(list(a['produc']))

