import mido
from time import sleep

# Create a new MIDI file and track
midi = mido.MidiFile()
track = mido.MidiTrack()
midi.tracks.append(track)

# Set instrument to piano (program 0)
track.append(mido.Message('program_change', program=0, time=0))

def note(note,velocity=64, time=0):
    return mido.Message('note_on', note=note, velocity=velocity, time=time)

def note_off(note, duration, velocity=64, time=480):
    return mido.Message('note_off', note=note, velocity=velocity, time=time*duration)

def majorChord(root, duration):
    track.append(note(root))
    track.append(note(root+4))
    track.append(note(root+7))
    track.append(note_off(root, duration))
    track.append(note_off(root+4, duration))
    track.append(note_off(root+7, duration))

def minorChord(root, duration):
    track.append(note(root))
    track.append(note(root+3))
    track.append(note(root+7))
    track.append(note_off(root, duration))
    track.append(note_off(root+3, duration))
    track.append(note_off(root+7, duration))

C = 60 
G = 55 
A = 57 
F = 53 

majorChord(C,1)
majorChord(G,1)
minorChord(A,1)
majorChord(F,1)
majorChord(F,1)
majorChord(G,1)
majorChord(C,2)

# Save MIDI file
file_name = "chord_test.mid"
midi.save(file_name)
print(f"MIDI file saved as {file_name}")