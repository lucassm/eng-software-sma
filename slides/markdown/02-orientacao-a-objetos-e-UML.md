# Engenharia de Software e Sistemas Multiagentes

## Orientação a Objetos e UML

- Linguagem de programação Python
    - vantagens
    - ferramentas
    - conceitos básicos
- Orientação a objetos
    - conceitos básicos
    - exemplo de OO em Python
- UML
    - diagrama de classes
    - diagrama de caso de uso
    - diagrama de sequencia
    - diagrama de atividades

## Introdução a linguagem de programação Python

Algumas vantagens de Python:

- Permite **focar no problema** sem perder tempo na sintaxe;
- Alta **produtividade**;
- **Baterias inclusas**;
- **Comunidade** livre, forte, diversificada, e acolhedora;
- Linguagem de verdade: orientada a objetos, funcional e estruturada;
- Linguagem de uso geral e também de nichos;
- Simples de iniciar sem esgotar.

## Começando com Python

- instalar o interpretador Python (**Anaconda** é uma ótima solução para Windows);
- Utilizar as ferramentas **JupyterConsole**, **JupyterNotebook**;
- IDE: **Pycharm**;
- Editores para desenvolvimento: **Sublime Text** e **Atom**.

## Primeiros passos

- Notebook: Introdução a Python

## Python para computação científica

- Numpy
- Scipy
- Matplotlib
- Simpy
- Pandas

## Orientação a Objetos

> Definição: A orientação a objetos é um modelo de análise, projeto e programação de sistemas de software baseado na composição e interação entre diversas unidades de software chamadas de objetos.

- Na qualidade de método de modelagem, é tida como a melhor estratégia para se eliminar o "gap semântico", dificuldade recorrente no processo de modelar o mundo real do domínio do problema em um conjunto de componentes de software que seja o mais fiel na sua representação deste domínio.

- Na programação orientada a objetos, implementa-se um conjunto de classes que definem os objetos presentes no sistema de software.

- Cada classe determina o comportamento (definido nos métodos) e estados possíveis (atributos) de seus objetos, assim como o relacionamento com outros objetos.

## Conceitos importantes em orientação a objetos

- Classe: Modelo para criar objetos, abstração que representa uma entidade do mundo real;
- Objeto: É a instância de uma classe;
- Atributo: Parâmetro de uma classe;
- Método: Executa uma ação dentro de uma classe;
- Herança: Relação entre classes onde é possível utilizar a expressão 'é um';
- Associação: Relação entre classes onde é possível utiizar a expressão 'tem um';
- Encapsulamento: Serve para controlar o acesso aos atributos e métodos de uma classe.

## Exemplo Simples

```python
class Geldeira(object):
    def __init__(self, cervejas, temperatura, estado):
        self.cervejas = cerveja
        self.temperatura = temperatura
        self.estado = estado

    def consultar_cervejas(self):
        return self.cervejas

    def retirar_cerveja(self, cerveja):
        for i, c in enumerate(self.cervejas):
            if c == cerveja
            return self.cervejas.pop(i)
        else:
            return None
```

## Exercício

Crie uma classe calculadora, que implemente os métodos soma, subtração, divisão e multiplicação recebendo como parâmetros em cada método duas variáveis (x e y) e devolva o resultado da operação, exemplo:

```
>> calc.soma(12, 10)
22
``` 

## UML

A UML, Linguagem Unificada de projetos orientados a objetos é uma linguagem padrão de notação de projetos.

- serve como liguagem para expressar decisões de projeto que não são óbvias ou que não podem ser deduzidas do código;
-  provê semântica que permite capturar decisões estratégicas e táticas;
- provê uma forma concreta para a compreensão das pessoas e para ser manipulada pelas máquinas.
- É independente das linguagens de programação.

## Diagrama de Classes

![Diagrama de Classes](https://cdn.rawgit.com/lucassm/eng-software-sma/c3e1a492/slides/markdown/Figuras/c1.svg)

## Diagrama de Classes

![Diagrama de Classes](https://cdn.rawgit.com/lucassm/eng-software-sma/eb191acd/slides/markdown/Figuras/c2.svg)

## Diagrama de Atividades

![Diagrama de Classes](https://cdn.rawgit.com/lucassm/eng-software-sma/eb191acd/slides/markdown/Figuras/c3.svg)

## Diagrama de Caso de Uso

![Diagrama de Classes](https://cdn.rawgit.com/lucassm/eng-software-sma/eb191acd/slides/markdown/Figuras/c4.svg)
