from tkinter import *
from utils import form_data

input_name, type_personnage = '', ''

def open_mac():
    global form_data, type_personnage
    root = Tk()
    root.geometry('500x500')
    root.title('Register RPG')
    
    label_name = Label(root, text="Entrez votre nom: ", font=('bold'))
    label_name.place(x=50, y=50)
    
    form_data['input_name'] = Entry(root, width=40)
    input_name.place(x=220, y=57)
    
    label_sexe = Label(root, text="Entrez votre sexe: ", font=('bold'))
    label_sexe.place(x=50, y=90)
    Radiobutton(root, text='Homme', value=1).place(x=50, y=120)
    Radiobutton(root, text='Femme', value=2).place(x=150, y=120)
    Radiobutton(root, text='Trans', value=3).place(x=250, y=120)
    
    label_name = Label(root, text="Entrez votre type: ", font=('bold'))
    label_name.place(x=50, y=140)
    listeOptions = ('Guerrier', 'Voleur', 'Mage')
    type_personnage = StringVar()
    type_personnage.set(listeOptions[0])
    OptionMenu(root, type_personnage, *listeOptions).place(x=50, y=170)
    
    label_ethnie = Label(root, text="Entrez votre ethnie: ", font=('bold'))
    label_ethnie.place(x=50, y=210)
    listeOptions = ('Congo', 'Mongolie', 'France', 'USA', 'Japon', 'Cote_Ivoire', 'Argentine', 'Haiti', 'Angleterre')
    ethnie = StringVar()
    ethnie.set(listeOptions[0])
    OptionMenu(root, ethnie, *listeOptions).place(x=50, y=240)
    
    Button(root, command=click_button, text='Envoyez', width=30).place(x=250, y= 280)
    root.mainloop()
    
def click_button():
    global form_data, type_personnage
    print(form_data['input_name'].get())
    print(type_personnage.get())
if __name__ == '__main__':
    open_mac()