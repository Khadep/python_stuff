from datetime import date
import datetime

#store the next available id for all new notes
task_id  = 0
class Tasklist:
    """represent a collection of tasks that can be dated, modified, and searched"""
    def __init__(self):
        """initialie a tasklist with an empty list."""
        self.tasks =[]

    def new_task(self, item, day=""):
        """create a new note and add it to a list."""
        if day:
            self.day = day
        else:
            self.day = date.today()
        self.tasks.append(Task(item, day))

    def modify_task(self, task_id, item):
        """Find the note with the given id and change its memo to the given value."""
        task = self._find_task(task_id)
        if task:
            task.item = item
            return True
        return False

    def modify_day(self, task_id, day):
        """find the note with the given id and change its tags to the given value."""
        self._find_task(task_id).day = day

    def _find_task(self, task_id):
        """LOcate the note with the given id."""
        for task in self.tasks:
            if str(task.id) == str(task.id):
                return task
        return None

    def modify_status(self, task_id, status):
            """Find the note with the given id and change its memo to the given value."""
            task = self._find_task(task_id)
            if task:
                task.status = status
                return True
            return False   
    


    def search(self, filter):
        """find all notes that match the given filter string."""
        return [task for task in self.tasks if task.match(filter)]

class Task:
    """REpresent a note in a notebook. Match against a string in searches and store tags for each note."""
    def __init__(self, item, day ='', status="Incomplete"):
        """inititalize a note with memo and optional space-separated tags. AUtomatically set the note's creation date and a unique id."""
        self.item = item
        if day:
            self.day = day
        else:
            self.day = date.today().isoformat()
        self.creation_date = datetime.date.today()
        global task_id
        task_id += 1
        self.id = task_id
        self.status = status

    def match(self, filter):
        """Determine if this note matches the filter text. Return True if it matches, false otherwise. Search is case sensitive ad matches both text and tags."""
        return filter in self.item or filter in self.day

