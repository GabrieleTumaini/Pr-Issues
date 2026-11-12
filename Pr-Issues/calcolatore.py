class Operazione:
    def __init__(self, nome: str, *valori) -> None:
        self.nome = nome
        self.valori = list(valori)

    def esegui(self):
        raise NotImplementedError("Le classi figlie devono implementare esegui()")

    def __str__(self) -> str:
        return f"{self.nome}: {self.valori}"


class Somma(Operazione):
    def __init__(self, *valori) -> None:
        super().__init__("somma", *valori)

    def esegui(self):
        return sum(self.valori)