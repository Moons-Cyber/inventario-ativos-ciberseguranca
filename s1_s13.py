from enum import Enum

class StatusAtivo(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"
    EM_MANUTENCAO = "Em Manutenção"


print(StatusAtivo.EM_MANUTENCAO.value)