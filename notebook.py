import datetime

# Store the next availabel id for all new notes

last_id = 0

class Note:

    def __init__(self, memo, tags =""):

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id +=1
        self.id = last_id

    def match(self, filter):

        return self.filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        """Initialize a Notebook with and empty list."""
        self.notes = []


    def new_note(self, memo, tags = ""):
        """ICreate a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and chage its tags as
        to the given value"""
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_memo(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        """ find all notes that mathc the given filter string """
        return [note for note in self.notes if note.match(filter)]
