import sys

from to_do_list import Tasklist, Task

class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.tasklist = Tasklist()
        self.choices = {
            "1": self.show_tasks,
            "2": self.search_tasks,
            "3": self.add_task,
            "4": self.modify_task,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        
        To do list Menu
        
        1. Show all Tasks
        2. Search Tasks
        3. Add Task
        4. Modify Task
        5. Quit
        """)

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_tasks(self, tasks=None):
        if not tasks:
            tasks = self.tasklist.tasks
        for task in tasks:
            print ("{0}: {1}\n{2} status:{3}".format(
                task.id, task.day, task.item, task.status))

    def search_tasks(self):
        filter = input("Search for: ")
        tasks = self.tasklist.search(filter)
        self.show_tasks(tasks)

    def add_task(self):
        item = input("Enter a item: ")
        self.tasklist.new_task(item)
        print("Your note has been added.")

    def modify_task(self):
        id = input("Enter a task id:")
        item = input("Enter a item: ")
        day = input("Enter date \"year-day-month\" format: ")
        status = input("Enter the status of this item")
        if item:
            self.tasklist.modify_task(id, item)
        if day:
            self.tasklist.modify_day(id, day)
        if status:
            self.tasklist.modify_status(id, status)

    def quit(self):
        print("THank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()