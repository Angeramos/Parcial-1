class parqueadero:
    def __init__(self, horarios:float, plazas:int,): 
        self.horarios = horarios 
        self.plazas = plazas
        pass

    def precios (self, tipo_coche:str, horas: int, precio: int): 
        self.horas = horas 
        self.tipo_coche = tipo_coche
        self.precio=precio
        precios = horas * tipo_coche

    def disponibilidad (self, tipo_coche= str, plazas = int):
        disponibilidad = disponibilidad - coche_nuevo

class coche_nuevo: 
    def __init_ (self, tipo_coche: str  ): 
        self.tipo_coche = tipo_coche
        pass 
