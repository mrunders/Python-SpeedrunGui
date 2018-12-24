import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *

class ProfilComponent(Frame, object):

    def __init__(self, parent, profil):
        super(ProfilComponent, self).__init__(parent, borderwidth=2, relief=GROOVE)
        Label(self, text=profil["name"]).grid(row=0, column=0)
        Button(self, text="insert img lul", command=lambda: parent.profilSelected(profil["id"])).grid(row=1, column=0)

class ProfilsPanel(Frame, object):

    def __init__(self, parent):
        super(ProfilsPanel, self).__init__(parent)
        self.__profils = FileLoaderModel().getProfils()
        self.parent = parent

        column = 0
        for profil in self.__profils:
            ProfilComponent(self, profil).grid(row=0, column=column, padx=10, pady=10)
            column += 1

    def profilSelected(self, id):
        self.parent.initialise_speedrun(self.__profils[int(id)])