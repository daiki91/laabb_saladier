from tkinter import *
from tkinter import ttk, messagebox

class formulaire:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire")
        self.root.geometry("1920x1080+0+0")

        # Champs du formulaire
        inscription = Frame(self.root, bg="grey")
        inscription.pack(fill=BOTH, expand=True)

        title = Label(inscription, text="Creation de compte", font=("Arial", 20, "bold"), fg="orange")
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
        lbl_password = Label(inscription, text="Mot de passe:")
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
        


root = Tk()
app = formulaire(root)
root.mainloop()
