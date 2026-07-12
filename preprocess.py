from music21 import converter, note, chord
import glob

notes = []

for file in glob.glob("midi/*.mid"):
    print("Reading:", file)

    midi = converter.parse(file)

    for element in midi.flatten().notes:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

print("\nTotal notes extracted:", len(notes))
print("First 20 notes:")
print(notes[:20])