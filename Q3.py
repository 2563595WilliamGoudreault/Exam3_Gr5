# - Pseudocode -
#
# Fonction qui vérifie si les mots sont au moins 3 lettres de long

# Fonction qui supprime les toutes les lettres des mots à part les 2 avant-dernières
# Fonction qui valide les mots
#
# print validées
#print altérée



messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}


def message_supprimer():
    """
    Fonction qui supprime toutes les lettres à part les 2 avant-dernières
    :return:
    """
        for mot in mots:
            if len(mot) >= 3:
                resultat += mot[-3] + mot[-2]  # https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
        return


def message_valider():
    """
    Fonction qui valide les résultats
    :return:
    """
    return

if __name__ == '__main__':
    print("Messages avec signatures validées :")
    print(messages_validees)
    print("-" * 40)
    print("Messages altérés, signatures non valides :")
    print(messages_alterees)

#messages_gr5_copie = messages_gr5.copy()

#print(messages_gr5_copie["messages"])


#print("La réponse est 142" in messages_gr5_copie["messages"])





