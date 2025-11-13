from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float 

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Film(**data)
