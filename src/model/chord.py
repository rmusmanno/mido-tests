from typing import List

from misc.enums import Notes, Accents
from model.note import Note

class Chord:
    base_note:Notes
    accent:Accents

    notes: List[Note] = []