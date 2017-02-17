# -*- coding: utf-8 -*-

"""This is the entry point of the program."""


def detect_word_language(word, languages):
    """
       For a given word find the language it belongs to
       input: word, language list
       output: language
    """
    for l in languages:
        if word in l['common_words']:
            return l['name']


def find_max(lang__word_count):
    """"
    For the given text find the language with max word count
    input: language_word_count
    output: max_count
    """

    sorted_lang_list = sorted(lang__word_count.items(),
                              key=lambda x: x[1], reverse=True)
    return sorted_lang_list[0][0]


def get_words_from_text(text):
    """
        Get the list of words from the text
    """
    text = text.split('\n')
    words = []
    for line in text:
        words.extend(line.split(' '))
    return words


def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here

    lang_word_count = {
        'Spanish': 0,
        'German': 0,
        'English': 0
    }
    result = None
    words = get_words_from_text(text)
    for word in words:
        # print word
        result = detect_word_language(word, languages)
        if result is not None:
            lang_word_count[result] += 1

    language_found = find_max(lang_word_count)
    return language_found
