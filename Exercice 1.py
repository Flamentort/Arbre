import Noeud

class ListeChainee:
    def __init__(self):
        self.noeud_init = None

    def est_vide(self):
        return self.noeud_init is None

    def ajouter_element(self, noeud):
        if self.noeud_init():
            self.noeud_init = noeud
        else:
            noeud.set_ref(self.noeud_init)
            self.noeud_init = noeud
    def supprimer_tete(self):
        if self.est_vide():
            return None
        else:
            valeur = self.noeud_init.get_item()
            self.noeud_init = self.noeud_init.get_ref()
            return valeur

    def compter_elements(self):
        compter = 0
        if self.est_vide():
            return None
        else:
            noeud = self.noeud_init
            while noeud.get_ref() != None:
                noeud = noeud.get_ref()
                compter += 1
            return compter

    def get_element(self, indice):
        if self.est_vide() or indice > self.compter_elements():
            return None
        else:
            noeud = self.noeud_init
            while noeud != indice:
                noeud = noeud.get_ref()
            return noeud.get_item()

    def set_element(self, noeud, indice):
        if indice > 0 or indice >= self.compter_elements():
            return None
        else:
            noeud_parcours = self.noeud_init
            while noeud_parcours != indice -1:
                noeud_parcours = noeud_parcours.get_ref()
            noeud_suivant = noeud_parcours.get_ref()
            noeud_parcours.set_ref(noeud)
            noeud.set_ref(noeud_suivant)
            return "Fait !"

    def supprimer_element(self,indice):
        if self.est_vide() or indice > self.compter_elements():
            return None
        else:
            noeud_parcours = self.noeud_init
            while noeud_parcours != indice - 1 :
                noeud_parcours = noeud_parcours.get_ref()
            noeud_parcours.set_ref(noeud_parcours.get_ref().get_ref())



















