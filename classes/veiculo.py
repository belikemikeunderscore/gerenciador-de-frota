class Veiculo:
    def __init__(self, marca: str, preco: float, ano: int = None, kms: int = 0):
        self.marca = marca
        self.preco = float(preco)
        self.ano = ano
        self.kms = int(kms)

    def __str__(self) -> str:
        ano_str = f", {self.ano}" if self.ano else ""
        return f"{self.__class__.__name__}: {self.marca}{ano_str} - {self.preco:.2f}€ - {self.kms} km"

    def to_dict(self) -> dict:
        return {
            "tipo": self.__class__.__name__,
            "marca": self.marca,
            "preco": f"{self.preco:.2f}",
            "ano": self.ano if self.ano is not None else "",
            "kms": self.kms
        }
