import json

try:
    with open("ativos_seguros.json", "r") as arquivo:
        ativos = json.load(arquivo)

except FileNotFoundError:
    ativos = {}

try:
    id_ativo = int(input("Digite o ID numérico do ativo: "))
except ValueError:
    print("Erro: O ID precisa ser apenas números!")
else:
    nome_ativo = input("Digite o nome do ativo: ")
    ativos[id_ativo] = nome_ativo
    try:
        with open("ativos_seguros.json", "w") as arquivo:
            json.dump(ativos, arquivo)
    except Exception as e:
        print(f"Falha ao salvar: {e}")
    finally:
        print("Fim da operação de segurança. ")


