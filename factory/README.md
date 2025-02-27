# Modelos de Design Patterns Factory 🚀

No exemplo o código contido no arquivo main.py tenta instanciar três objetos utilizando a classe ClienteFactory.
- ao criar o objeto passando o tipo pj a classe ClienteFactory, que contém a lógica de criação, devolve um objeto da classe ClientePF
- ao criar o objeto passando o tipo pf a classe ClienteFactory devolve um objeto da classe ClientePJ
- passando qualquer outro tipo que não seja pf ou pj é devolvida uma exceção.

Desta forma é possível adicionar mais tipos de cliente, como MEI, implementar sua classe com atributos e adicionar na lógica da factory. Assim o código contido em main.py não precisa se adaptar para criar um novo objeto (como MEI), seguirá implementando novo objeto sempre da classe factory.