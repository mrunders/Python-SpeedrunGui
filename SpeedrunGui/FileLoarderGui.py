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
    
    file_name = "SpeedrunGui_profils.xml"

    def __init__(self, profil="0", path="./"):
        self.profil = profil
        self.path = path
        self.xmltree = etree.parse(self.path + self.file_name)

    def update_best_segment(self, segment):
        id_level = segment.get_id()
        elt = self.xmltree.xpath("/speedrunGui-Project/profil[@id='%s']/data/level[@id='%s']" % (self.profil, id_level))[0]
        elt.set("best-segment", segment.get_best_segment_str()) 
    
    def commit_changes(self):
        file = open(self.path + self.file_name, "w")
        file.write(etree.tostring(self.xmltree))
        file.close()
