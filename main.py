class Plato:
   'Clase comun para todos los platos'
   platoContador = 0

   def __init__(self, nombre, precio):
      self.nombre = nombre
      self.precio = precio
      Plato.platoContador += 1
   
   def mostrarContador(self):
     print "Total de platos: %d" % Plato.platoContador

   def mostrarPlato(self):
      print "Nombre : ", self.nombre,  ", Precio: ", self.precio

"Aqui se crea el primer objeto de la clase plato"
plato1 = Plato("Carne asada", 90)
"Aqui se crea el segundo objeto de la clase plato"
plato2 = Plato("Tajada con queso", 30)
plato1.mostrarPlato()
plato2.mostrarPlato()
print "Total de platos %d" % Plato.platoContador