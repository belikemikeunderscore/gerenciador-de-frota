from .veiculo import Veiculo

class CarroEletrico(Veiculo):
    def __init__(self, marca: str, preco: float, bateria_kwh: float, autonomia_km: int, ano: int = None, kms: int = 0):
        super().__init__(marca, preco, ano, kms)
        self.bateria_kwh = float(bateria_kwh)
        self.autonomia_km = int(autonomia_km)

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Bateria: {self.bateria_kwh} kWh, Autonomia: {self.autonomia_km} km"

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "bateria_kwh": f"{self.bateria_kwh}",
            "autonomia_km": f"{self.autonomia_km}"
        })
        return d