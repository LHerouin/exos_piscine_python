from tkinter import *

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=1000, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        
        # Création de nos widgets

        #Widget Label
        self.message = Label(self, text="Source :")
        self.message.pack()

        #Widget Entry
        var_texte = StringVar()
        self.ligne_texte = Entry(self, textvariable=var_texte, width=20)
        self.ligne_texte.pack()

        var_texte.set("\\B\\T80CM\\T60CM\\N")
        

        #Widget Button
        self.bouton_clean = Button(self, text="CLEAN",bg="green", command=self.quit)
        self.bouton_clean.pack()



        #Widget Label
        self.message = Label(self, text="Destination")
        self.message.pack()


        #Widget Entry
        var_texte2 = StringVar()
        self.ligne_texte2 = Entry(self, textvariable=var_texte2, width=10)
        self.ligne_texte2.pack(side="right",padx=20)

        var_texte2.set("80CM")


        #Widget Entry
        var_texte3 = StringVar()
        self.ligne_texte3 = Entry(self, textvariable=var_texte3, width=10)
        self.ligne_texte3.pack(side="right")

        var_texte3.set("60CM")


#Initialisation de la fenêtre
fenetre = Tk()

#Définition de la taille de la fenêtre
fenetre.geometry("200x150")

#Initialisation de l'objet interface
interface = Interface(fenetre)


#Lancement de la fenêtre via l'objet
interface.mainloop()

#Quand la boucle est terminée, desctruction de l'objet
interface.destroy()