from pyscript import display, document

class addingClassmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject
        
    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}! My favorite subject is {self.subject}."

previousClassmate = [
    addingClassmate("Sean Cotioco", "Topaz", "Filipino"),
    addingClassmate("Sang-Heon Choi", "Topaz", "CAT"),
    addingClassmate("Prince Gano", "Topaz", "SS"),
    addingClassmate("Jalainie Abdullah", "Topaz", "Glee"),
    addingClassmate("Renzo", "Topaz", "ICT"),
    ]

classmates = []


def addClassmate(e):
    output = document.getElementById("output")
    output.innerHTML = ""
    
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value
    
    if name and section and subject:
        classmate = addingClassmate(name, section, subject)
        classmates.append(classmate)
        
        display(f"{name} has been added to the list.", target="output")
    else:
        display("Please fill in all the fields.", target="output")


def showList(e):
    output = document.getElementById("output")
    output.innerHTML = ""
    
    if previousClassmate:
        for i in previousClassmate:
            display(i.introduce(), target="output")
    if classmates:
        for i in classmates:
            display(i.introduce(), target="output")