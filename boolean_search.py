import shelve
import json
from boolean_index import InvertedIndex

"""
boolean_search.py
author: 

Students: Modify this file to include functions that implement 
Boolean search, snippet generation, and doc_data presentation.
"""


def dummy_search(query):
    """Return a list of movie ids that match the query."""
    ii = InvertedIndex()
    return ii.lookup_query(query)


def dummy_movie_data(doc_id):
    """
    Return data fields for a movie.
    Your code should use the doc_id as the key to access the shelf entry for the movie doc_data.
    You can decide which fields to display, but include at least title and text.
    """
    with open('2018_movies.json') as f:
        doc = json.load(f)
    doc_file = doc[doc_id]

    movie_object = {"title": doc_file['Title'],
                    "director": doc_file['Director'],
                    "location": doc_file['Location'],
                    "text": doc_file['Text']
                    }
    return (movie_object)


def dummy_movie_snippet(doc_id):
    """
    Return a snippet for the results page.
    Needs to include a title and a short description.
    Your snippet does not have to include any query terms, but you may want to think about implementing
    that feature. Consider the effect of normalization of index terms (e.g., stemming), which will affect
    the ease of matching query terms to words in the text.
    """
    with open('2018_movies.json') as f:
        doc = json.load(f)
    doc_file = doc[doc_id]
    s = doc_file['Text'][:100] + "......"
    return (doc_id, doc_file['Title'], s)


def dummy_know_term():
    ii = InvertedIndex()
    return ii.dict_keys()
