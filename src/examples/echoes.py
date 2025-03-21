from mido import MidiFile, MidiTrack, Message

# Create a new MIDI file and track
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Set instrument to piano (program 0)
track.append(Message('program_change', program=0, time=0))

# Define note and duration function
def add_note(note, duration, velocity=64):
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=duration))

# Define quarter note duration (480 ticks)
quarter = 480

# Melody Notes (A harmonic minor motif)
melody_notes = [
    (64, quarter),  # E
    (65, quarter),  # F
    (68, quarter),  # G#
    (69, quarter),  # A (Pause here in real play)
    (69, quarter),  # A (Pause here in real play)
    (68, quarter),  # G#
    (64, quarter),  # E
    (62, quarter),  # D
    (60, quarter),  # C
    (57, quarter)   # A (Final resolution)
]

# Add melody to MIDI track
for note, duration in melody_notes:
    add_note(note, duration)

# Save the MIDI file
file_name = "harmonic_minor_motif.mid"
midi.save(file_name)
print(f"MIDI file saved as {file_name}")
