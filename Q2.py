from datetime import * # Il y avait une seule chose d'importée, il fallait faire un *
import locale
locale.setlocale(locale.LC_TIME,'')

def afficher_jours_examens(horaire_examen: dict) -> list[str]:
    """
    Cette fonction sert à extraire les jours de la semaines où il y a des examens
    :param horaire_examen: dictionnaire contenant les dates d'examens
    :return: une liste de jours de la semaine
    """
    jours = [] # Ça retournait toujours juste le dernier quand il était à l'interieur de la fonction.
    for i, date_examen in horaire_examen.items(): # https://projets420.gitbook.io/notes-de-cours/les-collections-de-donnees/les-dictionnaires Parcourir : for cle, valeur in dict.items()
        date = datetime.strptime(horaire_examen[i], "%d/%m/%Y") # Ce n'est pas année/mois/jour c'est supposé être jour/mois/année

        j = date.strftime("%a")
        jours.append(j)
    return jours # Ça retournait toujours juste le premier avant que je le bouge en arrière.

if __name__ == '__main__':
    horaire_examen = {
        "math" : "10/12/2015",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    print("Les examens sont :", ", ".join(afficher_jours_examens(horaire_examen)))
