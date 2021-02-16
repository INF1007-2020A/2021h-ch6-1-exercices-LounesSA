#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    pass
    if values is None:
        # TODO: demander les valeurs ici
        values=[]
        while len(values)<10:
            values.append(input("Entrez une valeur : "))
        values.sort()

    return print(values)


def anagrams(words: list = None) -> bool:

    if words is None:
        # TODO: demander les mots ici
        is_anagram = True
        words = []
        a = str(input("Entrez un mot"))
        words.append(a)
        b = str(input("Entrez un deuxième mot"))
        words.append(b)
        if len(words[0]) != len(words[1]) :
            is_anagram = False

        for lettres in words[0] :
            if lettres not in words[1] :
                is_anagram = False
                break
            else:
                is_anagram = True

    return print(is_anagram)


def contains_doubles(items: list) -> bool:
    count = 0
    contient_doublons = True
    for elements in items :
        for i in range(len(items)) :
            if elements == items[i]:
                count+=1
    if count==1 :
        contient_doublons = False


    return contient_doublons


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key,value in student_grades.items():
        average = sum(value)/len(value)

        if len(best_student) == 0 or list(best_student.values())[0]<average:
            best_student = {key: average}

    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequence = {letter : sentence.count(letter) for letter in sentence}
    sorted_keys = sorted(frequence, reverse = True, key=frequence.__class_getitem__())
    for key in sorted_keys :
        if frequence[key]>5 :
            print(f"Le caracte)


    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
