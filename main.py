#question 1 

def puiss (chiffre, liste):
  return [i** chiffre for i in liste]

print(puiss(2,[3,5]))


#question 2

def puiss_etoile (chiffre, *liste):
  return [i** chiffre for i in liste]

print(puiss_etoile(2,3,5))

#question 3 

def mafonction(a, b , **options):
  print(a)
  print(b)
  print(options)


mafonction(1,2, z=8)

def somme2(z, y):
   return z + y

def somme3(x,y,z):
  return x + y + z


def somme3(*a):
  return sum(a)

somme3(1,2,3)



b = 1,2

*a,c = 0, *b
print(a)
print(b)
a = *a,*b
print(a)

print(somme3(*a))


#ca ne fonctionne pas avec somme2 car il y a 4 arguments alors que somme2 ne peut en supporter que 2. 



#0903

#question1

def somme(param1,param2):
  return param1+param2 

print(somme(2,4))


#question2 

def test(a, b, c):
  return a+b+c


print(test(2,3,4))
print(test(2,3,c= 4))
print(test(a=2, b=3, c=4))

#print(test(a=2)) #manque b et c ne fonctionne pas 

#print(test(a=2, b=3, 12)) #ne comprends pas le c 


#question3

def test(a, b, c):
  return a+b+c


valeurs = 2,4,5

valeurs1 = [2,4,5]
dico = {'a': 3, 'b': 2, 'c':3 }
print(test(*valeurs1))
print(test(*valeurs))
print(test(**dico))


#question3.1 


def puissance(a, b):
  return a ** b



valeurs = [[2,3], [3,3]]
print(valeurs)
def puissance(a, b):
  return a ** b

a,b= valeurs
print(a)
print(b)

print(a[0])

valeurs = [[2,3], [3,3]]

def puiss1(valeurs):
 for v in valeurs:
   a,b= v
   p= puissance(*v)
   print(p)
   print(v)
puiss1(valeurs)


#question4 

maliste = [1,2,3,5]
maliste.append(4)
print(maliste)


def append(liste,new):
 return liste.append(str(new))

print(maliste)

print(append(maliste,7))
print(maliste)


#question5


#il manque l'argument 
append() # est valide
append(2)
append(valeur=4)



#question6 

