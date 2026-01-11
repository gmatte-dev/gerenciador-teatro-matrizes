# 🎭 Sistema de Reservas de Teatro

Este projeto é um **programa em Python** que simula o sistema de reservas de um teatro, utilizando uma **matriz 10x12** para representar os assentos.

O objetivo do projeto é praticar **lógica de programação**, **uso de matrizes**, **funções**, **estruturas de repetição** e **manipulação de arquivos**.

---

## 🛠️ Tecnologias
![Python](https://img.shields.io/badge/Python-3-blue?style=flat-square&logo=python)

---

## 🪑 Estrutura do Teatro

- **Fileiras:** 10
- **Assentos por fileira:** 12
- **Total de assentos:** 120

### Representação dos Assentos
| Símbolo | Status |
|---------|--------|
| `0` | Lugar livre |
| `1` | Lugar ocupado |

---

## ✨ Funcionalidades

- ✅ Exibir a disposição atual dos assentos
- ✅ Reservar um lugar disponível
- ✅ Liberar um lugar ocupado
- ✅ Contar quantos assentos estão livres e ocupados
- ✅ Identificar a fileira com mais assentos ocupados
- ✅ Identificar a fileira com menos assentos ocupados
- ✅ Verificar se há dois assentos livres lado a lado em uma fileira
- ✅ Salvar o estado do teatro em um arquivo `.txt`
- ✅ Carregar o estado do teatro a partir de um arquivo

---

## ▶️ Como Executar

### Pré-requisitos
- Python 3 instalado

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/gmatte-dev/gerenciador-teatro-matrizes.git 
```
2. Acesse a pasta do projeto:
```bash
cd gerenciador-teatro-matrizes
```

3. Execute o arquivo principal:
```bash
python sistema_reserva_matrizes.py
