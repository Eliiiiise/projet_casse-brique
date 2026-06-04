'''
Ce fichier gère les meilleurs scores du jeu.

Il est responsable de :
- charger les scores sauvegardés (load_scores()) ;
- enregistrer les nouveaux scores (save_scores()) ;
- trier les scores du plus grand au plus petit (add_score()) ;
- conserver uniquement les 3 meilleurs résultats (get_top3()). 

Les données sont stockées dans un fichier afin de pouvoir
être conservées entre plusieurs exécutions du programme.
'''
import json # permet de lire et écrire des données au format JSON, utilisé pour stocker les scores dans un fichier
import os # permet de vérifier si un fichier existe déjà

class Scoreboard:

    def __init__(self):

        # nom du fichier contenant les scores
        self.file_name = "highscores.json"

        # charge les scores existants au démarrage
        self.scores = self.load_scores()


    def load_scores(self):
        """
        Charge les scores depuis le fichier JSON.
        """

        # vérifie si le fichier existe
        if not os.path.exists(self.file_name):
            return []

        # ouvre le fichier en lecture
        with open(self.file_name, "r", encoding="utf-8") as file:

            # transforme le JSON en liste Python
            return json.load(file)


    def save_scores(self):
        '''
        Enregistre les scores dans le fichier JSON.
        '''
        # ouvre le fichier en écriture
        with open(self.file_name, "w", encoding="utf-8") as file:

            # écrit les données dans le fichier
            json.dump(self.scores, file, indent=4)


    def add_score(self, name, score):
        '''
        Ajoute un nouveau score à la liste, trie les scores et conserve uniquement le top 3.
        '''

        # ajoute le joueur à la liste
        self.scores.append({
            "name": name,
            "score": score
        })

        # trie du plus grand score au plus petit
        self.scores.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        # conserve uniquement le top 3
        self.scores = self.scores[:3]

        # met à jour le fichier JSON
        self.save_scores()


    def get_top_scores(self):
        ''' 
        Retourne la liste des meilleurs scores. 
        '''
        return self.scores