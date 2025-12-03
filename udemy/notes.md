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
        - logical operation (and / or / not) -> Pour and: les 2 doivent être True / Or: 1 des deuc doit être True
    - Real (floating -> decimal)
    - Complex numbers (2 + 3j) -> fractions 

String (immutable):
    - core
    - indexing
    - slicing 




