class Voiture:
    def _init_(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficher_infos(self):
        print("Matricule :", self.matricule)
        print("Marque :", self.marque)
        print("Couleur :", self.couleur)
class Parc:
    def _init_(self, id, adresse, capacite, liste_voitures):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voitures = liste_voitures

    def afficher_infos(self):
        print("ID :", self.id)
        print("Adresse :", self.adresse)
        print("Capacite :", self.capacite)
        print("Liste des voitures :")
        for v in self.liste_voitures:
            v.afficher_infos()
            print("------")

    def entrerVoiture(self, voiture):
        if voiture in self.liste_voitures:
            print("La voiture existe deja dans le parc")
        elif len(self.liste_voitures) >= self.capacite:
            print("Le parc est plein")
        else:
            self.liste_voitures.append(voiture)
            print("Voiture ajoutee au parc")

    def sortirVoiture(self, voiture):
        if voiture not in self.liste_voitures:
            print("La voiture n'est pas dans le parc")
        else:
            self.liste_voitures.remove(voiture)
            print("Voiture retiree du parc")

