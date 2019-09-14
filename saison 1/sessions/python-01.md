# Introduction à la programmation avec Python (chapitre 1)



<p align="right">
E2L <br />
24/11/2018 <br />
Dimitri Merejkowsky <br />
</p>

---

# Plan

* Présentation et historique du langage
* L'interpréteur interactif
* Un jeu simple

---

# Historique

* Créé par Guido van Rossum. Conçu à la base pour l'enseignement.
* Le nom vient des Monty Python (si, si)
* Python 1: Sortie en 1991
* Python 2: en 2000
* Python 3: en 2008



---

# Le grand schisme

La plupart des langages continuent à être compatibles d'une version à l'autre.

*Ce n'est pas le cas pour Python3*, et ça a causé beaucoup de confusion et de débats.

Heureusement, 10 ans plus tard, la situation s'est arrangée.

---

# Python3

Ce cours fonctionne donc uniquement avec Python3.

N'utilisez *pas* Python2, sinon certaines choses expliquées ici ne marcheront pas :/

---

# Utilisation de Python

* Aussi appelé "langage de script", `glue language`

* Bon partout, excellent nulle part

* Exemples d'utilisation:

    * Sciences (physique, chimie, linguistique ...)
    * Animation (Pixar, Disney ...)
    * Sites web (journaux, youtube, ...)
    * Ligne de commande
    * ...

---

# Installation

---

# L'interpréteur interactif



    !pycon
    $ python3
    Python 3.7.1 (default, Oct 22 2018, 10:41:28)
    [GCC 8.2.1 20180831] on linux
    Type "help", "credits" or "license" for more information.
    >>>

---

# Note


À partir de maintenant, recopiez les entrées sur les slides dans votre propre
interpréteur.

Vous devez taper la même chose après l'invite de commande ('>>>') et vous devez voir les mêmes réponses.

Si ce n'est pas le cas, prévenez moi!

---
# Entiers et maths simples

    !pycon
    >>> 1
    1
    >>> 2
    2
    >>> 1 + 2
    3
    >>> 2 * 3
    6

---

# Flottants

C'est le `.` qui fait le flottant

    !pycon
    >>> 0.5
    0.5
    >>> 0.5 + 0.2
    0.7
    >>> 10 / 3
    3.3333333333333335

*Note: les flottants sont imprécis*

----

# Division entières et modulo

    !pycon
    >>> 14 // 3
    4
    >>> 14 % 3
    2

*Le `%` n'a rien à voir avec un pourcentage!*

---

# Priorité des opérations


    !pycon
    >>> 1 + 2 * 3
    7
    >>> (1 + 2) * 3
    9

*Les parenthèses permettent de grouper les expressions*

---

# Variables

   !pycon
    >>> a = 2
    >>> a
    2
    >>> b = 3
    >>> a + b
    5

* On peut nommer des valeurs
* On peut afficher la valeur d'une variable entrant son nom dans le REPL

---

# Variables (2)


   !pycon
    >>> a = 2
    >>> a
    2
    >>> a = 3
    >>> a
    3

* On peut changer la valeur d'une variable (d'où son nom)

---

# Nom des variables

Préférez des noms longs et descriptifs

Toujours en minuscule

Séparez les "mots" par des tirets bas (underscore)

    !pycon
    >>> score = 42
    >>> medium_age = 22

---

# Les chaînes de caractères

Aussi appelées "string".


Avec des simple quotes (`'`)

    !pycon
    >>> 'Bonjour monde!'
    'Bonjour monde'

Marche aussi avec des double quotes (`"`)

    !pycon
    >>> "Bonjour, monde!"
    'Bonjour monde'



---

# Double et simple quotes

On peut mettre des simples quotes dans des double quotes et vice-versa.

    !pycon
    >>> "Il a dit: 'bonjour' ce matin."
    "Il a dit: 'bonjour' ce matin."

    >>> 'Il a dit: "bonjour" ce matin'
    'Il a dit: "bonjour" ce matin!'

---

# Échappement


Avec la barre oblique inversée "backslash"


    !pycon
    >>> 'Il a dit: "bonjour". C\'est sympa!'
    'Il a dit: "bonjour". C\'est sympa!'

---

# Concaténation


    !pycon
    >>> name = "John"
    >>> message = "Bonjour " + name + " !"
    >>> message
    "Bonjour John !"

---

# Types

    !pycon
    >>> a = 42
    >>> message = "La réponse est: " + a
    TypeError: can only concatenate str (not "int") to str

On ne mélange pas les torchons et les serviettes!

---

# Conversions


    !python
    # Entier vers string
    >>> a = 42
    >>> message = "La réponse est: " + str(a)
    >>> message
    'La réponse est 42'


    # String vers entier
    >>> answer = int("42")
    >>> answer
    42

Notez les parenthèses autour des valeurs.

---

# Booléens

True et False


En Python, elle sont en majuscules!

---

# Assignation

On peut assigner des variables aux valeurs True  et False


    !pycon
    >>> la_terre_est_plate = False
    ...
    >>> python_c_est_genial = True

---

# Comparaisons

    !pycon
    >>> a = 2
    >>> b = 3
    >>> a > b
    False

    >>> 2 + 2 == 4
    True

Note: `==` pour la comparaison, `=` pour l'assignation

---

