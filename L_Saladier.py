from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

class Formulaire:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire")
        self.root.geometry("780x520+250+100")
        
        # Chargement de l'image de fond
        self.icon = ImageTk.PhotoImage(file='daiki.png')
        self.lbl = tk.Label(self.root, image=self.icon, bg='#ddd', compound="top")
        self.lbl.pack(pady=15)

        # Champs du formulaire
        inscription = Frame(self.root)
                # Création d'une couleur semi-transparente (blanc avec 50% d'opacité)
        bg_color = "#ffffff"  # Couleur blanche
        bg_color_alpha = bg_color   # Ajout de 80 pour 50% d'opacité (hexadécimal)
        
        inscription.configure(bg=bg_color_alpha)  # Définition de la couleur semi-transparente comme fond



        inscription.pack(fill=BOTH, expand=True)
        inscription.place(x=100, y=50, width=700, height=400)

        title = Label(inscription, text="Creation de compte", font=("Arial", 20, "bold"), bg="blue", fg="grey")
        title.pack(pady=20)

        # Nom
        lbl_nom = Label(inscription, text="Nom:")
        lbl_nom.pack()
        self.ent_nom = Entry(inscription)
        self.ent_nom.pack()

        # Prénom
        lbl_prenom = Label(inscription, text="Prenom:")
        lbl_prenom.pack()
        self.ent_prenom = Entry(inscription)
        self.ent_prenom.pack()

        # Email
        lbl_email = Label(inscription, text="Email:")
        lbl_email.pack()
        self.ent_email = Entry(inscription)
        self.ent_email.pack()

        # Mot de passe
        lbl_password = Label(inscription, text="Mot de passe:", font=("times new roman", 15), fg="black")
        lbl_password.pack()
        self.ent_password = Entry(inscription, show="*")
        self.ent_password.pack()

        # Bouton Soumettre
        btn_submit = Button(inscription, text="Soumettre", command=self.submit_form)
        btn_submit.pack(pady=20)

    def submit_form(self):
        # Fonction appelée lors du clic sur le bouton Soumettre
        nom = self.ent_nom.get()
        prenom = self.ent_prenom.get()
        email = self.ent_email.get()
        password = self.ent_password.get()

        # Here you can add code to validate and process the form data
        # For now, let's just print the data
        print("Nom:", nom)
        print("Prenom:", prenom)
        print("Email:", email)
        print("Mot de passe:", password)

root = Tk()
app = Formulaire(root)
root.mainloop()
