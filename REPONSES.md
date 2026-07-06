## Quelle est la différence entre une classe et un objet ? Donnez un exemple tiré de votre diagramme de classes.
Une classe est un ensemble d'elements ayant des etats et comportements similaire tandis qu'un objet n'est qu'une instance d'une classe. Exple: Class :Book Objet: La belle histoire de Leu le Lievre

## Qu'est-ce que l'encapsulation ? Où l'appliqueriez-vous concrètement dans la classe Loan ?
L'encapsulation est un concept de la POO ayant pour objectif de regrouper un ensemble d'attributs ou methodes afin de gerer les acces.
Dans la classe Loan je l'appliquerait en mettantles attributs private(-) et cetaines methodes publiques (+)

## Expliquez la différence entre association, agrégation et composition, avec un exemple tiré de votre diagramme de classes.
Une association est une interaction entre deux classes tandisqu'une agregation est une relation entre agregat->agrege (ensemble- element) stricte alors qu'une composition est une agregation non stricte entre composant et compose(partie)
Exples : association : Membre--Effectuer--Emprunt
composition: Catalogue--contient--Livre
agregation: Livre--possede--exemplaires

## Qu'est-ce que l'héritage ? Y a-t-il un cas d'héritage pertinent dans ce système (par exemple une classe Person dont hériteraient Member et Librarian) ? Justifiez votre choix.
L'heritage est une association de specialisation au cours de laquelle une classe dite fille acquiert les attribut et methodes publiques ou protegees d'une classe mere
Pour le moment la creation d'une classe personne n'est pas necessaire car le systeme est petit. La creation de cette classe ne serait ideale que dans un plus grand systeme

## Qu'est-ce que le polymorphisme ? Donnez un exemple concret, même en dehors du système bibliothèque si nécessaire. 
Le Polymorphisme est le conept de POO caracterisant une methode se comportant differemment en fonction de la classe dans laquelle ell est utilisee
Exemple:Chien: Parler()-> Le chien aboie
        Lion: Parler()->  Le lion rugit

## Quelle est la différence entre un diagramme de cas d'utilisation et un diagramme de séquence ? Que montre l'un que l'autre ne montre pas ?
Le diagramme de cas d'utilisation s'occupe des acteurs et de leurs interaction dans le systeme tandis que le diagramme de sequence s'occupe de comment se passe une interaction avec le systeme
Le DCU repond a qui fait quoi ?
Le DSE repond a comment ?

## Dans votre diagramme de cas d'utilisation, expliquez la différence entre une relation include et une relation extend, avec un exemple concret pris dans votre diagramme.
Une relation << include >> signifie que le cas appelant sera toujours execute avec le cas appele tandis au'une relation << extend >> le cas appele peut ne pas s'executer avec le cas appelant et necessite souvent une condition
exple: Reserver Livre << extend >> Envoyer une notification
        Emprunter un exemplaire << include >> valider emprunts

## Pourquoi utilise-t-on un diagramme d'état-transition ? Quel problème résout-il par rapport à une simple description textuelle des états possibles ?
On l'utilise montrer ou expliquer le changement d'etat d'un objet avec l'element declencheur
Il sera plus simple a comprendre car plus intuitif que de lire un texte verbeux

## Qu'est-ce que la multiplicité dans un diagramme de classes ? Donnez la multiplicité entre Member et Loan dans votre diagramme et expliquez-la en français.
La multiplicite dans un diagramme de classes represente les cardinalite des differentes classes dans une relation
Exple:Member1   * Loan Un membre peut effectuer plusieurs prets

##  En quoi l'approche orientée objet, telle que modélisée ici avec UML, diffère-t-elle d'une approche procédurale pour représenter ce même système ?
Elle differe dans le sens ou elle est plus modulable donc pas besoin de remodeliser en entierete le projet pour ajouter des elements ou fonctionnalite

## Quelle est la différence fondamentale entre le paradigme impératif et le paradigme déclaratif ?
Le paradigme decrit le fonctionnement d'uen operation ou d'un domain tandisque que celui declaratif decrit ou definit ce qu l'on veut sans s'occuper des fonctionnement

## Dans votre version fonctionnelle, qu'est-ce qu'une « fonction pure » ? Pourquoi cherche-t-on à éviter les effets de bord ?
Une fonction pure est une fonction qui ne modifie pas l'etat des variables en dehors de sa portee ou le systeme et deplus elle retourne toutjours le meme resultat pour des meme arguments
On cherche a eviter des effets de bords car :le programme devient moins previsible et donc moins controllable et maintenable

## Quels avantages apporte l'approche orientée objet par rapport à l'approche procédurale pour ce problème, quand le programme grossit (plus de fonctionnalités, plus de types de réduction, etc.) ?
La POO apporte l'avantage d'etre plus modulable et flexible ainsi plusieurs entites peuvent fonctionner sans toute fois modifier les autres et en plus le projet devient plus scalble et facile a cprendre en main

##  Citez un langage principalement associé à chacun des paradigmes suivants : impératif, orienté objet, fonctionnel, déclaratif.
POO : Java
imperatif: C
fonctionnel: Haskell 
declaratif : SQL

## Le langage que vous avez choisi (JavaScript ou Python) est-il rattaché à un seul paradigme ? Justifiez votre réponse à l'aide des versions que vous venez d'écrire.
Le python n'est pas rattache a un seul paradigme de programmation car il associe divers meniere de coder

## Dans quel contexte réel préféreriez-vous une approche fonctionnelle plutôt qu'orientée objet ? Donnez un exemple concret.
L'approche fonctionnelle produit des programmes plus stables car immunise contre les conflits entre les donnees 
Exemple plus grand interet dan le Big Data

## Quel est le lien entre le paradigme orienté objet que vous venez de pratiquer ici (Version 2) et les diagrammes UML réalisés en Partie 1 ?
Le lien est que les deux respecten les memes principes de l'OO et donc la definition des classes en POO est similaire qu'en UML

## Django, que vous allez utiliser dans la suite de la formation, repose principalement sur quel(s) paradigme(s) ? Justifiez avec un exemple concret (par exemple les models Django ou les QuerySets).
POO, exemple les modeles (le modele Utilisateur qui est une classe)