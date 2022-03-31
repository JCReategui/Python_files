class Trabajador:
    print ("\n==================")
    print ("DATOS DE ENTRADA ")
    print ("==================")
    nombre= (input("TRABAJADOR: "))
    cat= (input("CATEGORÍA [A-B-C]: ")).upper() #considere mayúscula
    hx= int(input("HORAS EXTRAS: "))
    tardanza= int(input("TARDANZAS (minutos): "))

class Boleta(Trabajador):
    SueldoBase = 0
    PHX = 0
    DT = 0
    SueldoNeto = 0

    def msueldo(self, cat):
        if cat == "A":
            self.SueldoBase = 3000
        if cat == "B":
            self.SueldoBase = 2500
        if cat == "C":
            self.SueldoBase = 2000

        return self.SueldoBase

    def mhoraex(self, hx, cat):
        if cat == "A":
            self.PHX = 3000/240 * hx * 4
        if cat == "B":
            self.PHX = 2500/240 * hx * 3
        if cat == "C":
            self.PHX = 2000/240 * hx * 2
        
        return self.PHX

    def mtar(self, tardanza):
        self.DT = self.SueldoBase / 240 * tardanza / 60

        return self.DT

    def msldneto(self):
        self.SueldoNeto = self.SueldoBase + self.PHX - self.DT

        return self.SueldoNeto

bo = Boleta()
tr = Trabajador()

#Impresión
print ("\n=================")
print ("BOLETA DE PAGO ")
print ("=================")
print ("NOMBRE............:", tr.nombre)
print ("CATEGORÍA.........:", tr.cat)
print ("SUELDO BÁSICO.....:", bo.msueldo(tr.cat))
print ("DESCUENTO TARDANZA: ""{:.2f}".format(bo.mtar(bo.tardanza)))
print ("PAGOS HORAS EXTRAS: " "{:.2f}".format(bo.mhoraex(bo.hx, bo.cat)))
print ("SUELDO NETO.......: ""{:.2f}".format (bo.msldneto()))



