class Fraction():
    def __init__(self,nom,denom):
        self.nom=nom
        self.denom=denom
    def __str__(self):
        return "{}/{}".format(self.nom,self.denom)

    def __add__(self,other):
        temp_nom=(self.nom * other.denom) + (self.denom * other.nom)
        print(temp_nom)
        temp_denom=self.denom * other.denom

        return "{}/{}".format(temp_nom,temp_denom)

    def __sub__(self,other):
        temp_nom=self.nom * other.denom - self.denom * other.nom
        temp_denom=self.denom * other.denom

        return "{}/{}".format(temp_nom,temp_denom)

    def __mul__(self,other):
        temp_nom=self.nom * other.nom
        temp_denom=self.denom * other.denom

        return "{}/{}".format(temp_nom,temp_denom)

    def __truediv__(self,other):
        temp_nom=self.nom * other.denom 
        temp_denom=self.denom * other.nom

        return "{}/{}".format(temp_nom,temp_denom)
