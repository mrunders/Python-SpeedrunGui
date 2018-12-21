from Tkinter import *
from lxml import etree

class FileLoaderModel():

    file_name = "SpeedrunGui_profils.xml"
    profils = list()

    def __init__(self, path="./"):
        self.__path = path
        self.__xmltree = etree.parse(path + self.file_name)

        self.load_profils()

    def elts_to_dict(self, profil):
        childrens = profil.getchildren()
        result = dict((elt.tag, elt.text.strip()) for elt in childrens)
        result["id"] = profil.get("id")
        result["data"] = self.__xmltree.xpath("profil[@id=%s]/data" % result["id"])[0]
        return result

    def load_profils(self):
        for profil in self.__xmltree.xpath("/speedrunGui-Project/profil"):
            self.profils.append(self.elts_to_dict(profil))

    def getProfils(self):
        return self.profils
    
class ProfilComponent(Frame, object):

    def __init__(self, parent, profil):
        super(ProfilComponent, self).__init__(parent, borderwidth=2, relief=GROOVE)
        Label(self, text=profil["name"]).grid(row=0, column=0)
        but = Button(self, text="insert img lul", command=lambda: parent.profilSelected(profil["id"]))
        but.grid(row=1, column=0)


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
        self.parent.initialise_speedrun(self.__profils[int(id)]['data'].getchildren())
