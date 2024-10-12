"""
Singleton je kreativní návrhový vzor, který umožňuje zajistit, aby třída měla pouze jednu instanci, a zároveň poskytuje globální přístupový bod k této instanci.
"""

"""
Důvody
- Optimalizace výkonu: 
    V některých případech může být vytvoření nové instance objektu nákladné. Singleton může zlepšit výkon tím, že se vyhne opakovanému vytváření stejných objektů.
- Řízení přístupu:
    Singleton umožňuje centralizované řízení přístupu k určitým zdrojům nebo funkcím.
- Jediný zdroj pravdy:
    Spojení s databází, které by mělo být otevřeno pouze jednou.
    Logovací objekt, který zaznamenává všechny události v aplikaci.
"""

class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance 


object1 = Singleton()
object2 = Singleton()

print(object1 is object2)




