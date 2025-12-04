SECTION 1

- class = plusieurs fonctions regroupées ensembles (its a blueprint for creating objetcs)
- object = (en vrai vie: cup kettle, chai) nommé instance aussi and created by the class
- properties/attributes = (en vraie vie: cup, color, chai sweetness)
- functions (methods inside a class) = (en vraie vie, actions: stir, pour, drink)

* "def" creates a function
* when you write a class, there must be an init method in it (means that class has initialized)

virtual environment

    - one ecosystem in a big one
    - only affects the ecosystem
    - to install an environment (-m venv ".venv") * -m c'est pour l'installer dans cet environnement pas un autre 
    - to install modules in this env.
        - create a file (requirements.text)
        - modules == version
        - in terminal run install -r requirements

Organization
    - modules ( a signle python file : ends with .py)
    - packages ( __init__, has one or + modules in it)

=================================================================================================================================

SECTION 2

(objects and mutability)

* everything is object in python 

Object:

    - unique identity (tea has an unique blend), 
    - type (green tea, black tea...)
    - Value (can be empty too)

Mutable:
    - "changeable"
Immutable:
    - "NOT changeable"

* its the identity who helps identify if mutable or immutable

Theres a memory, with different things in it (numbers, lists...) differente references

    -When the id stays the same, but the thing or (object is changed), it's mutable:
    -Initial spice mix id: 4342388032
    -Initial spice mix id: set()
    -After spice mix id: {'Ginger', 'cardamom'}
    -After spice mix id: 4342388032"

En gros..
    - Numbers are immutable (reference can be changed but not the number itself)
    - Lists are mutable, the reference is always the same, the inside changes tho


Numbers:

    - Integers
    - Boolean
        - logical operation (and / or / not) -> Pour and: les 2 doivent être True / Or: 1 des deux doit être True
    - Real (floating -> decimal)
    - Complex numbers (2 + 3j) -> fractions 

String (immutable):

    - core
    - indexing
        - " A r o m a t i c  a n d  b o l d
        (first one is 0), last number is not inclusive 
    - slicing 
        - ( [start:end:start] )

Tuples:
     - ()
     - immutable

List:
    - list (array) 
    - []
    - mutable
    - list() = string into list of character

Operators overloading
    - list 1 + list 2 = new list with both of them (just like the function .extend()) (concatenate)
    - list * 3 = [ [list] [list] [list] ] 


Sets:
    - {}
    - mathematical
    - we have a and b, in the middle there is intersections (a little bit of a / b)
    - union = everything ( | )
    - intersection() ( & ) (common)
    - set1.difference(set2 = )

Dictionary:

    - indexing (0 , 1...)
    - each data has a name instead of a number as an index
    - key and value

* 
1. Liste

- Mutabilité : Modifiable (Mutable). Vous pouvez changer, ajouter ou supprimer des éléments après la création.
- Ordre/Indexation : Ordonnée. Les éléments sont accessibles par leur position (index) qui commence à 0.
- Syntaxe : [élément1, élément2, ...]
- Méthodes et Instructions Clés
    - append(element) : Ajoute un élément unique à la fin de la liste.
    - insert(index, element) : Ajoute un élément à une position (index) spécifique.
    - extend(iterable) : Ajoute tous les éléments d'une autre collection (liste, tuple, etc.) à la fin.
    - remove(value) : Supprime la première occurrence de la valeur spécifiée.
    - pop([index]) : Supprime l'élément à l'index donné et le retourne. (Par défaut, retire le dernier élément).
    - del list[index/slice] : Instruction pour supprimer par index ou par tranche d'éléments.
    - sort() : Trie la liste en place (modifie l'originale).
    - reverse() : Inverse l'ordre des éléments en place.
    - index(value) : Retourne l'index de la première occurrence de la valeur.
    - count(value) : Compte le nombre de fois qu'une valeur apparaît.

2. Tuples 

- Mutabilité : Non Modifiable (Immutable). Une fois créés, leur contenu ne peut pas être modifié.
- Ordre/Indexation : Ordonnée. Les éléments sont accessibles par leur position (index).
- Syntaxe : (élément1, élément2, ...)
- Méthodes Clés
    - Accès par index [ ] : Pour lire un élément à une position spécifique.
    - index(value) : Retourne l'index de la première occurrence de la valeur.
    - count(value) : Retourne le nombre d'occurrences de la valeur.
    - Note : Il n'y a aucune méthode pour ajouter ou supprimer des éléments car les tuples sont immuables.

3. Sets

- Mutabilité : Modifiable (Mutable) en termes d'ajout/suppression d'éléments.
- Ordre/Indexation : Non ordonnée. Les éléments n'ont pas d'index et sont tous uniques (les doublons sont ignorés).
- Syntaxe : {élément1, élément2, ...}
- Méthodes Clés

    - add(element) : Ajoute un élément unique à l'ensemble.
    - update(iterable) : Ajoute les éléments de n'importe quelle collection à l'ensemble.
    - remove(element) : Supprime l'élément (lève une erreur si l'élément n'est pas trouvé).
    - discard(element) : Supprime l'élément (ne lève pas d'erreur si l'élément n'est pas trouvé).
    - pop() : Supprime et retourne un élément aléatoire.
    - union(other) ou | : Combine les éléments des deux ensembles.
    - intersection(other) ou & : Trouve les éléments communs aux deux ensembles.
    - difference(other) ou - : Retourne les éléments du premier ensemble qui ne sont pas dans le second.

4. dict

- Mutabilité : Modifiable (Mutable). Les paires Clé:Valeur peuvent être ajoutées, supprimées ou modifiées.
- Ordre/Indexation : Ordonnée (depuis Python 3.7+). Les éléments sont accédés par leur clé, qui doit être unique et immuable.
- Syntaxe : {'clé1': 'valeur1', 'clé2': 'valeur2', ...}
- Méthodes Clés

    - Accès/Ajout dict[key] = value : Ajoute une nouvelle paire ou met à jour la valeur d'une clé existante.
    - get(key, [default]) : Accède à la valeur. Retourne None ou la valeur par défaut si la clé est absente (prévient les erreurs).
    - pop(key) : Supprime la paire Clé:Valeur associée à la clé et retourne la valeur.
    - popitem() : Supprime et retourne la dernière paire insérée.
    - del dict[key] : Instruction pour supprimer par clé.
    - keys() : Retourne une vue de toutes les clés.
    - values() : Retourne une vue de toutes les valeurs.
    - items() : Retourne une vue des paires (clé, valeur).
    - update()


Advanced data types:
    - datetime
    - time
    - calendar
    - timedelta
    - arrow (import)
    - dateutil (import)
    - collections

    
SECTION 3

* exercices 06.py (mini projects)

Conditionnals:
 - if
 - elif 
 - else
 - case match _



