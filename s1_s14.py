import json



vulnerabilidades = {"falha": "Porta 3389 Aberta", "severidade": "Alta"}
with open("dados_vuln.json", "w") as arquivo_escrita:
    json.dump(vulnerabilidades, arquivo_escrita)
    print("Arquivo 'dados_vuln.json' criado e dados salvos!")


try:
    with open("dados_vuln.json", "r") as arquivo_leitura:
        dados_recuperados = json.load(arquivo_leitura)
    print("Dados recuperados com sucesos!")
    print(dados_recuperados)

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado")
