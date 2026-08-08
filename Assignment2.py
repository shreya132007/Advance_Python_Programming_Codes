# TITLE : Advanced Class Concepts – Decorators and Magic methods

"""
Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to
customize and format reports. The system should allow users to define report templates and apply various
formatting options dynamically.
"""

# Decorator
def message(func):
    def show(self):
        print("Report is Ready")
        func(self)
    return show


class Report:

    template = "Simple Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return "Title : " + self.title + "\nContent : " + self.content

    @message
    def display(self):
        print("Template :", Report.template)
        print(self)


# Main Program
r1 = Report("Student Report", "Marks are good.")

print("Before Changing Template")
r1.display()

Report.change_template("College Report")

print("\nAfter Changing Template")
r1.display()

#output
# Before Changing Template
# Report is Ready
# Template : Simple Report
# Title : Student Report
# Content : Marks are good.

# After Changing Template
# Report is Ready
# Template : College Report
# Title : Student Report
# Content : Marks are good.