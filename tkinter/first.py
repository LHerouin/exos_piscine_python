"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(cadre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack(side="right", fill=X)

var_texte = StringVar()
ligne_texte = Entry(cadre, textvariable=var_texte, width=30)
ligne_texte.pack()



bouton_quitter = Button(cadre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()


var_case = IntVar()
case = Checkbutton(cadre, text="Ne plus poser cette question", variable=var_case)
case.pack()


var_choix = StringVar()

choix_rouge = Radiobutton(cadre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(cadre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(cadre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

liste = Listbox(cadre)
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")

liste.pack()

#var_case.get()
#var_choix.get()
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()