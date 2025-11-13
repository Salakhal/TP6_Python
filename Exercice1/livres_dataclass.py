from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)
    
    def promo(self, prix_reduit: float):
        """Retourne un nouveau Livre avec le prix réduit"""
        return replace(self, prix=prix_reduit)
    
    @staticmethod
    def from_json(json_str: str):
        """Crée un Livre à partir d'une chaîne JSON"""
        data = json.loads(json_str)
        return Livre(**data)


livre1 = Livre("1984", "George Orwell", 1949, 9.90)
livre2 = livre1.promo(7.90)
livre3 = Livre.from_json('{"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee": 1943, "prix": 12.5}')

livres = [livre1, livre2, livre3]
livres_tries = sorted(livres, key=lambda l: l.prix)

for l in livres_tries:
    print(l.to_json())
