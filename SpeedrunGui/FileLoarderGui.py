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

class FileWritterModel():
    
    path = "./"
    file_name = "SpeedrunGui_profils.xml"
    xmltree = etree.parse(path + file_name)
    profil = None

    @staticmethod
    def init(xmltree, profil, path="./"):
        profil = profil
        xmltree = xmltree

    @staticmethod
    def update_best_segment(id_level, new_best_segment):
        elt = xmltree.xpath("/speedrunGui-Project/profil[@id='%s']/data/level[@id='%s']" % (profil, id_level))[0]
        elt.set("best-segment", "0"+new_best_segment.__str__()) 
    
    @staticmethod
    def save_update():
        file = open(path + file_name, "w")
        file.write(etree.tostring(xmltree))
        file.close()
