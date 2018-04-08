"""
 Created by XThundering on 2018/4/3
"""
__author__ = 'XThundering'


def is_isbn_or_key(word):
    """

    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(word) == 10 and word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
