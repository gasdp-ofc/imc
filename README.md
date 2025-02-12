# 🏋️ Cálculo de IMC (Índice de Massa Corporal) 

## 📌 Sobre o Projeto
Este é um projeto simples em Python para calcular o **Índice de Massa Corporal (IMC)** de um usuário com base no peso e altura informados. O objetivo é classificar a saúde corporal da pessoa conforme as diretrizes da **Organização Mundial da Saúde (OMS)**.

## 📊 Como Funciona?
O programa solicita ao usuário os seguintes dados:
- 📏 **Altura (m)**
- ⚖️ **Peso (kg)**

Após a entrada dos dados, o programa calcula o IMC utilizando a fórmula:

```
IMC = Peso (kg) / (Altura (m) * Altura (m))
```

Em seguida, exibe uma das seguintes classificações:

| IMC (kg/m²)       | Classificação          |
|-------------------|----------------------|
| Menor que 18,5   | Baixo Peso           |
| 18,5 - 24,9      | Peso Adequado        |
| 25,0 - 29,9      | Sobrepeso            |
| 30,0 - 34,9      | Obesidade Grau I     |
| 35,0 - 39,9      | Obesidade Grau II    |
| Maior ou igual a 40,0 | Obesidade Grau III |

## 🚀 Como Executar o Projeto
### 1️⃣ Clone o Repositório
```sh
$ git clone https://github.com/gasdp-ofc/imc.git
$ cd imc
```

### 2️⃣ Execute o Programa
Certifique-se de ter o **Python 3** instalado em sua máquina:
```sh
$ python imc.py
```

## 🛠 Tecnologias Utilizadas
- 🐍 **Python 3**
- 💻 **VS Code** para desenvolvimento
- 🔧 **Git e GitHub** para versionamento

## 📂 Estrutura do Projeto
```
📂 imc
 ├── 📄 imc.py  # Código principal
 ├── 📄 README.md  # Documentação do projeto
 ├── 📄 .gitignore  # Arquivos a serem ignorados pelo Git
```

## 🤝 Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:
1. Faça um **fork** do repositório
2. Crie um **branch** para sua feature (`git checkout -b minha-feature`)
3. Faça **commit** das suas alterações (`git commit -m 'Adicionando nova funcionalidade'`)
4. Faça um **push** para seu branch (`git push origin minha-feature`)
5. Abra um **Pull Request**

## 📜 Licença
Este projeto está sob a licença **MIT**. Sinta-se à vontade para usar e modificar!

---

💡 Desenvolvido por **[Guilherme Alves](https://github.com/seu-usuario)** 😊
