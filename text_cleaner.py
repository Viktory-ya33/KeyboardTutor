#!/usr/bin/env python3
"""Очистка текста, исправление форматирования, очистка от ненужных символов"""

import re
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import lower_text, normalize_whitespace, remove_multiple_spaces_and_strip_text


def remove_repeating_punctuation_and_spaces(text):
    text = re.sub(r'(?<=[.,:;!?"\'%#-])[ .,:;?!#%-]*', r'', text)
    text = ' '.join(text.split())
    text = re.sub(r'\s+(?=(?:[,.?!:;-]))', r'', text)
    text = re.sub(r'(?<=[.,:;?!])(?=[^?!. ])', r' ', text)
    return text


def capitalize_first_word(text):
    return ''.join([i.capitalize() for i in re.split('([.!?] *)', text)])


def remove_bad_symbols(text):
    text = re.sub(r'[«»]', r'"', text)
    text = re.sub(r'[\\/]', r'', text)
    return text


def remove_word_wrapping(text):
    return re.sub(r'(?<=[a-zа-яё])-\s*\n\s*(?=[a-zа-яё])', r'', text)


def normalize_whitespace_with_special_signs(text):
    text = re.sub('-', r' - ', text)
    text = re.sub(r'\+', ' + ', text)
    text = re.sub(r'=', ' = ', text)
    return text


class TextCleaner:
    @staticmethod
    def clean_text(text):
        preprocessor = Preprocessor()
        preprocessor.pipe(lower_text)
        preprocessor.pipe(remove_word_wrapping)
        preprocessor.pipe(remove_repeating_punctuation_and_spaces)
        preprocessor.pipe(remove_bad_symbols)
        preprocessor.pipe(normalize_whitespace)
        preprocessor.pipe(remove_multiple_spaces_and_strip_text)
        preprocessor.pipe(capitalize_first_word)
        preprocessor.pipe(normalize_whitespace_with_special_signs)
        return preprocessor.run(text)
