#!/usr/bin/env python3
"""Главное окно приложения"""

ERROR_PYTHON_VERSION = 1

import sys

if sys.version_info < (3, 6):
    print('Use python >= 3.6', file=sys.stderr)
    sys.exit(ERROR_PYTHON_VERSION)

__version__ = '1.1'
__author__ = 'Vikhlyantseva Viktoria'
__email__ = 'v.vihluantseva@gmail.com'

import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from keyboard_tutor import KeyboardTutor


class SpeedLabel:
    def __init__(self, frame):
        self.counter = tkinter.StringVar()
        self.counter.set(0)
        speed_text = tkinter.Label(frame, text="Текущая скорость (сим / мин): ",
                                   font=('Arial', 12, 'bold'))
        speed_counter = tkinter.Label(frame, textvariable=self.counter,
                                      font=('Arial', 12), anchor="e", width=5)

        speed_counter.pack(side=tkinter.RIGHT, padx=5)
        speed_text.pack(side=tkinter.RIGHT)


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Клавиатурный тренажёр")
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.minsize(600, 300)
        self.geometry(f"+{self.winfo_screenwidth() // 5}"
                      f"+{self.winfo_screenheight() // 7}")
        self.resizable(width=False, height=False)
        self.font = ('Times', 12)
        self.option_add('*TCombobox*Listbox.font', self.font)

        buttons_frame = tkinter.Frame(self)
        buttons_frame.pack(side=tkinter.BOTTOM, fill='x')

        top_frame = tkinter.Frame(self)
        top_frame.pack(side=tkinter.TOP, fill='x')

        center_frame = tkinter.Frame(self)
        center_frame.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)

        volume = Image.open("Volume.png")
        self.volume_image = ImageTk.PhotoImage(volume)
        volume_mute = Image.open("VolumeMute.png")
        self.volume_mute_image = ImageTk.PhotoImage(volume_mute)

        self.is_sound_off = False
        self.sound_button = tkinter.Label(top_frame, image=self.volume_image,
                                          font=('Arial', 15, 'bold'))
        self.sound_button.pack(side=tkinter.LEFT)
        self.sound_button.bind("<Button-1>", self.change_sound_state)

        speed_label = SpeedLabel(top_frame)

        topic = ttk.Combobox(top_frame, values=['Буквы', 'Пунктуация',
                                                'Числа', 'Слова',
                                                'Цитаты', 'Длинный текст',
                                                'Python', 'TypeScript'],
                             font=self.font, state='readonly')
        topic.set('Выберите тему')
        topic.pack(side=tkinter.RIGHT, padx=90)

        self.keyboard_tutor = KeyboardTutor(center_frame, speed_label.counter,
                                            topic, top_frame)

        progress = tkinter.Button(buttons_frame, text='Прогресс',
                                  font=('Arial', 12),
                                  command=self.keyboard_tutor.load_progress)
        progress.pack(side=tkinter.RIGHT, padx=10, pady=5)

        reload_button = tkinter.Button(buttons_frame, text='Поменять текст',
                                       font=('Arial', 12),
                                       command=self.keyboard_tutor.reload_text)
        reload_button.pack(side=tkinter.LEFT, padx=10, pady=5)

    def change_sound_state(self, event):
        if self.is_sound_off:
            self.is_sound_off = False
            self.sound_button.config(image=self.volume_image)
            self.keyboard_tutor.sound_on()
        else:
            self.is_sound_off = True
            self.sound_button.config(image=self.volume_mute_image)
            self.keyboard_tutor.sound_off()


main = MainWindow()
main.mainloop()
