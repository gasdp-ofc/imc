# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return imc, "Baixo peso"
    elif 18.5 <= imc < 24.9:
        return imc, "Peso adequado"
    elif 25.0 <= imc < 29.9:
        return imc, "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        return imc, "Obesidade grau I"
    elif 35.0 <= imc < 39.9:
        return imc, "Obesidade grau II"
    else:
        return imc, "Obesidade grau III"

# Entrada do usuário
if __name__ == "__main__":
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        imc, classificacao = calcular_imc(peso, altura)
        print(f"Seu IMC é {imc:.2f} - Classificação: {classificacao}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")