class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficher_infos(self):
        print("Matricule :", self.matricule)
        print("Marque :", self.marque)
        print("Couleur :", self.couleur)


class Parc:
    def __init__(self, id, adresse, capacite, liste_voitures):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voitures = liste_voitures
