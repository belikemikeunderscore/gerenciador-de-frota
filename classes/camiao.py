from .veiculo import Veiculo

class Camiao(Veiculo):
    def __init__(self, marca: str, preco: float, carga_max_kg: int, ano: int = None, kms: int = 0):
        super().__init__(marca, preco, ano, kms)
        self.carga_max_kg = int(carga_max_kg)

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Carga máxima: {self.carga_max_kg} kg"

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({"carga_max_kg": f"{self.carga_max_kg}"})
        return d
