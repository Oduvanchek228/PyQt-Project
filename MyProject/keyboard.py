import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from pygame import mixer

mixer.init()

c3 = mixer.Sound('notes/C3.wav')
d3 = mixer.Sound('notes/D3.wav')
e3 = mixer.Sound('notes/E3.wav')
f3 = mixer.Sound('notes/F3.wav')
g3 = mixer.Sound('notes/G3.wav')
a3 = mixer.Sound('notes/A3.wav')
b3 = mixer.Sound('notes/B3.wav')

c4 = mixer.Sound('notes/C4.wav')
d4 = mixer.Sound('notes/D4.wav')
e4 = mixer.Sound('notes/E4.wav')
f4 = mixer.Sound('notes/F4.wav')
g4 = mixer.Sound('notes/G4.wav')
a4 = mixer.Sound('notes/A4.wav')
b4 = mixer.Sound('notes/B4.wav')

c5 = mixer.Sound('notes/C5.wav')
d5 = mixer.Sound('notes/D5.wav')
e5 = mixer.Sound('notes/E5.wav')
f5 = mixer.Sound('notes/F5.wav')
g5 = mixer.Sound('notes/G5.wav')
a5 = mixer.Sound('notes/A5.wav')
b5 = mixer.Sound('notes/B5.wav')

c6 = mixer.Sound('notes/C6.wav')
d6 = mixer.Sound('notes/D6.wav')
e6 = mixer.Sound('notes/E6.wav')
f6 = mixer.Sound('notes/F6.wav')
g6 = mixer.Sound('notes/G6.wav')
a6 = mixer.Sound('notes/A6.wav')
b6 = mixer.Sound('notes/B6.wav')

c7 = mixer.Sound('notes/C7.wav')

csharp3 = mixer.Sound('notes/c#3.wav')
dsharp3 = mixer.Sound('notes/d#3.wav')
fsharp3 = mixer.Sound('notes/f#3.wav')
gsharp3 = mixer.Sound('notes/g#3.wav')
asharp3 = mixer.Sound('notes/a#3.wav')

csharp4 = mixer.Sound('notes/c#4.wav')
dsharp4 = mixer.Sound('notes/d#4.wav')
fsharp4 = mixer.Sound('notes/f#4.wav')
gsharp4 = mixer.Sound('notes/g#4.wav')
asharp4 = mixer.Sound('notes/a#4.wav')

csharp5 = mixer.Sound('notes/c#5.wav')
dsharp5 = mixer.Sound('notes/d#5.wav')
fsharp5 = mixer.Sound('notes/f#5.wav')
gsharp5 = mixer.Sound('notes/g#5.wav')
asharp5 = mixer.Sound('notes/a#5.wav')

csharp6 = mixer.Sound('notes/c#6.wav')
dsharp6 = mixer.Sound('notes/d#6.wav')
fsharp6 = mixer.Sound('notes/f#6.wav')
gsharp6 = mixer.Sound('notes/g#6.wav')
asharp6 = mixer.Sound('notes/a#6.wav')

keymap = {'C3': c3,
          'D3': d3,
          'E3': e3,
          'F3': f3,
          'G3': g3,
          'A3': a3,
          'B3': b3,
          'C#3': csharp3,
          'D#3': dsharp3,
          'F#3': fsharp3,
          'G#3': gsharp3,
          'A#3': asharp3,
          'C4': c4,
          'D4': d4,
          'E4': e4,
          'F4': f4,
          'G4': g4,
          'A4': a4,
          'B4': b4,
          'C#4': csharp4,
          'D#4': dsharp4,
          'F#4': fsharp4,
          'G#4': gsharp4,
          'A#4': asharp4,
          'C5': c5,
          'D5': d5,
          'E5': e5,
          'F5': f5,
          'G5': g5,
          'A5': a5,
          'B5': b5,
          'C#5': csharp5,
          'D#5': dsharp5,
          'F#5': fsharp5,
          'G#5': gsharp5,
          'A#5': asharp5,
          'C6': c6,
          'D6': d6,
          'E6': e6,
          'F6': f6,
          'G6': g6,
          'A6': a6,
          'B6': b6,
          'C#6': csharp6,
          'D#6': dsharp6,
          'F#6': fsharp6,
          'G#6': gsharp6,
          'A#6': asharp6,
          'C7': c7
          }

notes_names = [note for note in keymap.keys() if '#' not in note]
sharp_notes_names_1 = [note for note in keymap.keys() if 'C#' in note or 'D#' in note]
sharp_notes_names_2 = [note for note in keymap.keys() if '#' in note and 'C#' not in note and 'D#' not in note]


