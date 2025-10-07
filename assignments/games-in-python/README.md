

# 🎮 Jogo da Forca em Python

## 🎯 Objetivo
Construa o clássico jogo da forca utilizando strings, laços e entrada de dados em Python. O estudante irá praticar manipulação de strings, controle de fluxo e lógica condicional.

## 📝 Tarefas

### 1. Implementar o Jogo da Forca
**Descrição:**
Desenvolva um programa que sorteia uma palavra secreta de uma lista e permite ao jogador tentar adivinhar, letra por letra, antes de esgotar o número de tentativas.

**Requisitos:**
- Sortear uma palavra aleatória de uma lista pré-definida
- Aceitar palpites de letras do usuário
- Exibir o progresso atual da palavra (ex: `_ _ a _ a _`)
- Mostrar as letras já tentadas
- Controlar e exibir o número de tentativas restantes
- Encerrar o jogo quando a palavra for descoberta ou as tentativas acabarem
- Exibir mensagens de vitória ou derrota

**Exemplo de execução:**
```
Palavra: _ _ _ _ _
Tentativas restantes: 6
Letras já tentadas: 
Digite uma letra: a

Palavra: _ a _ a _
Tentativas restantes: 6
Letras já tentadas: a
Digite uma letra: e

Palavra: _ a _ a _
Tentativas restantes: 5
Letras já tentadas: a, e
Digite uma letra: m

Palavra: m a _ a _
Tentativas restantes: 5
Letras já tentadas: a, e, m
... (continua até vencer ou perder)
```
