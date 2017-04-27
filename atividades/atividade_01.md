# Atividade 01 da disciplina de Engenharia de Software e Sistemas Multiagentes Aplicados a Redes Elétricas

Como atividade 01 de nossa disciplina foram designadas as tarefas:

## Introdução a UML 

Realizar a leitura do texto:

[Analise e projeto UML](https://www.dropbox.com/s/oqib8wvrpxgvj0n/ANALISE%20E%20PROJETO%20%26%20UML%202.0.pdf?dl=0): Esse texto dá uma visão geral a respeito da modelagem de software utilizando a linguagem gráfica UML, muitos dos conceitos gerais e básicos para se compreender a linguagem são encontrados neste texto.

## Introdução a Orientação a Objetos

Uma boa alternativa de aprendizagem dos conceitos relacionados a orientação a objetos é o aprendizado da linguagem Python, que além de ser bem simples e objetiva será essencial para o desenvolvimento dos conceitos apresentados nas próximas aulas, em que será utilizado o PADE, framework para desenvolvimento de sistemas multiagentes em Python.

Os textos sugeridos para leitura são:

[Tutorial de Python](https://www.dropbox.com/s/a0jg9v3f0qujtcj/DocumentacaoPython.pdf?dl=0)

[Tutorial de computação científica com Python](https://www.dropbox.com/s/4yzjyv1d3a5fjle/PythonScientific-simple.pdf?dl=0)

[Notebook de Python](https://www.dropbox.com/s/sxn6s7adspszho6/Intro%20Python.ipynb?dl=0)

Algumas ferramentas muito importantes para se trabalhar com Python são:

- [Anaconda](https://www.continuum.io/downloads): Pacote para realizar computação numérica com Python, além de ser uma distribuição Python, oferce uma série de bibliotecas comumente utilizadas em análises numéricas com Python, de fácil instalação nos ambientes Linux, OSX e Windows;
- [Projeto Jupyter](http://jupyter.org/): Oferece um ambiente de desenvolvimento para Python, voltado à análise numérica. Oferece os componentes super populares Jupyter-notebook e Jupyter-console.
- [PyCharm](https://www.jetbrains.com/pycharm/): É uma IDE com super recursos para desenvolvimento de aplicações Python para qualquer tipo de situação. Conta com um ótimo ambiente para executar debugs.
- [Sublime Text](https://www.sublimetext.com/3) e [Atom](https://atom.io/): São editores de texto voltados para programação com diversas linguagens. São leves e oferecem pluguins que os tornam verdadeiras IDEs de desenvolvimento.

## Atividade

1. Realize a modelagem UML do seguinte sistema:

Um sistema de chamadas aos consultórios de uma clínica médica. O sistema deve conter:

- Um módulo que libera uma senha para os pacientes que chagam e devem ficar na fila de espera;
- Um módulo para as atendentes realizarem as chamadas das senhas;
- Um módulo que gerencia a fila de espera e libera a chamada das senhas com a possibilidade de senhas com prioridade;
- Um módulo que permite ao médico consultar e fazer a chamada de seus pacientes.

> Faça a modelagem do sistema de acordo com o grau de abstração que achar mais conveniente, e não se prenda a detalhes que poderiam ser importantes em um sistema real, o objetivo não é implementar um sistema real, mas colocar em prática tanto os conceitos de modeagem UML, quanto os conceitos de desenvolvimento orientado a objetos em Python.

Alguns dos componentes que podem estar presentes em sua modelagem são:

- Paciente;
- Atendente;
- Médico;
- Fila de Espera;
- Painel de Chamadas;
- Gerador de Senhas;
- Entre outros.

**Dica**: Use o software [Astah](http://astah.net/download) para desenhar os diagramas UML, é um ótimo software para esta tarefa.

Boa sorte!

