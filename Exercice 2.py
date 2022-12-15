class Noeud:
    def __init__(self, val):
        self.valeur = val
        self.fg = None
        self.fd = None

    def greffer_fg(self, val):
        self.fg = Noeud(val)

    def greffer_fd(self, val):
        self.fd = Noeud(val)

    def est_une_feuille(self):
        return (self.fg is None) and (self.fd is None)

    def est_peigne_gauche(self):
        noeud = self
        while noeud.fg is not None:
            if noeud.fd is not None:
                return False
            noeud = noeud.fg
        return True

    def est_peigne_droit(self):
        noeud = self
        while noeud.fd is not None:
            if noeud.fg is not None:
                return False
            noeud = noeud.fd
        return True