class Keyboard(QWidget):
    def __init__(self):
        super(Keyboard, self).__init__()

        self.setWindowTitle('Синтезатор MIDI')
        self.setFixedSize(1044, 300)
        self.setStyleSheet('QWidget { background-color: gray }')
        self.notes = [name for name in keymap.keys()]
        self.standard_notes = [note for note in keymap.values()]
        self.effect1_notes = [mixer.Sound('effect_1/c3_1.wav'), mixer.Sound('effect_1/d3_1.wav'),
                              mixer.Sound('effect_1/e3_1.wav'), mixer.Sound('effect_1/f3_1.wav'),
                              mixer.Sound('effect_1/g3_1.wav'),
                              mixer.Sound('effect_1/a3_1.wav'), mixer.Sound('effect_1/b3_1.wav'),
                              mixer.Sound('effect_1/C#3_1.wav'), mixer.Sound('effect_1/D#3_1.wav'),
                              mixer.Sound('effect_1/F#3_1.wav'),
                              mixer.Sound('effect_1/G#3_1.wav'), mixer.Sound('effect_1/A#3_1.wav'),
                              mixer.Sound('effect_1/C4_1.wav'), mixer.Sound('effect_1/D4_1.wav'),
                              mixer.Sound('effect_1/E4_1.wav'),
                              mixer.Sound('effect_1/F4_1.wav'), mixer.Sound('effect_1/G4_1.wav'),
                              mixer.Sound('effect_1/A4_1.wav'), mixer.Sound('effect_1/B4_1.wav'),
                              mixer.Sound('effect_1/C#4_1.wav'),
                              mixer.Sound('effect_1/D#4_1.wav'), mixer.Sound('effect_1/F#4_1.wav'),
                              mixer.Sound('effect_1/G#4_1.wav'), mixer.Sound('effect_1/A#4_1.wav'),
                              mixer.Sound('effect_1/C5_1.wav'),
                              mixer.Sound('effect_1/D5_1.wav'), mixer.Sound('effect_1/E5_1.wav'),
                              mixer.Sound('effect_1/F5_1.wav'), mixer.Sound('effect_1/G5_1.wav'),
                              mixer.Sound('effect_1/A5_1.wav'),
                              mixer.Sound('effect_1/B5_1.wav'), mixer.Sound('effect_1/C#5_1.wav'),
                              mixer.Sound('effect_1/D#5_1.wav'), mixer.Sound('effect_1/F#5_1.wav'),
                              mixer.Sound('effect_1/G#5_1.wav'),
                              mixer.Sound('effect_1/A#5_1.wav'), mixer.Sound('effect_1/C6_1.wav'),
                              mixer.Sound('effect_1/D6_1.wav'), mixer.Sound('effect_1/E6_1.wav'),
                              mixer.Sound('effect_1/F6_1.wav'),
                              mixer.Sound('effect_1/G6_1.wav'), mixer.Sound('effect_1/A6_1.wav'),
                              mixer.Sound('effect_1/B6_1.wav'), mixer.Sound('effect_1/C#6_1.wav'),
                              mixer.Sound('effect_1/D#6_1.wav'),
                              mixer.Sound('effect_1/F#6_1.wav'), mixer.Sound('effect_1/G#6_1.wav'),
                              mixer.Sound('effect_1/A#6_1.wav'), mixer.Sound('effect_1/C7_1.wav')]

        for n, note in enumerate(notes_names):
            button = QPushButton(self)
            button.setFixedSize(36, 210)
            button.setStyleSheet('QPushButton {background-color: white}')
            button.setText(note)
            button.move(n * 36, 90)
            button.clicked.connect(self.play)

        count = 0
        for n, note in enumerate(sharp_notes_names_1):
            button = QPushButton(self)
            button.setFixedSize(18, 150)
            button.setStyleSheet('QPushButton {background-color: black}')
            button.setText(note)
            button.clicked.connect(self.play)
            if ((n + 1) != 3) and ((n + 1) != 5) and ((n + 1) != 7):
                button.move(((n + 1) * 30) + count, 90)
            else:
                count += 193
                button.move(((n + 1) * 30) + count, 90)

        count = 110

        for n, note in enumerate(sharp_notes_names_2):
            button = QPushButton(self)
            button.setFixedSize(18, 150)
            button.setStyleSheet('QPushButton {background-color: black}')
            button.clicked.connect(self.play)
            button.setText(note)
            if ((n + 1) != 4) and ((n + 1) != 7) and ((n + 1) != 10):
                button.move(((n + 1) * 30) + count, 90)
            else:
                count += 162
                button.move(((n + 1) * 30) + count, 90)

        self.record_btn = QPushButton(self)
        self.record_btn.setText('▶️')
        self.record_btn.setStyleSheet('QWidget { background-color: red }')
        self.record_btn.move(580, 50)
        self.record_btn.clicked.connect(self.record)

        self.effect1_btn = QPushButton(self)
        self.effect1_btn.setText('Эффект №1')
        self.effect1_btn.move(380, 50)
        self.effect1_btn.setStyleSheet('QWidget { background-color: white }')
        self.effect1_btn.clicked.connect(self.effect_1)

        self.effect2_btn = QPushButton(self)
        self.effect2_btn.setText('Эффект №2')
        self.effect2_btn.setStyleSheet('QWidget { background-color: white }')
        self.effect2_btn.move(480, 50)

        self.back_btn = QPushButton(self)
        self.back_btn.setText('Без эффектов')
        self.back_btn.setStyleSheet('QWidget { background-color: white }')
        self.back_btn.move(280, 50)
        self.back_btn.clicked.connect(self.back)

    def play(self):
        note = keymap[self.sender().text()]
        note.play()

    def back(self):
        for n, note in enumerate(self.standard_notes):
            keymap[self.notes[n]] = note

    def effect_1(self):
        for n, note in enumerate(self.effect1_notes):
            keymap[self.notes[n]] = note

    def record(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Keyboard()
    ex.show()
    sys.exit(app.exec())
