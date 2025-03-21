from mido import MidiFile, MidiTrack, Message
import math

# Create MIDI file and tracks
midi = MidiFile()
melody_track = MidiTrack()
chord_track = MidiTrack()
midi.tracks.append(melody_track)
midi.tracks.append(chord_track)

# Set instruments (Piano)
melody_track.append(Message('program_change', program=0, time=0))
chord_track.append(Message('program_change', program=0, time=0))

# Define note and duration function
def add_note(track, note, duration, velocity=64):
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=duration))

def add_chord(track, chord, duration, velocity=64):
    for note in chord:
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
        track.append(Message('note_off', note=note, velocity=velocity, time=duration))

# Define duration values
quarter = 960  # Quarter note duration
half = quarter * 2  # Half note duration
triplet = math.floor(quarter / 3)  # triplet note duration
eight = math.floor(quarter / 4)  # triplet note duration

# Melody Notes (A harmonic minor motif)
melody_notes = [
    (64, quarter),  # E
    (65, quarter),  # F
    (68, quarter),  # G#
    (69, quarter),  # A
    (68, quarter),  # G#
    (64, quarter),  # E
    (62, quarter),  # D
    (62, quarter),  # D
    (60, quarter),  # C
    (57, quarter)   # A
]

# Chord Progression (A harmonic minor)
chords = [
    [57, 60, 64],  # A minor (A – C – E)
    [57, 60, 64],  # A minor (A – C – E)
    [56, 59, 62],  # G# diminished (G# – B – D)
    [53, 57, 60],  # F major (F – A – C)
    [52, 56, 59],   # E major (E – G# – B)
]

# Add melody to track
for note, duration in melody_notes:
   add_note(melody_track, note, duration)

# Add chords
#for chord in chords:
#    for note in chord:
#        add_note(chord_track, note, half)

for chord in chords:
    add_chord(chord_track, chord, half)

# Save MIDI file
file_name = "harmonic_minor_motif_with_chords.mid"
midi.save(file_name)
print(f"MIDI file saved as {file_name}")