# Comparaisons (2)

    !pycon
    >>> a = 2
    >>> b = 3
    >>> a != b
    True
    >>> 2 + 2 >= 4
    True

---

# Comparaisons (3)

    !pycon
    >>> a = 2
    >>> a < 2
    False
    >>> 1 < a < 3   # only in Python
    True

---
# Non persistance

    !pycon
    >>> a = 2
    >>> quit()

<span />

    !pycon
    >>> a
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'a' is not defined

*Notre premier message d'erreur !*


---

# Du code dans un fichier

Aussi appelé: "code source", ou "source".

L'essence du logiciel libre :)

---


# Installation d'un éditeur de texte simple

* Linux; `gedit`, `kate`, ...
* macOS: `CotEditor`
* Windows: `Notepad++`

J'insiste sur **simple**. Inutile d'installer un IDE pour le moment.

---

# Configuration

* Police de caractères à chasse fixe
* Indentation de *4 espaces*
* Remplacer tabulation par des espaces
* Activer la coloration syntaxique

---


# Notre premier fichier source


Insérez le code suivant dans votre éditeur de texte

    !python
    # Affiche un message
    print("Bonjour, monde")


Sauvegardez dans un fichier `bonjour.py` dans `Documents/e2l/python` par exemple

---

# Lancer du code en ligne de commande


    !console
    $ cd Documents/e2l/python/
    $ python3 bonjour.py
    Bonjour, monde

 * Les lignes commençant par dièse (`#`) ont été ignorées
 * `print()` affiche la valeur, comme dans le REPL.

---

# Note importante (1)

Vous avez juste besoin:

* d'un éditeur de texte
* de Python3 installé
* d'une ligne de commande

Pas la peine d'installer quoique ce soit de plus pour le moment

---

# Note importante (2)

À partir de maintenant, s'il y a marqué `# à recopier` en haut d'un exemple


1. *Recopiez* le code affiché dans votre éditeur, à la suite du code
   déjà écrit
2. Lancez le code depuis la ligne de commande
3. Réparez les erreurs éventuelles
4. Recommencez

---

# Note importante (3)

C'est le meilleur moyen d'apprendre. Si vous restez passifs vous retiendrez beaucoup moins de choses et ne pourrez pas coder par vous-même.

Profitez qu'on soit là pour vous aider si vous avez des erreurs que vous ne comprenez pas!

---

# Flot de contrôle

L'essence de la programmation!

---

# while

Répéter tant qu'une condition est vraie



    !python
    print("Bonjour, monde")
    while True:
        print("spam!")

Notes:

* deux points à la fin de la ligne
* indentation après les deux points
---

# Notre première boucle infinie


    !bash
    $ python bonjour.py
    Bonjour, monde
    spam!
    spam!
    spam!
    ....

CTRL-C pour interrompre

---

# Conditions

    !python
    a = 3
    b = 4
    if a == b:
        print("a et b sont égaux")
    else:
        print("a et be sont différents")

Rappel:

* deux points à la fin de la ligne
* indentation après les deux points

---

# Combiner while et if

Interrompt la boucle quand une condition devient vraie:


    !python
    i = 0
    while True:
        i = i + 1
        if i > 3:
            print("i est plus grand que 3, on arrête")
            break
        print("i =" + str(i))
        print("i est plus petit que 3, on continue")


<pre>
i = 1
i est plus petit que 3, on continue
i = 2
i est plus petit que 3, on continue
i = 3
i est plus petit que 3, on continue
i est plus grand que 3, on arrête
</pre>
---

# Lire une entrée utilisateur

* `input()`  (encore des parenthèses ...)

    * interrompt le script
    * lit ce que l'utilisateur tape jusqu'à ce qu'il tape "entrée".
    * renvoie une string

---

# Le jeu

On fait deviner un nombre à l'utilisateur, en affichant 'trop grand', 'trop petit'
jusqu'à ce qu'il trouve la valeur exacte.

---

# Le code


    !python
    # À recopier dans devine-nombre.py
    secret = 42

    print("Devine le nombre auquel je pense")

    while True:
        response = input()
        response = int(response)

        if response == secret:
            print("Gagné")
            break
        else:
            if response > secret:
               print("Trop grand")
            if response < secret:
               print("Trop petit")

---

# Éviter de hard-coder le secret

Le secret a une valeur prédéfinie, et il faut changer le code source
pour changer le secret, pas terrible.


Solution: le choisir au hasard

---

# Un secret au hasard

Remplacez le première ligne pour avoir:

    !python
    # À recopier dans devine-nombre.py
    import random

    secret = random.randint(0, 100)

Le jeu devient tout de suite plus amusant :)

(Oui, c'est un peu magique pour le moment, mais on expliquera en
détail comment ça marche plus tard).


---

# Et voilà!


      $ python 02-devine-nombre.py
      Devine le nombre auquel je pense
      50
      Trop grand
      25
      Trop petit
      27
      Trop grand
      26
      Gagné

---

# Liens


* Les sources sont [sur GitHub](https://github.com/E2L/cours-python/tree/master/sources).
* La présentation est disponible en PDF sur [le site de l'e2l](https://cours.getall.fr/e2l/DownLoads/0q0udu7qgaicv3djgevjlfpck4/C1600_chapitre-01.pdf)
