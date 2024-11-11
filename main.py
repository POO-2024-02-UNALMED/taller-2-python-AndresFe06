class Asiento:

  def __init__(self, color, precio,registro):
    self.color=color
    self.precio=precio
    self.registro=registro

  def cambiarColor(self,nuevo_color):
    lista_colores=["negro","blanco","amarillo","rojo","verde"]
    if nuevo_color in lista_colores:
      self.color=nuevo_color

class Motor:


  def __init__(self, numeroCilindros,tipo,registro):
    self.numeroCilindros=numeroCilindros
    self.tipo=tipo
    self.registro=registro

  def cambiarRegistro(self,nuevo_registro):
    self.registro=nuevo_registro

  def asignarTipo(self,nuevo_tipo):
    lista_tipos=["electrico","gasolina"]
    if nuevo_tipo in lista_tipos:
      self.tipo=nuevo_tipo

class Auto:
    cantidadCreados=0
    def  __init__(self,modelo,precio,asientos:list,marca,motor,registro):
      self.modelo=modelo
      self.precio=precio
      self.asientos=asientos
      self.marca=marca
      self.motor=motor
      self.registro=registro

    def cantidadAsientos(self):
      return sum(1 for e in self.asientos if isinstance(e,Asiento))

    def verificarIntegridad(self):
      for e in self.asientos:
        if isinstance(e,Asiento):
          if e.registro!=self.motor.registro or e.registro!=self.registro or self.registro!=self.motor.registro:
            return "Las piezas no son originales"
      return "Auto original"
