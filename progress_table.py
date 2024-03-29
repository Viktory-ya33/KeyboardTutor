#!/usr/bin/env python3
"""Окно с таблицей прогресса"""

import tkinter
import json

BEST_TIME = 'Лучшее время'
BEST_SPEED = 'Лучшая скорость'
LAST_TIME = 'Крайнее время'
LAST_SPEED = 'Крайняя скорость'
WORDS = 'Слова'
LETTERS = 'Буквы'
QUOTATIONS = 'Цитаты'
PUNCTUATIONS = 'Пунктуация'
NUMBERS = 'Числа'
LONG_TEXT = 'Длинный текст'
PYTHON = 'Python'
TYPESCRIPT = 'TypeScript'

class Table:
    def __init__(self, root, rows, columns, values):
        for i in range(rows):
            for j in range(columns):
                self.e = tkinter.Entry(root, width=16, font=('Arial', 12),
                                       justify=tkinter.CENTER)
                if i == 0:
                    self.e.config(font=('Arial', 13, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(tkinter.END, values[i][j])
                self.e.config(state="readonly")


class ProgressTableWindow(tkinter.Toplevel):
    def __init__(self, main):
        super().__init__(master=main)
        self.title("Прогресс")
        self.resizable(width=False, height=False)

        columns = ['Тема тренировки', BEST_TIME, f'{BEST_SPEED} (с/м)',
                   LAST_TIME, f'{LAST_SPEED} (с/м)']
        with open("progress.json", encoding='utf-8') as file:
            self.progress_json = json.load(file)

        ltrs = self.progress_json[LETTERS]
        pt = self.progress_json[PUNCTUATIONS]
        nmrs = self.progress_json[NUMBERS]
        words = self.progress_json[WORDS]
        qts = self.progress_json[QUOTATIONS]
        lng = self.progress_json[LONG_TEXT]
        py = self.progress_json[PYTHON]
        tps = self.progress_json[TYPESCRIPT]
        values = [columns,
                  [LETTERS, f'{ltrs[BEST_TIME]}', f'{ltrs[BEST_SPEED]}',
                   f'{ltrs[LAST_TIME]}', f'{ltrs[LAST_SPEED]}'],
                  [PUNCTUATIONS, f'{pt[BEST_TIME]}', f'{pt[BEST_SPEED]}',
                   f'{pt[LAST_TIME]}', f'{pt[LAST_SPEED]}'],
                  [NUMBERS, f'{nmrs[BEST_TIME]}', f'{nmrs[BEST_SPEED]}',
                   f'{nmrs[LAST_TIME]}', f'{nmrs[LAST_SPEED]}'],
                  [WORDS, f'{words[BEST_TIME]}', f'{words[BEST_SPEED]}',
                   f'{words[LAST_TIME]}', f'{words[LAST_SPEED]}'],
                  [QUOTATIONS, f'{qts[BEST_TIME]}', f'{qts[BEST_SPEED]}',
                   f'{qts[LAST_TIME]}', f'{qts[LAST_SPEED]}'],
                  [LONG_TEXT, f'{lng[BEST_TIME]}', f'{lng[BEST_SPEED]}',
                   f'{lng[LAST_TIME]}', f'{lng[LAST_SPEED]}'],
                  [PYTHON, f'{py[BEST_TIME]}', f'{py[BEST_SPEED]}',
                   f'{py[LAST_TIME]}', f'{py[LAST_SPEED]}'],
                  [TYPESCRIPT, f'{tps[BEST_TIME]}', f'{tps[BEST_SPEED]}',
                   f'{tps[LAST_TIME]}', f'{tps[LAST_SPEED]}']]
        self.table = Table(self, 9, 5, values)
