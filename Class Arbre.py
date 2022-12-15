class arbre_avec_liste:
    def __init__(self):
        self.liste = [None]

    def ajouter_niveau(self):
        for i in range(2** ((len(self.liste) -1) // 2)):
            self.liste.append(None)

    def ajouter_racine(self, valeur):
        self.liste[0] = valeur

    def ajouter_fg(self, indice_parent, valeur):
        self.liste[2 * indice_parent + 1] = valeur

    def ajouter_fd(self, indice_parent, valeur):
        self.liste[2 * indice_parent + 1] = valeur

    def calculer_taille(self):
        nb_noeud = 0
        for noeud in self.liste:
            if noeud is not None:
                nb_noeud += 1
        return nb_noeud

    def calculer_hauteur(self):
        hauteur = 0
        while 2**hauteur -1 <len(self.liste):
            hauteur += 1
        return hauteur




