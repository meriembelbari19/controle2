
note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]


#moy = (sum(notes[3] for i in notes)/len(notes))
#i=0
#yaya = sum(notes[3] for i[2] in notes)
#print(yaya)

#ok = sum(note[2] for note in notes)
#print(ok)
#print(notes[0][2])

#pour l'élève 1 
notess = notes[0:5]
moy = (sum(note[2] for note in notess)/len(notess))
print(moy)


#pour les maths 
newliste = notes[0],notes[5],notes[6],notes[7]
print(newliste)
moymaths = (sum(note[2] for note in newliste)/len(newliste))
print(moymaths)


#fonction moyenne tuple

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)
 






