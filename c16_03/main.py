

import statistics

note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(notes)

notes_elv = [note for note in notes if note[0] == "eleve1"]
print(notes_elv)
notes_elv_matiere = [note for note in notes_elv if note[1] == "math"]
print(notes_elv_matiere)
note_eleve = [i[2] for i in notes_elv ]
note_eleve_matiere= [i[2] for i in notes_elv_matiere ]
print(note_eleve_matiere)
print(statistics.mean(note_eleve_matiere))


def moyenne_tuple(notes, eleve=None, matiere=None):
    
    notes_elv = [note for note in notes if note[0] == eleve] if eleve is not None else notes
    notes_elv_matiere = [n for n in notes_elv if n[1] == matiere] if matiere is not None else notes_elv
    return sum([n[2] for n in notes_elv_matiere])/len(notes_elv_matiere)


class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)

  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')" 


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)


onote1 = [Note(eleve, matiere, valeur) for eleve, matiere, valeur in notes]
for onote in onote1:
  onote.afficher()

for onote in onote1:
  print(onote)


