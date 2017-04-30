class Geladeira(object):
    def __init__(self, cervejas, temperatura, estado):
        self.cervejas = cervejas
        self.temperatura = temperatura
        self.estado = estado

    def consultar_cervejas(self):
        return self.cervejas

    def retirar_cerveja(self, cerveja):
        for i, c in enumerate(self.cervejas):
            if c == cerveja:
                return self.cervejas.pop(i)
        else:
            return None


if __name__ == '__main__':
    g = Geladeira(['Saint', 'Coruja', 'Dama', 'Boemia'], 0.0, True)
    g.retirar_cerveja('Coruja')