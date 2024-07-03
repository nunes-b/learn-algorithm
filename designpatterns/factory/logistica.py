from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass


class Caminhao(Transporte):
    def entregar(self):
        return "Entrega feita por caminhão."


class Navio(Transporte):
    def entregar(self):
        return "Entrega feita por navio."


class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self):
        transporte = self.criar_transporte()
        return transporte.entregar()


class LogisticaTerrestre(Logistica):
    def criar_transporte(self) -> Transporte:
        return Caminhao()


class LogisticaMaritima(Logistica):
    def criar_transporte(self) -> Transporte:
        return Navio()


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.logisticas = []

    def registrar_logistica(self, logistica: Logistica):
        self.logisticas.append(logistica)

    def planejar_entregas(self, cliente: "Cliente"):
        for logistica in self.logisticas:
            resultado = logistica.planejar_entrega()
            print(
                f"Entregue por {logistica.__class__.__name__} para o cliente {cliente.nome}. Resultado: {resultado}"
            )
            cliente.foi_entregue = True
            cliente.logistica = logistica.__class__.__name__


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.foi_entregue = False
        self.logistica = None


# Criando uma empresa
empresa = Empresa("Amazon do Rômulo")

# Adicionando diferentes tipos de logística à empresa
logistica_terrestre = LogisticaTerrestre()
logistica_maritima = LogisticaMaritima()
empresa.registrar_logistica(logistica_terrestre)
empresa.registrar_logistica(logistica_maritima)

# Criando clientes
cliente_a = Cliente("Lojas Americanas")
cliente_b = Cliente("Casa e video")

# Planejando entregas para os clientes
empresa.planejar_entregas(cliente_a)
empresa.planejar_entregas(cliente_b)
