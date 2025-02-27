# https://medium.com/@nelson.miranda_40644/implementando-design-patterns-em-python-o-padr%C3%A3o-factory-0043611c3fc6

from factory import ClienteFactory

fabrica = ClienteFactory()

try:

    pf = fabrica.criar_cliente('pf', 'Cesar Steinmeier', '002014749009')
    pf.exibir_dados()

    pj = fabrica.criar_cliente('pj', 'Cesar LTDA', "56.099.234/0001-00")
    pj.exibir_dados()

    pjegue = fabrica.criar_cliente('pjegue', 'Cesar LTDA', "56.099.234/0001-00")
    pjegue.exibir_dados()
except Exception as e:
    print(e)