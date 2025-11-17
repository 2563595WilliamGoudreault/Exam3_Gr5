import pytest
from Q2 import *

def test_jour_valide_1():
    """
    Teste avec ce qui est déjà écrit dans Q2.
    :return:
    """
    horaire_examen = {
    "math": "10/12/2015",
    "anglais": "12/12/2025",
    "français": "15/12/2025"
    }
    resultat = afficher_jours_examens(horaire_examen)
    assert resultat == ['jeu.', 'ven.', 'lun.']

def test_jour_valide_2():
    """
    Teste avec un jour en arrière comparé à Q2.
    :return:
    """
    horaire_examen = {
    "math": "09/12/2015",
    "anglais": "11/12/2025",
    "français": "14/12/2025"
    }
    resultat = afficher_jours_examens(horaire_examen)
    assert resultat == ['mer.', 'jeu.', 'dim.']



def test_jour_invalide():
    """
    Teste avec des dates invalides (retourne FAILED comme supposé)
    :return:
    """
    horaire_examen = {
        "math" : "99/99/9999",
        "anglais" : "88/88/8888",
        "français" : "77/77/777"
    }
    resultat = afficher_jours_examens(horaire_examen)

    assert resultat == ['jeu.', 'ven.', 'lun.']
