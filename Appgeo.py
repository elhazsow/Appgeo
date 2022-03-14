# -*-coding:utf-8-*-
#####################################################################
# ##### El Hadji SOW ,DAKAR 2019  ###################################
# ####### AppGeo is a piece of software that converts coordinates ###
# ###################################################################
# ######################## import ###################################
from tkinter import *
from math import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

import re
import os
import simplekml

# #################################################

root = Tk()
root.title('AppGéo')
root.geometry('1000x500')
root.iconbitmap(r'images\appgéo.ico')
root.minsize(height=500, width=1000)
root.maxsize(height=500, width=1000)
couleurs = ['#3B83BD', '#E1CC4F', '#BEBD7F', '#ED760E', '#2271B3', '#025669', '#212121', '#9A2B75', '#BEBD7F',
            '#6A6454', '#3F3D24', '#73A05B', '#204606', '#24627B']
root.config(background=couleurs[6])

# images utilisées


photo = ImageTk.PhotoImage(Image.open(r"images\fond ecran.jpg"))
photo_frm = ImageTk.PhotoImage(Image.open(r"images\fond ecran1.jpg"))
photo_frm1 = ImageTk.PhotoImage(Image.open(r"images\fond ecran2.jpg"))
photo_1 = ImageTk.PhotoImage(Image.open(r"images\bton.png"))
navbar = ImageTk.PhotoImage(Image.open(r"images\navbar.png"))
na_image = ImageTk.PhotoImage(Image.open(r"images\fond ecran3.jpg"))
exit_ico = ImageTk.PhotoImage(Image.open(r"images\open-png.png"))

# list des frames


f3 = Frame(root, height=500, width=1000)

f1 = Frame(root, height=500, width=1000)

f4 = Frame(root, height=500, width=1000)

f_navbar = Frame(root, bg=couleurs[2], height=500, width=260)

f_navbar.place(x=-261, y=45)

f5 = Frame(f4, height=300, width=1000)

f6 = Frame(f4, height=300, width=1000)

frame7 = Frame(f4, height=300, width=1000)

frame8 = Frame(f4, height=300, width=1000)

f7 = Frame(f4, height=300, width=1000)

f8 = Frame(f4, height=300, width=1000)

frames = [f4]
frm = [f5, f6, frame7, frame8]
frame_1 = [f3, f1]

for i in frames:
    label = Label(i, image=photo)
    label.place(relheight=1, relwidth=1)
for i in frm:
    label = Label(i, image=photo_frm)
    label.place(relheight=1, relwidth=1)

label1 = Label(f1, fg=couleurs[8], image=photo, compound=CENTER,
               text='Conversion de coordonnées:\n\n\n\n\n\n\n\n\n\n\n\n\n\n', font='Times 20 italic')
label1.place(relwidth=1, relheight=1)

label3 = Label(f3, width=65, fg=couleurs[8], image=photo, compound=CENTER,

               text="Bienvenue sur notre application qui permet de Convertir des cordonnées \n et de calculer "
                    "l'altérations linéaires des projections Lambert\n et des projections UTM\n\n\n\n\n\n\n\n\n\n\n",
               font='TIMES 22 italic')

label3.place(relwidth=1, relheight=1)

f3.pack(expand=1, fill=BOTH)


# FONCTIONS


def file_name():
    global fichier
    try:
        fichier = filedialog.askopenfilename(initialdir=r"C:\Users\Downloads", title='ouvrir',
                                             filetypes=(("Fichier Texte", '*.txt'),))

    
        file = open(fichier, 'r')
        filename.set(file.name)
        fichier.close()
    except:
        pass


def ask_string():
    try:
        try:
            with open(fichier, 'r') as f:
                i = 0

                with open('Appgeo.txt', 'w') as ap:
                    for lines in f:
                        t1 = nav_sp1.get()
                        t2 = nav_sp2.get()
                        t3 = nav_sp3.get()
                        valu = re.split('[{}{}{}]+'.format(spteur[t1], spteur[t2], spteur[t3]), lines.strip())

                        if is_float(valu[1]) and is_float(valu[2]) and len(valu) <= 4:
                            valu[1] = float(valu[1])
                            valu[2] = float(valu[2])
                            if idx == 7:
                                valux = nav_ellipsoide_f7(valu[1], valu[2])
                                if not valux:

                                    ap.write('\n??????')

                                else:
                                    if len(valu) == 4:
                                        linx = '{}{}{}{}{}{}{}\n'.format(valu[0], spteur[t1], valux[0], spteur[t2],
                                                                         valux[1], spteur[t3], valu[3])

                                    else:
                                        linx = '{}{}{}{}{}\n'.format(valu[0], spteur[t1], valux[0], spteur[t2],
                                                                     valux[1])
                                    ap.write(linx)

                                    i += 1

                            elif idx == 8:
                                valux = nav_ellipsoide_f8(valu[1], valu[2])
                                if not valux:
                                    ap.write('\n??????')

                                else:
                                    if len(valu) == 4:
                                        linx = '{}{}{}{}{}{}{}\n'.format(valu[0], spteur[t1], valux[0], spteur[t2],
                                                                         valux[1], spteur[t3], valu[3])

                                    else:
                                        linx = '{}{}{}{}{}\n'.format(valu[0], spteur[t1], valux[0], spteur[t2],
                                                                     valux[1])
                                    ap.write(linx)

                                    i += 1
                            else:
                                messagebox.showerror(title='!',
                                                     message='AppGéo a rencotré un promblème dans le fichier!'
                                                             '\n Veillez revoir les séparateurs et/ou la disposition')

                        else:
                            try:
                                valu[1] = re.split('=', valu[1])
                                valu[2] = re.split('=', valu[2])
                            except IndexError:
                                pass
                            if len(valu[1]) > 1 and len(valu[2]) > 1:
                                if is_float(valu[1][1]) and is_float(valu[2][1]):
                                    if idx == 7:
                                        valux = nav_ellipsoide_f7(valu[1][1], valu[2][1])
                                        if not valux:

                                            ap.write('??????\n')


                                        else:
                                            if len(valu) == 4:
                                                linx = '{}{}{}={}{}{}={}{}{}\n'.format(valu[0], spteur[t1], valu[1][0],
                                                                                       valux[0], spteur[t2], valu[2][0],
                                                                                       valux[1], spteur[t3], valu[3])
                                            else:
                                                linx = '{}{}{}={}{}{}={}\n'.format(valu[0], spteur[t1], valu[1][0],
                                                                                   valux[0], spteur[t2], valu[2][0],
                                                                                   valux[1])

                                            ap.write(linx)

                                            i += 1

                                    elif idx == 8:
                                        valux = nav_ellipsoide_f8(valu[1][1], valu[2][1])
                                        if not valux:
                                            ap.write('??????\n')
                                        else:

                                            if len(valu) == 4:
                                                linx = '{}{}{}={}{}{}={}{}{}\n'.format(valu[0], spteur[t1], valu[1][0],
                                                                                       valux[0], spteur[t2], valu[2][0],
                                                                                       valux[1], spteur[t3], valu[3])
                                            else:
                                                linx = '{}{}{}={}{}{}={}\n'.format(valu[0], spteur[t1], valu[1][0],
                                                                                   valux[0], spteur[t2], valu[2][0],
                                                                                   valux[1])

                                            ap.write(linx)

                                            i += 1
                                    else:
                                        ap.write('\n??????')

                            else:
                                ap.write('??????\n')
                with open('Appgeo.txt', 'r') as ap:
                    with open(
                            filedialog.asksaveasfilename(initialdir=r"C:\Users", title='ouvrir',
                                                         defaultextension=".txt",
                                                         filetypes=(("Text Files", '*.txt'),)), 'w') as wf:
                        for line in ap:
                            wf.write(line)
                        showinfo('Info', 'Le fichier {} a été converti avec succès'.format(f.name))

        except IndexError:
            messagebox.showerror(title='!', message='Choisissez les bons séparateurs!')
    except (NameError, FileNotFoundError):
        messagebox.showerror(title='!', message='Erreur de fichier!')


def convertir_degre(val):
    if valeunite[spin_unites.get()] == 0:
        return val * 180 / pi
    elif valeunite[spin_unites.get()] == 1:
        return val
    elif valeunite[spin_unites.get()] == 2:
        return val * 180 / 200
    elif valeunite[spin_unites.get()] == 3:
        vat = re.split('[°\'"]+', val)
        val = abs(float(vat[0])) + float(vat[1]) / 60 + float(vat[2]) / 3600
        if float(vat[0]) < 0:
            return -val
        else:
            return val


def displayfilepoint():
    points_path = 'appgeofichier.kml'  # file name
    try:
        try:
            with open(fichier, 'r') as f:

                fiche_point = simplekml.Kml()

                for lines in f:
                    t1 = nav_sp1.get()
                    t2 = nav_sp2.get()
                    t3 = nav_sp3.get()
                    valu = re.split('[{}{}{}]+'.format(spteur[t1], spteur[t2], spteur[t3]), lines.strip())
                    if is_float(valu[1]) and is_float(valu[2]):
                        valu[1] = float(valu[1])
                        valu[2] = float(valu[2])
                        if idx == 7:
                            valux = nav_ellipsoide_f7(valu[1], valu[2])
                            if not valux:
                                messagebox.showerror(title='Erreur',
                                                     message='AppGéo a rencontré un problème de fichier!')


                            else:
                                fiche_point.newpoint(name=valu[0],
                                                     coords=[(convertir_degre(valux[0]), convertir_degre(valux[1]))])

                        elif idx == 8:
                            valux = nav_ellipsoide_f8(valu[1], valu[2])
                            if not valux:
                                messagebox.showerror(title='Erreur',
                                                     message='AppGéo a rencontré un probleme de fichier!')

                            else:
                                fiche_point.newpoint(name=valu[0],
                                                     coords=[(convertir_degre(valux[0]), convertir_degre(valux[1]))])

                    else:
                        valu[1] = re.split('=', valu[1])
                        valu[2] = re.split('=', valu[2])
                        if len(valu[1]) > 1 and len(valu[2]) > 1:
                            if is_float(valu[1][1]) and is_float(valu[2][1]):
                                if idx == 7:
                                    valux = nav_ellipsoide_f7(valu[1][1], valu[2][1])
                                    if not valux:
                                        pass
                                    else:
                                        fiche_point.newpoint(name=valu[0],
                                                             coords=[(convertir_degre(valux[0]),
                                                                      convertir_degre(valux[1]))])

                                elif idx == 8:
                                    valux = nav_ellipsoide_f8(valu[1][1], valu[2][1])
                                    if not valux:
                                        messagebox.showerror(title='Erreur',
                                                             message='AppGéo a rencontré un probleme de fichier!')
                                    else:

                                        fiche_point.newpoint(name=valu[0],
                                                             coords=[
                                                                 (
                                                                 convertir_degre(valux[0]), convertir_degre(valux[1]))])
                            else:

                                pass

        except FileNotFoundError:
            messagebox.showerror(title='!', message='Erreur de fichier')
            try:
                fiche_point.save(points_path)
                os.startfile(points_path)  # it opens the file in google earth
            except:
                messagebox.showerror(title='!', message='Appgeo n\'a pas trouvé GOOGLE EARTH')
    except:
        messagebox.showerror(title='!', message='Choisissez les bons séparateurs \n et la bonne disposition!')


matricul = 0
valx = StringVar()
valy = StringVar()
valz = StringVar()


def exporter():
    global valx
    global valy
    global valz
    global checkvar
    val1 = valx
    val2 = valy
    val3 = valz
    global matricul
    name = askstring('Matricule du point', 'Donnez le nom du point :')
    if name:
        try:
            with open(filedialog.asksaveasfilename(initialdir=r"C:\Users", title='Exporter', defaultextension=".txt",
                                                   filetypes=(("Text Files", '*.txt'),)), 'a') as wf:
                if checkvar.get() == 0:
                    wf.write('{}  {}  {}\n'.format(name, val1, val2))
                elif checkvar.get() == 1:
                    wf.write('{}  {}  {}  {}\n'.format(name, val1, val2, val3))
                showinfo('Info', 'Le point {} a été enregistré avec succès'.format(name))

        except:
            pass
    else:
        check = messagebox.askquestion(title='!',
                                       message='Votre point n\' a pas de nom. \nVolez-vous un nom par défaut')
        if check == 'yes':
            try:
                with open(
                        filedialog.asksaveasfilename(initialdir=r"C:\Users", title='Exporter', defaultextension=".txt",
                                                     filetypes=(("Text Files", '*.txt'),)), 'a') as wf:

                    if checkvar.get() == 0:
                        wf.write('{}  {}  {}\n'.format(name, val1, val2))
                    elif checkvar.get() == 1:
                        wf.write('{}  {}  {}  {}\n'.format(name, val1, val2, val3))
                    showinfo('Info', 'Le point {} a été enregistré avec succès'.format(matricul))

                    matricul += 1
            except FileNotFoundError:
                pass
        else:
            pass


idx = 0


def display(nam, lon, lat):
    try:
        fichier_point = simplekml.Kml()  # create a  kml file
        fichier_point.newpoint(name=nam, coords=[(lon, lat)])  # create new point in the file
        point_path = 'appgeodoc.kml'  # file name

        fichier_point.save(point_path)
        os.startfile(point_path)  # it opens the file in google earth
    except:
        messagebox.showerror(title='!', message='Appgeo n\'a pas trouvé GOOGLE EARTH')


def display_on_map():  # show the point
    global showx
    global showy
    global matricul
    name = askstring('Matricule du point', 'Donnez le nom du point :')
    if name:
        try:
            display(name, showx, showy)
        except:
            pass
    else:
        check = messagebox.askquestion(title='!',
                                       message='Votre point n\' a pas de nom. \nVolez-vous un nom par défaut')
        if check == 'yes':
            try:
                display(name, showx, showy)
            except:
                pass
            showinfo('Info', 'Le point va s\'afficher sous le nom \"appgeo{}'.format(matricul))
            matricul += 1
        else:
            pass


def swap(frame):  # pour naviguer entre les frames
    global idx
    id = 0
    labelambert.place_forget()
    spin_lambert.place_forget()
    bton7.place(anchor=NW, y=10)
    btonhelp.place(x=965, anchor=NW, y=12)
    labelutm.place_forget()
    spin_utm.place_forget()
    NOR.place_forget()
    SU.place_forget()
    if frame == f4:
        idx = 4
        en_1.set('')
        en_0.set('')
        f4.pack(expand=1, fill=BOTH)
        frame7.place_forget()
        frame8.place_forget()
        f5.place_forget()
        f6.place_forget()
        btnf2.place(x=150, y=300)
        btnf1.place(x=600, y=300)
        label4.config(text='Latitude :', width=10)
        label4.place(x=55, y=100)
        label6.config(text='Longitude :', width=10)
        label6.place(x=55, y=150)
        label8.config(text='Convertir des coordonnées géographiques')
        label8.config(height=30)
        alter.place(x=405, y=150)
    if frame == f5:
        navba.place_forget()
        f4.pack(expand=1, fill=BOTH)
        frame.place(x=0, y=210)
        btnf1.place_forget()
        btnf2.place_forget()
        frame.tkraise()
        idx = 5
        label8.config(height=30)
        alter.place(x=405, y=150)
    if frame == f6:
        navba.place_forget()
        f4.pack(expand=1, fill=BOTH)
        frame.place(x=0, y=210)
        btnf1.place_forget()
        btnf2.place_forget()
        f5.place_forget()
        frame.tkraise()
        idx = 6
        label8.config(height=30)
        alter.place(x=405, y=150)
    if frame == frame8:
        en_1.set(conv_result(-15 * pi / 180))
        en_0.set(conv_result(0))
        NOR.place(x=560, y=143)
        SU.place(x=560, y=159)
        labelutm.place(x=405, y=150)
        spin_utm.place(x=500, y=150)
        alter.place_forget()
        navba.place(x=40, y=10)
        f4.pack(expand=1, fill=BOTH)
        frame.place(x=0, y=210)
        btnf1.place_forget()
        label8.config(text='Convertir des coordonnées planes UTM\n en coordonnées géographiques', height=50)
        btnf2.place_forget()
        f5.place_forget()
        frame7.place_forget()
        label4.config(text='Φ_0 = ', width=5)
        label4.place(x=105, y=100)
        label6.place(x=105, y=150)
        label6.config(text='λ_0 = ', width=5)
        frame.tkraise()
        idx = 8
    if frame == frame7:
        labelambert.place(x=405, y=150)
        spin_lambert.place(x=510, y=150)
        en_1.set(conv_result((2 + 20 / 60 + 14.025 / 3600) * pi / 180))
        en_0.set(conv_result(55 * pi / 200))
        alter.place_forget()
        navba.place(x=40, y=10)
        idx = 7
        f4.pack(expand=1, fill=BOTH)
        frame.place(x=0, y=210)
        btnf1.place_forget()
        btnf2.place_forget()
        label8.config(text='Convertir des coordonnées Lambert planes\n en coordonnées géographiques', height=50)
        f5.place_forget()
        f6.place_forget()
        label4.config(text='Φ_0 = ', width=5)
        label6.config(text='λ_0 = ', width=5)
        label4.place(x=105, y=100)
        label6.place(x=105, y=150)
        frame8.place_forget()
        frame.tkraise()
    for j in frame_1:
        if j != frame:
            j.pack_forget()
        else:
            idx = frame_1.index(j)
            j.pack(expand=1, fill=BOTH)
            btonhelp.place_forget()


nav = True


def button_navbar():
    global nav
    if nav is True:
        for i in range(-34, 0):
            f_navbar.place(x=8 * i, y=45)
            f_navbar.update()
            nav = False
    else:
        for i in range(0, 34):
            f_navbar.place(x=-8 * i, y=45)
            f_navbar.update()
            nav = True


gx = 0
g_x = 0


def retour1():
    i = idx
    global gx
    global g_x
    global nav
    if i == 6:
        f6.place_forget()
        btnf2.place(x=150, y=300)
        btnf1.place(x=600, y=300)
        navba.place_forget()
        f_navbar.place_forget()
        nav = True
        gx += 1
    elif i == 5:
        f5.place_forget()
        btnf2.place(x=150, y=300)
        btnf1.place(x=600, y=300)
        navba.place_forget()
        f_navbar.place_forget()
        nav = True
        g_x += 1
    elif i == 4 or i == 7 or i == 8:
        navba.place_forget()
        f_navbar.place_forget()
        nav = True
        f4.pack_forget()
        swap(f1)
    elif i == 1:
        swap(f3)
        bton7.place_forget()

    else:
        pass


def check():
    global gx
    global g_x
    if gx == 2 or g_x == 2:
        f4.pack_forget()
        swap(f1)
        gx = 0
        g_x = 0
    else:
        pass


def retourn():
    retour1()
    check()


def quitter():
    réponse = messagebox.askquestion(title="Quitter", message="Voulez vous vraiment quitter AppGéo", icon='warning')
    if réponse == 'yes':
        root.quit()
    else:
        return


def donothing():
    pass


def parcourir_bouton(bton):
    def buton_hover(e):
        if bton == bton11:
            bton["bg"] = '#C51D34'
            bton['fg'] = 'white'
            bton['relief'] = 'groove'
        else:
            bton["bg"] = '#025669'
            bton['fg'] = 'white'
            bton['relief'] = 'groove'

    def buton_hover_leave(e):
        if bton == bton11:
            bton["bg"] = 'red'
            bton['fg'] = 'white'
            bton['relief'] = 'raised'
        else:
            bton["bg"] = couleurs[0]
            bton['fg'] = 'black'
            bton['relief'] = 'raised'

    bton.bind("<Enter>", buton_hover)
    bton.bind("<Leave>", buton_hover_leave)


def nav_ellipsoide_f7(E_f7, N_f7):
    global n_fi
    global esc_2
    global ld
    global a
    global phi
    global exc_1
    ent_a = entry_a.get()
    ent_b = entry_b.get()
    ent_0 = entry_0.get()
    ent_1 = entry_1.get()
    az = valeunite[spin_unites.get()]
    if is_float(ent_0) and is_float(ent_1) and az != 3:
        phi = valeur(ent_0, sign, list_dir)
        ld = valeur(ent_1, sign_1, tab_dir)
        p = valellipse[spin_ellips.get()]
        if p == 0:
            a = 6378137.00
            b = 6356752.314
            f = a ** 2
            f_1 = b ** 2
            f_2 = (sqrt((f - f_1) / f))
            exc_1 = f_2
            esc_2 = (sqrt((f - f_1) / f_1))
            n_fi = a / sqrt(1 - pow(exc_1, 2)) * pow(sin(phi), 2)
            return nav_convertir_frame7(E_f7, N_f7)
        elif p == 1:
            a = 6378249.200
            b = 6356515
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
            return nav_convertir_frame7(E_f7, N_f7)
        else:
            if is_float(ent_a) and is_float(ent_b):
                a = float(ent_a)
                b = float(ent_b)
                f = a ** 2
                f_1 = b ** 2
                exc_1 = sqrt((f - f_1) / f)
                esc_2 = sqrt((f - f_1) / f_1)
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                return nav_convertir_frame7(E_f7, N_f7)
            elif ent_a == '' or ent_b == '':
                return False
    elif az == 3:
        phi = valeur(ent_0, sign, list_dir)
        ld = valeur(ent_1, sign_1, tab_dir)
        p = valellipse[spin_ellips.get()]
        if p == 0 and is_float(phi) and is_float(ld):
            a = 6378137.00
            b = a - a * (1 / 298.257222101)
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
            return nav_convertir_frame7(E_f7, N_f7)
        elif p == 1:
            a = 6378249.200
            b = a - a * (1 / 293.46602048)
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
            return nav_convertir_frame7(E_f7, N_f7)
        else:
            if is_float(ent_a) and is_float(ent_b):
                a = float(ent_a)
                b = float(ent_b)
                f = a ** 2
                f_1 = b ** 2
                exc_1 = sqrt((f - f_1) / f)
                esc_2 = sqrt((f - f_1) / f_1)
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                return nav_convertir_frame7(E_f7, N_f7)
            elif ent_a == '' or ent_b == '':
                return False
    else:
        return False


def nav_convertir_frame7(E_f7, N_f7):
    global n_fi
    E0_f7 = entryframe7_E0.get()
    N0_f7 = entryframe_7N0.get()
    mu_0 = μ_0.get()
    if is_float(E_f7) and is_float(N_f7) and is_float(E0_f7) and is_float(N0_f7) and is_float(mu_0):
        try:
            if sign.get() == 1:
                r0 = float(mu_0) * n_fi * (1 / tan(phi))
                x = float(E_f7) - float(E0_f7)
                y = float(N_f7) - r0 - float(N0_f7)
                gama = atan((-1) * (x / y))
                lamda = gama / sin(phi) + ld
                r = sqrt(x ** 2 + y ** 2)
                l_phi = log(tan(phi / 2 + pi / 4)) + (exc_1 / 2) * log((1 - exc_1 * sin(phi)) / (1 + exc_1 * sin(phi)))
                l = l_phi - (1 / sin(phi)) * log(r / r0)

                val_phi = 2 * atan(exp(l)) - pi / 2
                for i in range(6):
                    p = pow(((1 + exc_1 * sin(val_phi)) / (1 - exc_1 * sin(val_phi))), exc_1 / 2)
                    val_ph = 2 * atan(p * exp(l)) - pi / 2
                    val_phi = val_ph
                lamda = conv_result(lamda)
                val_p = conv_result(val_phi)
                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_ph = "{0:.9f}".format(val_p)
                    return [lamda, val_ph]
                else:
                    return [lamda, val_p]

            else:
                N_f7 = 10000000 - float(N_f7)
                r0 = float(mu_0) * n_fi * (1 / tan(phi))
                x = float(E_f7) - float(E0_f7)
                y = float(N_f7) - r0 - float(N0_f7)
                gama = atan((-1) * (x / y))
                lamda = gama / sin(phi) + ld
                r = sqrt(x ** 2 + y ** 2)
                l_phi = log(tan(phi / 2 + pi / 4)) + (exc_1 / 2) * log((1 - exc_1 * sin(phi)) / (1 + exc_1 * sin(phi)))

                l = l_phi - (1 / sin(phi)) * log(r / r0)
                val_phi = 2 * atan(exp(l)) - pi / 2
                for i in range(6):
                    p = pow(((1 + exc_1 * sin(val_phi)) / (1 - exc_1 * sin(val_phi))), exc_1 / 2)
                    val_ph = 2 * atan(p * exp(l)) - pi / 2
                    val_phi = val_ph
                lamda = conv_result(lamda)
                val_p = conv_result(val_phi)
                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_ph = "{0:.9f}".format(val_p)
                    return [lamda, val_ph]
                else:
                    return [lamda, val_p]

        except (ValueError, ZeroDivisionError):
            return False
    else:
        return False


def nav_convertir_frame8(E_f7, N_f7):
    global a
    global n_fi
    E0_f7 = entryframe8_E0.get()
    N0_f7 = entryframe_8N0.get()
    mu_0 = μ_10.get()
    if is_float(E_f7) and is_float(N_f7) and is_float(E0_f7) and is_float(N0_f7) and is_float(mu_0):
        try:
            if sign.get() == 1:
                phi_1 = float(N_f7) / (float(mu_0) * a)
                n_1 = sqrt(1 + ((esc_2) ** 2) * pow(cos(phi_1), 4))
                v_1 = sqrt(1 + ((esc_2) ** 2) * pow(cos(phi_1), 2))
                epsi = pow(v_1, 2) * (float(E_f7) - float(E0_f7)) / (float(mu_0) * a * sqrt(1 + pow(esc_2, 2)))
                n_b = (float(N_f7) - float(mu_0) * béta(phi_1)) * pow(v_1, 2) / (
                        float(mu_0) * a * sqrt(1 + pow(esc_2, 2))) + atan((tan(phi_1) / v_1))
                delt_ld = (1 / n_1) * atan(tan(2 * atan(exp(epsi)) - pi / 2) / cos(n_b))
                lamda = ld + delt_ld
                h = atan(cos(n_1 * delt_ld) * tan(n_b))
                h_1 = atan((tan(phi_1)) / v_1)
                lphi_1 = log(tan(phi_1 / 2 + pi / 4)) + (exc_1 / 2) * log(
                    (1 - exc_1 * sin(phi_1)) / (1 + exc_1 * sin(phi_1)))
                ll = lphi_1 + (1 / n_1) * (log(tan(h / 2 + pi / 4)) - log(tan(h_1 / 2 + pi / 4)))
                val_ph = 2 * atan(exp(ll)) - pi / 2
                for i in range(6):
                    t_x = (1 + exc_1 * sin(val_ph)) / (1 - exc_1 * sin(val_ph))
                    val_phi = 2 * atan(pow(t_x, exc_1 / 2) * exp(ll)) - pi / 2
                    val_ph = val_phi
                lamda = conv_result(lamda)
                val_p = conv_result(val_ph)
                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_ph = "{0:.9f}".format(val_p)
                    return [lamda, val_ph]
                else:
                    return [lamda, val_p]
            else:
                N_f7 = 10000000 - float(N_f7)
                phi_1 = float(N_f7) / (float(mu_0) * a)
                n_1 = sqrt(1 + (esc_2 ** 2) * pow(cos(phi_1), 4))
                v_1 = sqrt(1 + (esc_2 ** 2) * pow(cos(phi_1), 2))
                epsi = pow(v_1, 2) * (float(E_f7) - float(E0_f7)) / (float(mu_0) * a * sqrt(1 + pow(esc_2, 2)))
                n_b = (float(N_f7) - float(mu_0) * béta(phi_1)) * pow(v_1, 2) / (
                        float(mu_0) * a * sqrt(1 + pow(esc_2, 2))) + atan((tan(phi_1) / v_1))
                delt_ld = (1 / n_1) * atan(tan(2 * atan(exp(epsi)) - pi / 2) / cos(n_b))
                lamda = ld + delt_ld
                h = atan(cos(n_1 * delt_ld) * tan(n_b))
                h_1 = atan(tan(phi_1) / v_1)
                lphi_1 = log(tan(phi_1 / 2 + pi / 4)) + (exc_1 / 2) * log(
                    (1 - exc_1 * sin(phi_1)) / (1 + exc_1 * sin(phi_1)))
                ll = lphi_1 + (1 / n_1) * (log(tan(h / 2 + pi / 4)) - log(tan(h_1 / 2 + pi / 4)))
                val_ph = 2 * atan(exp(ll)) - pi / 2
                for i in range(6):
                    t_x = (1 + exc_1 * sin(val_ph)) / (1 - exc_1 * sin(val_ph))
                    val_phi = 2 * atan(pow(t_x, exc_1 / 2) * exp(ll)) - pi / 2
                    val_ph = val_phi
                lamda = conv_result(lamda)
                val_p = conv_result(val_ph)
                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_phi = "{0:.9f}".format(val_p)
                    return [lamda, val_phi]
                else:
                    return [lamda, val_p]
        except (ValueError, ZeroDivisionError, OverflowError):
            return False
    else:
        return False


def nav_ellipsoide_f8(E_f7, N_f7):
    global n_fi
    global esc_2
    global ld
    global a
    global phi
    global exc_1
    ent_a = entry_a.get()
    ent_b = entry_b.get()
    ent_0 = entry_0.get()
    ent_1 = entry_1.get()
    az = valeunite[spin_unites.get()]
    if is_float(ent_0) and is_float(ent_1) and az != 3:
        phi = valeur(ent_0, sign, list_dir)
        ld = valeur(ent_1, sign_1, tab_dir)
        p = valellipse[spin_ellips.get()]
        if p == 0:
            a = 6378137.00
            b = a - a * (1 / 298.257222101)
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
            return nav_convertir_frame8(E_f7, N_f7)
        elif p == 1:
            a = 6378249.200
            b = a - a * (1 / 293.46602048)
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
            return nav_convertir_frame8(E_f7, N_f7)
        else:
            if is_float(ent_a) and is_float(ent_b):
                a = float(ent_a)
                b = float(ent_b)
                f = a ** 2
                f_1 = b ** 2
                exc_1 = sqrt((f - f_1) / f)
                esc_2 = sqrt((f - f_1) / f_1)
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                return convertir_frame7(E_f7, N_f7)
            elif ent_a == '' or ent_b == '':
                return False
    elif az == 3:
        phi = valeur(ent_0, sign, list_dir)
        ld = valeur(ent_1, sign_1, tab_dir)
        p = valellipse[spin_ellips.get()]
        if p == 0 and is_float(phi) and is_float(ld):
            a = 6378137.00
            b = a - a * (1 / 298.257222101)
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
            return nav_convertir_frame8(E_f7, N_f7)
        elif p == 1:
            a = 6378249.200
            b = a - a * (1 / 293.46602048)
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
            return nav_convertir_frame8(E_f7, N_f7)
        else:
            if is_float(ent_a) and is_float(ent_b):
                a = float(ent_a)
                b = float(ent_b)
                f = a ** 2
                f_1 = b ** 2
                exc_1 = sqrt((f - f_1) / f)
                esc_2 = sqrt((f - f_1) / f_1)
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                return nav_convertir_frame8(E_f7, N_f7)
            elif ent_a == '' or ent_b == '':
                return False
    else:
        return False


global n_fi
global esc_2
global ld
global a
global phi
global exc_1


def ellipsoide(frame):
    global n_fi
    global esc_2
    global ld
    global a
    global phi
    global exc_1
    ent_a = entry_a.get()
    ent_b = entry_b.get()
    ent_0 = entry_0.get()
    ent_1 = entry_1.get()
    az = valeunite[spin_unites.get()]
    if is_float(ent_0) and is_float(ent_1) and az != 3:
        phi1 = valeur(ent_0, sign, list_dir)
        ld1 = valeur(ent_1, sign_1, tab_dir)
        phi = angle(ld1, phi1)[1]
        ld = angle(ld1, phi1)[0]
        p = valellipse[spin_ellips.get()]
        if p == 0:
            a = 6378137.00
            b = 6356752.314
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
            swap(frame)
            return
        elif p == 1:
            a = 6378249.200
            b = 6356515
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = f_2
            esc_2 = sqrt((f - f_1) / f_1)
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
            swap(frame)
            return
        else:
            if is_float(ent_a) and is_float(ent_b):
                try:

                    a = float(ent_a)
                    b = float(ent_b)
                    f = a ** 2
                    f_1 = b ** 2
                    exc_1 = sqrt((f - f_1) / f)
                    esc_2 = sqrt((f - f_1) / f_1)
                    n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                    swap(frame)
                    return
                except:
                    messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')
            elif ent_a == '' or ent_b == '':
                messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')
    elif az == 3:
        try:
            phik = valeur(ent_0, sign, list_dir)
            ldk = valeur(ent_1, sign_1, tab_dir)
            phi = angle(ldk, phik)[1]
            ld = angle(ldk, phik)[0]
            p = valellipse[spin_ellips.get()]
            if p == 0:
                a = 6378137.00
                b = 6356752.314
                f = a ** 2
                f_1 = b ** 2
                f_2 = sqrt((f - f_1) / f)
                exc_1 = f_2
                esc_2 = sqrt((f - f_1) / f_1)
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
                swap(frame)
                return
            elif p == 1:
                a = 6378249.200
                b = 6356515.00
                f = a ** 2
                f_1 = b ** 2
                f_2 = sqrt((f - f_1) / f)
                exc_1 = f_2
                esc_2 = sqrt((f - f_1) / f_1)
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                swap(frame)
                return
            else:
                if is_float(ent_a) and is_float(ent_b):
                    try:

                        a = float(ent_a)
                        b = float(ent_b)
                        f = a ** 2
                        f_1 = b ** 2
                        exc_1 = sqrt((f - f_1) / f)
                        esc_2 = sqrt((f - f_1) / f_1)
                        n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                        swap(frame)
                        return
                    except:
                        messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')
                elif ent_a == '' or ent_b == '':
                    messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')
        except:
            messagebox.showerror(title='Erreur!',
                                 message='Format incorrect !!\n bon format : degrés °minutes\'secondes"')
    else:
        messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')


def ellipsoide_f7():
    global n_fi
    global esc_2
    global ld
    global a
    global phi
    global exc_1
    ent_a = entry_a.get()
    ent_b = entry_b.get()
    ent_0 = entry_0.get()
    ent_1 = entry_1.get()
    az = valeunite[spin_unites.get()]
    if is_float(ent_0) and is_float(ent_1) and az != 3:
        phi1 = valeur(ent_0, sign, list_dir)
        ld1 = valeur(ent_1, sign_1, tab_dir)
        phi = angle(ld1, phi1)[1]
        ld = angle(ld1, phi1)[0]
        p = valellipse[spin_ellips.get()]
        if p == 0:
            a = 6378137.00
            b = 6356752.314
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = float('{0:.11}'.format(f_2))
            esc_2 = sqrt((f - f_1) / f_1)
            esc_2 = float('{0:.11}'.format(esc_2))
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
            return
        elif p == 1:
            a = 6378249.200
            b = 6356515
            f = a ** 2
            f_1 = b ** 2
            f_2 = sqrt((f - f_1) / f)
            exc_1 = float('{0:.11}'.format(exc_1))
            esc_2 = sqrt((f - f_1) / f_1)
            esc_2 = float('{0:.11}'.format(esc_2))
            n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
            return
        else:
            if is_float(ent_a) and is_float(ent_b):
                a = float(ent_a)
                b = float(ent_b)
                f = a ** 2
                f_1 = b ** 2
                exc_1 = sqrt((f - f_1) / f)
                exc_1 = float('{0:.11}'.format(exc_1))
                esc_2 = sqrt((f - f_1) / f_1)
                esc_2 = float('{0:.11}'.format(esc_2))
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                return
            elif ent_a == '' or ent_b == '':
                messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')
    elif az == 3:
        try:
            phi2 = valeur(ent_0, sign, list_dir)
            ld2 = valeur(ent_1, sign_1, tab_dir)
            phi = angle(ld2, phi2)[1]
            ld = angle(ld2, phi2)[0]
            p = valellipse[spin_ellips.get()]
            if p == 0 and is_float(phi) and is_float(ld):
                a = 6378137.00
                b = 6356752.314
                f = a ** 2
                f_1 = b ** 2
                f_2 = sqrt((f - f_1) / f)
                exc_1 = float('{0:.11}'.format(f_2))
                esc_2 = sqrt((f - f_1) / f_1)
                esc_2 = float('{0:.11}'.format(esc_2))
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
                return
            elif p == 1:
                a = 6378249.200
                b = 6356515
                f = a ** 2
                f_1 = b ** 2
                f_2 = sqrt((f - f_1) / f)
                exc_1 = float('{0:.11}'.format(f_2))
                esc_2 = sqrt((f - f_1) / f_1)
                esc_2 = float('{0:.11}'.format(esc_2))
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                return
            else:
                if is_float(ent_a) and is_float(ent_b):
                    a = float(ent_a)
                    b = float(ent_b)
                    f = a ** 2
                    f_1 = b ** 2
                    exc_1 = sqrt((f - f_1) / f)
                    exc_1 = float('{0:.11}'.format(exc_1))
                    esc_2 = sqrt((f - f_1) / f_1)
                    esc_2 = float('{0:.11}'.format(esc_2))
                    n_fi = a / sqrt(1 - pow(exc_1, 2) * pow((sin(phi)), 2))
                    return
                elif ent_a == '' or ent_b == '':
                    messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')
        except:
            messagebox.showerror(title='Erreur!',
                                 message='Format incorrect !!\n bon format : degrés °minutes\'secondes"')

    else:
        messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')


def ellip():
    p = valellipse[spin_ellips.get()]
    if p != 2:
        label_a.config(fg='gray')
        label_b.config(fg='gray')
        entry_a.config(state=DISABLED)
        entry_b.config(state=DISABLED)
    else:
        label_a.config(fg='blue')
        label_b.config(fg='blue')
        entry_a.config(state=NORMAL)
        entry_b.config(state=NORMAL)


def conv(val):
    num = valeunite[spin_unites.get()]
    num1 = (val * pi) / 180
    num2 = (val * pi) / 200
    if num == 1:
        return num1
    elif num == 0:
        return val
    else:
        return num2


def conv_result(val):
    global unit
    num = valeunite[spin_unites.get()]
    num1 = (val * 180) / pi
    num2 = (val * 200) / pi
    if num == 1:
        unit = "°"
        return round(num1, 10)
    elif num == 0:
        unit = "rad"
        return val
    elif num == 2:
        unit = "gr"
        return round(num2, 10)
    elif num == 3:
        dd = abs(val)
        dd = dd * 180 / pi
        d = int(dd)
        tf = (dd - d) * 60
        m1 = int(tf)
        y1 = (tf - m1) * 60
        s1 = float("{0:.5f}".format(y1))
        unit = ''
        if s1 >= 60:
            s = s1 - 60
            m = m1 + 1
            if m >= 60:
                m = m - 60
                d = d + 1
            if val < 0:
                return "-{}°{}'{}\" ".format(d, m, s)
            else:
                return "{}°{}'{}\" ".format(d, m, s)

        if val < 0:
            return "-{}°{}'{}\" ".format(d, m1, s1)
        else:
            return "{}°{}'{}\" ".format(d, m1, s1)
    else:
        pass


def is_float(nomb):
    try:
        float(nomb)
        return True
    except:
        return False


def utmnordsud():
    entN08.set(0)
    entE08.set(500000)
    sign.set(1)
    select_colr(list_dir, sign)
    if sig.get() == 0:
        sign.set(0)
        select_colr(list_dir, sign)
        entN08.set(10000000)


def utmnord():
    entN08.set(0)
    entE08.set(500000)
    sig.set(1)
    select_colr(list_di, sig)
    if sign.get() == 0:
        sig.set(0)
        select_colr(list_di, sig)
        entN08.set(10000000)


def utmspin():
    global phi
    global ld
    numfuseau = spin_utm.get()
    en_0.set(conv_result(0))
    phi1 = valeur(conv_result(0), sign, list_dir)
    valn = (6 * int(numfuseau) - 183) * pi / 180
    en_1.set(conv_result(valn))
    ld1 = valeur(conv_result(valn), sign_1, tab_dir)
    ld = angle(ld1, phi1)[0]
    phi = angle(ld1, phi1)[1]


def is_int(nomb):
    if is_float(nomb):
        if int(nomb) == nomb:
            return True
        else:
            return False


def e_1(n):
    return pow(exc_1, n)


def coef_de_arc(m):
    if m == 1:
        return 1 + (3 / 4) * e_1(2) + (45 / 64) * e_1(4) + (175 / 256) * e_1(6) + (11025 / 16384) * e_1(8) + (
                43659 / 65536) * e_1(10) + (693693 / 1048576) * e_1(12)
    elif m == 2:
        return (-1) * (3 / 8) * e_1(2) - (15 / 32) * e_1(4) - (525 / 1024) * e_1(6) - (2205 / 4096) * e_1(8) - (
                72765 / 131072) * e_1(10) - (297297 / 524288) * e_1(12)
    elif m == 3:
        return (15 / 256) * e_1(4) + (105 / 1024) * e_1(6) + (2205 / 16384) * e_1(8) + (10395 / 65536) * e_1(10) + (
                1486485 / 8388608) * e_1(12)
    elif m == 4:
        return (-1) * (35 / 3072) * e_1(6) - (315 / 12288) * e_1(8) - (31185 / 786432) * e_1(10) - (
                165165 / 3145728) * e_1(12)
    elif m == 5:
        return (315 / 131072) * e_1(8) + (3465 / 524288) * e_1(10) + (99099 / 8388608) * e_1(12)
    elif m == 6:
        return ((-1) * 693 / 1310720) * e_1(10) - (9009 / 5242880) * e_1(12)
    elif m == 7:
        return (1001 / 8388608) * e_1(12)


def béta(m):
    val = coef_de_arc(1) * m
    for i in range(2, 8):
        valu = coef_de_arc(i) * sin(2 * (i - 1) * m)
        val = val + valu

    return val * a * (1 - (exc_1 ** 2))


def angle(ld0, phi0):
    ld__0 = abs(ld0) % (2 * pi)
    phi__0 = abs(phi0) % (2 * pi)
    if ld0 < 0:
        ld__0 = - ld__0
        if -1 * pi > ld__0:
            ld__0 = 2 * pi + ld__0
    if ld0 > 0:
        if pi < ld__0:
            ld__0 = -2 * pi + ld__0
    if phi0 < 0:
        phi__0 = -phi__0
        if -1 * pi > phi__0:
            phi__0 = 2 * pi + phi__0
        if phi0 > 0:
            if pi < phi__0:
                phi__0 = -2 * pi + phi__0
    return [ld__0, phi__0]


def sign_numb(num_1, valu):
    if num_1 == 0:
        return valu
    elif num_1 == 1:
        return (-1) * valu


def help():
    try:
        os.startfile('Présentation du logiciel App géo.pdf')
    except:
        messagebox.showerror(title='Erreur!', message='Fichier non trouvé!')


def buton_convertir_f5():
    global phi_0
    global ld_0
    global u_c
    global showx
    global showy
    global n_phi
    global checked5
    global valx
    global valy
    global valz
    valx = ''
    valy = ''
    valz = ''
    ent_X_0 = entry_X_0.get()
    ent_Y_0 = entry_Y_0.get()
    phi_0 = entry_phi_0.get()
    u_c = entry_u_c.get()
    ld_0 = entry_lambda_0.get()
    try:
        ellipsoide(f5)
        phi0 = valeur(phi_0, signe_1, tab_f5)
        ld0 = valeur(ld_0, signe, list_f5)
        vas = angle(ld0, phi0)
        phi__0 = vas[1]
        ld__0 = vas[0]
        if is_float(u_c) and is_float(ent_X_0) and is_float(ent_Y_0):
            try:
                u_c = float(u_c)
                x_0 = float(ent_X_0)
                y_0 = float(ent_Y_0)
                n_phi = n_fi * u_c
                w_0 = sin(phi__0) * sin(phi__0)
                k_1 = exc_1 * exc_1
                n_fi_0 = a / sqrt(1 - k_1 * w_0)
                t_1 = tan(pi / 4 + phi / 2)
                t_2 = exc_1 / 2
                t_3 = 1 + exc_1 * sin(phi)
                t_4 = 1 - exc_1 * sin(phi)
                l_fi = log(t_1) + t_2 * log(t_4 / t_3)
                v_1 = tan(pi / 4 + phi__0 / 2)
                v_2 = exc_1 / 2
                v_3 = 1 + exc_1 * sin(phi__0)
                v_4 = 1 - exc_1 * sin(phi__0)
                l_fi_0 = log(v_1) + v_2 * log(v_4 / v_3)
                r_1 = (-1) * sin(phi__0) * (l_fi - l_fi_0)
                rayon_0 = u_c * n_fi_0 / tan(phi__0)
                rayon = rayon_0 * exp(r_1)
                omega = (ld - ld__0) * sin(phi__0)
                x_m = x_0 + rayon * sin(omega)
                y_m = y_0 + rayon_0 - rayon * cos(omega)
                f_1 = "{0:.4f}".format(x_m)
                Xm.set("E  = " + str(f_1) + " m")
                f_2 = "{0:.4f}".format(y_m)
                valx = f_1
                valy = f_2
                Ym.set("N = " + str(f_2) + " m")

                '''calcul de l'altération linéaire'''
                A = tan(phi__0) * sqrt((1 - pow(exc_1, 2) * pow(sin(phi__0), 2)))
                nu_c = u_c
                n = sin(phi__0)

                Nu = (rayon * n) / (n_fi * cos(phi))
                alt_mer = (Nu - 1) * pow(10, 6)
                f_3 = "{0:.4f}".format(alt_mer)
                valz = f_3
                oméga.set('alt =' + f_3 + 'ppm')
                checked5 = True
                alt1()

                showx = ld * 180 / pi
                showy = phi * 180 / pi
                label_Ym_1.place(x=675, y=140)
                label_Xm_1.place(x=675, y=110)
                btnRESET.place(x=750, y=220)
                afficherf5.place(x=390, y=220)
            except (ValueError, ZeroDivisionError):
                messagebox.showerror(title='Erreur!', message='Math Error!')
    except:
        messagebox.showerror(title='Erreur!', message='Valeurs érronnées!')


def valeur(nombre, choix, tab_1):
    p = valeunite[spin_unites.get()]
    if p != 3:
        if is_float(nombre):
            chix = choix.get()
            nombre = float(nombre)
            if nombre >= 0:
                if chix == 1:
                    return conv(nombre)
                else:
                    return conv(nombre) * (-1)
            else:
                choix.set(0)
                select_colr(tab_1, choix)
                return conv(nombre)
        else:
            messagebox.showerror(title='Erreur!', message='valeurs erronnées!')
    elif p == 3:
        try:
            chi = choix.get()
            return parse_dms(nombre, chi)
        except Exception as exc:
            raise RuntimeError("erreur") from exc


def buton_convertir_f6():
    label_Ym_f6.place(x=220, y=120)
    lab_Xm_f6.place(x=220, y=70)
    btnRESET_1.place(x=750, y=220)


def switch(val):
    if val == 0:
        entry_u_c.place(x=240, y=230)
        label_x_0_choix.place_forget()
        label_y_0_choix.place_forget()
        entry_X_0.place_forget()
        entry_Y_0.place_forget()
    else:
        entry_u_c.place_forget()
        label_x_0_choix.place(x=240, y=290)
        label_y_0_choix.place(x=240, y=310)
        entry_X_0.place(x=280, y=290)
        entry_Y_0.place(x=280, y=310)


def select_color(tab_1, val):
    p_0 = val.get()
    for i in tab_1:
        i.config(fg='black')
        for h in range(4):
            if p_0 == h:
                tab_1[h].config(fg='blue')


def select_colr(tab_1, val):
    p_0 = val.get()
    for i in tab_1:
        i.config(fg='black')
        for h in range(2):
            if p_0 == h:
                tab_1[h].config(fg='blue')


def parse_dms(entry, dir):
    try:
        part = re.split('[°\'"]+', entry)
        l = len(part)
        if is_float(part[0]) and is_float(part[1]) and is_float(part[2]) and l == 4:
            angle = dms2dd(part[0], part[1], part[2], dir)
            return angle
    except:
        pass


def dms2dd(degré, minute, seconde, dir):
    try:
        dd = abs(float(degré)) + float(minute) / 60 + float(seconde) / (60 * 60)
        if dir == 1:
            if float(degré) >= 0:
                return (dd * pi) / 180
            elif float(degré) <= 0 and dd != 0:
                return - (dd * pi) / 180
        elif dir == 0:
            return -(dd * pi) / 180
    except:
        pass


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def alt1():
    global checked5
    global checked6
    label_altération.place_forget()
    label_oméga_1.place_forget()
    if checkvar.get() == 1:
        if checked5:
            label_oméga_1.place(x=675, y=80)
        if checked6:
            label_altération.place(x=550, y=95)


checked5 = False
checked6 = False


def bouton_f6():
    global valx
    global valy
    global valz
    global showx
    global showy
    global checked6
    valx = ''
    valy = ''
    valz = ''
    tr = valeunite[spin_unites.get()]
    try:
        ellipsoide(f6)

        if ld < 0:
            num_z = 30 + int((ld * 180 / pi) / 6)
        else:
            num_z = 31 + int((ld * 180 / pi) / 6)
        lamda_c = (6 * num_z - 183) * pi / 180
        fg = phi
        ph = abs(fg)

        k__0 = 0.9996

        r = béta(ph)
        r_1 = ld - lamda_c
        n = sqrt(1 + pow(esc_2, 2) * pow(cos(ph), 4))
        v = sqrt(1 + pow(esc_2, 2) * pow(cos(ph), 2))
        x_c = 500000
        r_2 = k__0 * a * sqrt(1 + pow(esc_2, 2))
        r_3 = 2 * pow(v, 2)
        l_1 = 1 + (v * cos(ph) * sin(n * r_1)) / n
        l_2 = 1 - (v * cos(ph) * sin(n * r_1)) / n
        E = x_c + (r_2 / r_3) * log(l_1 / l_2)
        c_1 = k__0 * r
        c_2 = pow(v, 2)
        c_3 = r_2 / c_2
        t_1 = tan(ph) / (v * cos(n * r_1))
        t_2 = tan(ph) / v
        N = c_1 + c_3 * (atan(t_1) - atan(t_2))
        if fg < 0:
            N_1 = 10000000 - N
            N = N_1

        f_1 = "{0:.4f}".format(E)
        Xm_1_f6.set("E = " + str(f_1) + "m")
        f_2 = "{0:.4f}".format(N)
        valx = f_1
        valy = f_2
        Ym_1_f6.set("N = " + str(f_2) + "m")

        ''' altération linéaire '''
        Nu = k__0 / sqrt(1 - pow(sin(r_1), 2) * pow(cos(ph), 2))
        alt_utm = (Nu - 1) * pow(10, 6)
        valz = "{0:.4f}ppm".format(alt_utm)
        label_alt.set("alt = {0:.4f} ppm".format(alt_utm))
        checked6 = True
        alt1()
        showx = ld * 180 / pi
        showy = phi * 180 / pi
        buton_convertir_f6()
    except:
        pass


def convertir_frame7():
    global valx
    global valy
    global n_fi
    valx = ''
    valy = ''
    global showx
    global showy
    ellipsoide_f7()
    E_f7 = entryframe7.get()
    N_f7 = entryframe_7.get()
    E0_f7 = entryframe7_E0.get()
    N0_f7 = entryframe_7N0.get()
    mu_0 = entryframe7mu_0.get()
    if is_float(E_f7) and is_float(N_f7) and is_float(E0_f7) and is_float(N0_f7) and is_float(mu_0):
        try:

            if sign.get() == 1:
                n_fi = a / sqrt(1 - pow(exc_1, 2) * pow(sin(phi), 2))
                r0 = (float(mu_0) * a) / (sqrt(1 - pow(exc_1 * sin(phi), 2)) * tan(phi))
                x = float(E_f7) - float(E0_f7)
                y = float(N_f7) - r0 - float(N0_f7)

                gama = atan(-x / y)
                lamda = gama / sin(phi) + ld
                r = sqrt(x ** 2 + y ** 2)

                l_phi = log(tan(phi / 2 + pi / 4)) + (exc_1 / 2) * log((1 - exc_1 * sin(phi)) / (1 + exc_1 * sin(phi)))
                l = l_phi - (1 / sin(phi)) * log(r / r0)

                val_phi = 2 * atan(exp(l)) - pi / 2
                for i in range(7):
                    p = pow(((1 + exc_1 * sin(val_phi)) / (1 - exc_1 * sin(val_phi))), exc_1 / 2)
                    val_ph = 2 * atan(p * exp(l)) - pi / 2
                    val_phi = val_ph
                showx = lamda * 180 / pi
                showy = val_phi * 180 / pi
                lamda = conv_result(lamda)
                val_phi = conv_result(val_phi)

                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_phi = "{0:.9f}".format(val_phi)
                    lblf7.set("λ = {} {}".format(lamda, unit))
                    lblf_7.set("Φ = {} {}".format(val_phi, unit))
                    valx = "{} {}".format(lamda, unit)
                    valy = "{} {}".format(val_phi, unit)
                else:
                    valx = lamda
                    valy = val_phi

                    lblf7.set("λ = {}".format(lamda))
                    lblf_7.set("Φ = {}".format(val_phi))
                btnRESET_f7.place(x=735, y=220)
                labelframe_7phi.place(x=720, y=50)
                labelframe_7ld.place(x=720, y=90)
                afficherf7.place(x=390, y=220)

            else:
                N_f7 = 10000000 - float(N_f7)
                r0 = float(mu_0) * n_fi * (1 / tan(phi))
                x = float(E_f7) - float(E0_f7)
                y = float(N_f7) - r0 - float(N0_f7)
                gama = atan((-1) * (x / y))
                lamda = gama / sin(phi) + ld
                r = sqrt(x ** 2 + y ** 2)
                px = (1 - exc_1 * sin(phi)) / (1 + exc_1 * sin(phi))
                l_phi = log(tan(phi / 2 + pi / 4)) + (exc_1 / 2) * log(px)

                l = l_phi - (1 / sin(phi)) * log(r / r0)
                val_phi = 2 * atan(exp(l)) - pi / 2
                for i in range(7):
                    r_e = (1 + exc_1 * sin(val_phi)) / (1 - exc_1 * sin(val_phi))
                    p = pow(r_e, exc_1 / 2)
                    val_ph = 2 * atan(p * exp(l)) - pi / 2
                    val_phi = val_ph
                showx = lamda * 180 / pi
                showy = val_phi * 180 / pi
                lamda = conv_result(lamda)
                val_phi = conv_result(val_phi)
                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_phi = "{0:.9f}".format(val_phi)
                    lblf7.set("λ = {} {}".format(lamda, unit))
                    lblf_7.set("Φ = {} {}".format(val_phi, unit))
                    valx = "{} {}".format(lamda, unit)
                    valy = "{} {}".format(val_phi, unit)
                else:
                    valx = lamda
                    valy = val_phi
                    lblf7.set("λ = {}".format(lamda))
                    lblf_7.set("Φ = {}".format(val_phi))
                btnRESET_f7.place(x=735, y=220)
                labelframe_7phi.place(x=720, y=50)
                labelframe_7ld.place(x=720, y=90)
                afficherf7.place(x=390, y=220)

        except:
            messagebox.showerror(title='Erreur!', message='Valeurs érronnées!')
    else:
        messagebox.showerror(title='Erreur!', message='Valeurs érronnées!')


def convertir_frame8():
    global valx
    global valy
    global showx
    global showy
    global a
    global ld
    global phi
    global n_fi
    valx = ''
    valy = ''
    ellipsoide_f7()
    E_f7 = entryframe8.get()
    N_f7 = entryframe_8.get()
    E0_f7 = entryframe8_E0.get()
    N0_f7 = entryframe_8N0.get()
    mu_0 = μ_10.get()

    if is_float(E_f7) and is_float(N_f7) and is_float(E0_f7) and is_float(N0_f7) and is_float(mu_0):
        try:
            if sign.get() == 1:
                phi_1 = float(N_f7) / (float(mu_0) * float(a))
                n_1 = sqrt(1 + ((esc_2) ** 2) * pow(cos(phi_1), 4))
                v_1 = sqrt(1 + ((esc_2) ** 2) * pow(cos(phi_1), 2))
                epsi = pow(v_1, 2) * (float(E_f7) - float(E0_f7)) / (float(mu_0) * float(a) * sqrt(1 + pow(esc_2, 2)))
                n_b = (float(N_f7) - float(mu_0) * béta(phi_1)) * pow(v_1, 2) / (
                        float(mu_0) * float(a) * sqrt(1 + pow(esc_2, 2))) + atan((tan(phi_1) / v_1))
                delt_ld = (1 / n_1) * atan(tan(2 * atan(exp(epsi)) - pi / 2) / cos(n_b))
                lamda = ld + delt_ld
                h = atan(cos(n_1 * delt_ld) * tan(n_b))
                h_1 = atan((tan(phi_1)) / v_1)
                lphi_1 = log(tan(phi_1 / 2 + pi / 4)) + (exc_1 / 2) * log(
                    (1 - exc_1 * sin(phi_1)) / (1 + exc_1 * sin(phi_1)))
                ll = lphi_1 + (1 / n_1) * (log(tan(h / 2 + pi / 4)) - log(tan(h_1 / 2 + pi / 4)))
                val_ph = 2 * atan(exp(ll)) - pi / 2
                for i in range(6):
                    t_x = (1 + exc_1 * sin(val_ph)) / (1 - exc_1 * sin(val_ph))
                    val_phi = 2 * atan(pow(t_x, exc_1 / 2) * exp(ll)) - pi / 2
                    val_ph = val_phi
                showx = lamda * 180 / pi
                showy = val_ph * 180 / pi
                lamda = conv_result(lamda)
                val_p = conv_result(val_ph)
                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_ph = "{0:.9f}".format(val_p)
                    lblf8.set("λ = {} {}".format(lamda, unit))
                    lblf_8.set("Φ = {} {}".format(val_ph, unit))
                    valx = "{} {}".format(lamda, unit)
                    valy = "{} {}".format(val_ph, unit)
                else:
                    valx = lamda
                    valy = val_p
                    lblf8.set("λ = {}".format(lamda))
                    lblf_8.set("Φ = {}".format(val_p))
                btnRESET_f8.place(x=735, y=220)
                labelframe_8phi.place(x=720, y=50)
                labelframe_8ld.place(x=720, y=90)
                afficherf8.place(x=390, y=220)
            else:
                N_f7 = 10000000 - float(N_f7)
                phi_1 = float(N_f7) / (float(mu_0) * float(a))
                n_1 = sqrt(1 + (esc_2 ** 2) * pow(cos(phi_1), 4))
                v_1 = sqrt(1 + (esc_2 ** 2) * pow(cos(phi_1), 2))
                epsi = pow(v_1, 2) * (float(E_f7) - float(E0_f7)) / (float(mu_0) * float(a) * sqrt(1 + pow(esc_2, 2)))
                n_b = (float(N_f7) - float(mu_0) * béta(phi_1)) * pow(v_1, 2) / (
                        float(mu_0) * float(a) * sqrt(1 + pow(esc_2, 2))) + atan((tan(phi_1) / v_1))
                delt_ld = (1 / n_1) * atan(tan(2 * atan(exp(epsi)) - pi / 2) / cos(n_b))
                lamda = ld + delt_ld
                h = atan(cos(n_1 * delt_ld) * tan(n_b))
                h_1 = atan(tan(phi_1) / v_1)
                lphi_1 = log(tan(phi_1 / 2 + pi / 4)) + (exc_1 / 2) * log(
                    (1 - exc_1 * sin(phi_1)) / (1 + exc_1 * sin(phi_1)))
                ll = lphi_1 + (1 / n_1) * (log(tan(h / 2 + pi / 4)) - log(tan(h_1 / 2 + pi / 4)))
                val_ph = 2 * atan(exp(ll)) - pi / 2
                for i in range(6):
                    t_x = (1 + exc_1 * sin(val_ph)) / (1 - exc_1 * sin(val_ph))
                    val_phi = 2 * atan(pow(t_x, exc_1 / 2) * exp(ll)) - pi / 2
                    val_ph = val_phi
                showx = lamda * 180 / pi
                showy = val_ph * 180 / pi
                lamda = conv_result(lamda)
                val_p = conv_result(val_ph)
                if valeunite[spin_unites.get()] != 3:
                    lamda = "{0:.9f}".format(lamda)
                    val_phi = "{0:.9f}".format(val_p)
                    lblf8.set("λ = {} {}".format(lamda, unit))
                    lblf_8.set("Φ = {} {}".format(val_phi, unit))
                    valx = "{} {}".format(lamda, unit)
                    valy = "{} {}".format(val_phi, unit)
                else:
                    valx = lamda
                    valy = val_p
                    lblf8.set("λ = {}".format(lamda))
                    lblf_8.set("Φ = {}".format(val_p))

                btnRESET_f8.place(x=735, y=220)
                labelframe_8phi.place(x=720, y=50)
                labelframe_8ld.place(x=720, y=90)
                afficherf8.place(x=390, y=220)
        except:
            messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')
    else:
        messagebox.showerror(title='Erreur!!', message='Valeurs érronnées!!')


def autre_ellipse():
    label_a.place_forget()
    label_b.place_forget()
    entry_a.place_forget()
    entry_b.place_forget()
    if valellipse[spin_ellips.get()] == 2:
        label_a.place(x=745, y=138)
        label_b.place(x=745, y=160)
        entry_a.place(x=860, y=138)
        entry_b.place(x=860, y=160)


def unite():
    try:
        global idx
        global phi
        global ld
        if idx == 7 or idx == 8:
            if en_0.get() != '' and en_1.get() != '':
                e_0 = conv_result(phi)
                e_1 = conv_result(ld)
                en_0.set(e_0)
                en_1.set(e_1)
        else:
            pass
    except:
        pass


def lambertzone():
    nm = parametre[spin_lambert.get()]
    fii = conv_result(nm[0])
    lamdaa = conv_result(nm[1])
    tab1 = [en_0, en_1, f7E0, f7N0, μ_0]
    tab2 = [fii, lamdaa, nm[2], nm[3], nm[4]]
    for i in range(5):
        tab1[i].set(tab2[i])
    phi1 = valeur(fii, sign, list_dir)
    ld1 = valeur(lamdaa, sign_1, tab_dir)
    phi = angle(ld1, phi1)[1]
    ld = angle(ld1, phi1)[0]


############################################################################################################

bton4 = Button(f1, bg=couleurs[0], fg='black', width=20, text='Géographique', font='Times 15 italic', relief=RAISED,
               command=lambda: swap(f4))
bton4.place(x=600, y=250)
bton5 = Button(f1, bg=couleurs[0], fg='black', width=20, text=' Planes de Lambert', font='Times 15 italic',
               relief=RAISED, command=lambda: swap(frame7))
bton5.place(x=105, y=250)
bton6 = Button(f1, bg=couleurs[0], fg='black', width=20, text='Planes UTM', font='Times 15 italic', relief=RAISED,
               command=lambda: swap(frame8))
bton6.place(x=355, y=360)

bton3 = Button(f3, bg=couleurs[0], fg='black', height=2, width=15, text='Commencer', font='Times 20 italic',
               command=lambda: swap(f1))
bton3.place(x=380, y=250)
img = ImageTk.PhotoImage(Image.open(r"images\retour.png"))
bton7 = Button(root, width=30, height=30, image=img, command=retourn)
btonhelp = Button(root, width=3, bg='darkgreen', text='?', font='Times 13 bold', cursor='hand2',
                  activebackground='lightgreen', fg='white', command=help)
navba = Button(root, width=30, height=30, image=navbar, command=button_navbar)
bton11 = Button(root, bg='red', height=1, fg='WHITE', text='Quitter', font='Times 10 italic', command=quitter)
bton11.place(x=940, y=465)

# f4 ##########################################################################

label4 = Label(f4, bg=couleurs[8], width=10, fg='black', text='Latitude:', font='Times 13 bold')
label4.place(x=110, y=100)

label6 = Label(f4, bg=couleurs[8], width=10, fg='black', text='Longitude:', font='Times 13 bold')
label6.place(x=110, y=150)

labelellip = Label(f4, bg=couleurs[8], fg='black', text='Ellipsoide:', font='Times 13 bold').place(x=650, y=100)
label8 = Label(f4, height=30, image=photo, fg=couleurs[8], compound=CENTER,
               text='Convertir des Coordonnées géographique', font='Times 18 ')
label8.pack(pady=10, side=TOP, anchor=N, fill=X)
labelunit = Label(f4, bg=couleurs[8], fg='black', text='Unités:', font='Times 13 bold').place(x=405, y=100)

ellips = ["IAG_GRS80", "Clarke_1880_IGN", "autre"]
valellipse = {"Clarke_1880_IGN": 1, "autre": 2, "IAG_GRS80": 0}

spin_ellips = Spinbox(f4, font='Times 13 italic', bg='#6A6454', values=ellips, width=20, state='readonly',
                      command=autre_ellipse)
spin_ellips.place(x=745, y=100)

units = ["d°m\'s\"", "Degré", "Grade", "Radian"]
valeunite = {"Degré": 1, "Grade": 2, "Radian": 0, "d°m\'s\"": 3}

spin_unites = Spinbox(f4, font='Times 12 italic', bg='#6A6454', values=units, width=9, state='readonly', command=unite)
spin_unites.place(x=475, y=100)

sign = IntVar()
sign.set(1)
NORD = Radiobutton(f4, bg=couleurs[8], width=1, value=1, variable=sign, fg='blue', activebackground=couleurs[2],
                   text='N', font='Times 7', command=lambda: [select_colr(list_dir, sign), utmnord()])
NORD.place(x=273, y=94)
SUD = Radiobutton(f4, bg=couleurs[8], width=1, value=0, variable=sign, activebackground=couleurs[2], text='S',
                  font='Times 7 ', command=lambda: [select_colr(list_dir, sign), utmnord()])
SUD.place(x=273, y=110)

list_dir = [SUD, NORD]

sign_1 = IntVar()
sign_1.set(1)
EST = Radiobutton(f4, bg=couleurs[8], width=1, value=1, variable=sign_1, fg='blue', activebackground=couleurs[2],
                  text='E', font='Times 7', command=lambda: select_colr(tab_dir, sign_1))
EST.place(x=273, y=144)
ouest = Radiobutton(f4, bg=couleurs[8], width=1, value=0, variable=sign_1, activebackground=couleurs[2], text='O',
                    font='Times 7', command=lambda: select_colr(tab_dir, sign_1))
ouest.place(x=273, y=160)
tab_dir = [ouest, EST]

en_1 = StringVar()
en_0 = StringVar()

entry_0 = Entry(f4, width=10, textvariable=en_0, font='Times 14 italic')
entry_0.place(x=165, y=100)

entry_1 = Entry(f4, width=10, textvariable=en_1, font='Times 14 italic')
entry_1.place(x=165, y=150)

label_a = Label(f4, bg=couleurs[8], width=14, text='Demi-grand axe =', font='Times 10 italic')
label_b = Label(f4, bg=couleurs[8], width=14, text='Demi-petit axe=', font='Times 10 italic')

checkvar = IntVar()
alter = Checkbutton(f4, text='Calculer l\'altération linéaire', variable=checkvar, offvalue=0, onvalue=1,
                    activebackground=couleurs[2], bg=couleurs[8], font='Times 13 bold', command=alt1)
alter.place(x=405, y=150)

ent_b = StringVar()
ent_a = StringVar()
entry_a = Entry(f4, width=11, font='Tims 10 italic')
entry_b = Entry(f4, width=11, font='Tims 10 italic')

btnf1 = Button(f4, bg=couleurs[0], fg='black', width=15, text='Convertir (Lambert)', font='Times 13 italic',
               command=lambda: ellipsoide(f5))
btnf2 = Button(f4, bg=couleurs[0], width=15, fg='black', text='Convertir (UTM)', font='Times 13 italic',
               command=bouton_f6)
btnf2.place(x=150, y=300)
btnf1.place(x=600, y=300)

######################################

un = IntVar()

uni = []
for i in range(1, 61):
    uni.append(i)
spin_utm = Spinbox(f4, font='Times 14 italic', bg='#6A6454', textvariable=un, values=uni, width=4, state='readonly',
                   command=utmspin)
un.set(28)
labelutm = Label(f4, bg=couleurs[8], fg='black', text='Zone UTM:', font='Times 13 bold')

sig = IntVar()
sig.set(1)
NOR = Radiobutton(f4, bg=couleurs[8], width=1, value=1, variable=sig, fg='blue', activebackground=couleurs[2],
                  text='N', font='Times 7', command=lambda: [select_colr(list_di, sig), utmnordsud()])

SU = Radiobutton(f4, bg=couleurs[8], width=1, value=0, variable=sig, activebackground=couleurs[2], text='S',
                 font='Times 7 ', command=lambda: [select_colr(list_di, sig), utmnordsud()])

list_di = [SU, NOR]
parametre = {'I': [55 * pi / 200, (2 + 20 / 60 + 14.025 / 3600) * pi / 180, 600000, 200000, 0.99987734],
             'II': [52 * pi / 200, (2 + 20 / 60 + 14.025 / 3600) * pi / 180, 600000, 200000, 0.99987742],
             'III': [49 * pi / 200, (2 + 20 / 60 + 14.025 / 3600) * pi / 180, 600000, 200000, 0.99987750],
             'IV': [46.85 * pi / 200, (2 + 20 / 60 + 14.025 / 3600) * pi / 180, 234.358, 185861.369, 0.99994471],
             'II étendu': [52 * pi / 200, (2 + 20 / 60 + 14.025 / 3600) * pi / 180, 600000, 2200000, 0.99987742],
             '93': [46.5 * pi / 180, 3 * pi / 180, 700000, 6600000, 0.99905103]}
listlambert = ['I', 'II', 'III', 'IV', 'II étendu', '93']

spin_lambert = Spinbox(f4, font='Times 14 italic', bg='#6A6454', values=listlambert, width=7, state='readonly',
                       command=lambertzone)

labelambert = Label(f4, bg=couleurs[8], fg='black', text='Lambert zone:', font='Times 12 bold')

# f5 #########################################

afficherf5 = Button(f5, bg=couleurs[0], width=20, fg='black', text='Afficher sur Google Earth', font='Times 12 italic',
                    command=display_on_map)

btnUTM = Button(f5, bg=couleurs[0], height=1, width=7, fg='black', text='Convertir', font='Times 12 italic',
                command=buton_convertir_f5)
btnUTM.place(x=150, y=220)
btnRESET = Button(f5, bg=couleurs[5], height=1, width=7, fg='black', text='exporter', font='Times 12 italic',
                  command=exporter)

labelf5 = Label(f5, bg='#025669', fg=couleurs[8], text="Conversion en coodonnées Lambert", font='Times 15 italic')
labelf5.place(x=360, y=5)

label_phi_0 = Label(f5, bg=couleurs[8], width=5, fg='black', text='Φ_0 =', font='Times 13 bold').place(x=105, y=80)
label_lambda_0 = Label(f5, bg=couleurs[8], fg='black', width=5, text='λ_0 =', font='Times 13 bold').place(x=105, y=140)

phi_0 = StringVar()
ld_0 = StringVar()
entry_phi_0 = Entry(f5, width=10, font='Times 14 italic')
entry_phi_0.place(x=165, y=80)
entry_lambda_0 = Entry(f5, width=10, font='Times 14 italic')
entry_lambda_0.place(x=165, y=140)

oméga = StringVar()
Xm = StringVar()
Ym = StringVar()

label_oméga_1 = Label(f5, width=20, bg=couleurs[8], textvariable=oméga, fg='darkblue', font='Times 13 bold')

label_Xm_1 = Label(f5, width=20, bg=couleurs[8], textvariable=Xm, fg='darkblue', font='Times 13 bold')

label_Ym_1 = Label(f5, width=20, bg=couleurs[8], textvariable=Ym, fg='darkblue', font='Times 13 bold')

signe = IntVar()
signe.set(1)
EST_f5 = Radiobutton(f5, bg=couleurs[8], width=1, value=1, variable=signe, fg='blue', activebackground=couleurs[2],
                     text='E', font='Times 7 ', command=lambda: select_colr(list_f5, signe))
EST_f5.place(x=273, y=135)
ouest_f5 = Radiobutton(f5, bg=couleurs[8], width=1, value=0, variable=signe, activebackground=couleurs[2], text='O',
                       font='Times 7', command=lambda: select_colr(list_f5, signe))
ouest_f5.place(x=273, y=152)
list_f5 = [ouest_f5, EST_f5]

signe_1 = IntVar()
signe_1.set(1)
NORD_f5 = Radiobutton(f5, bg=couleurs[8], width=1, value=1, variable=signe_1, fg='blue', activebackground=couleurs[2],
                      text='N', font='Times 7 ', command=lambda: select_colr(tab_f5, signe_1))
NORD_f5.place(x=273, y=75)
SUD_f5 = Radiobutton(f5, bg=couleurs[8], width=1, value=0, variable=signe_1, activebackground=couleurs[2], text='S',
                     font='Times 7', command=lambda: select_colr(tab_f5, signe_1))
SUD_f5.place(x=273, y=92)
tab_f5 = [SUD_f5, NORD_f5]

u_c = StringVar()
u_c.set(1)

label_u_c = Label(f5, bg=couleurs[8], width=5, fg='black', text='μ_c =', font='Times 13 bold')
label_u_c.place(x=362, y=140)
entry_u_c = Entry(f5, width=8, textvariable=u_c, font='Times 14 italic')
entry_u_c.place(x=420, y=140)

label_x_0_choix = Label(f5, bg=couleurs[8], width=5, fg='black', text='X_0 =', font='Times 13 bold').place(x=362,
                                                                                                           y=80)

label_y_0_choix = Label(f5, bg=couleurs[8], fg='black', width=5, text='Y_0 =', font='Times 13 bold').place(x=362,
                                                                                                           y=110)

entx = StringVar()
ent_X_0 = StringVar()

enty = StringVar()
ent_Y_0 = StringVar()

entry_X_0 = Entry(f5, width=8, textvariable=entx, font='Times 14 italic')
entry_X_0.place(x=420, y=80)

entry_Y_0 = Entry(f5, width=8, textvariable=enty, font='Times 14 italic')
entry_Y_0.place(x=420, y=110)

listEntry = [enty, entx, u_c, oméga, Xm, Ym]

# f6 ##################################################################################

afficher = Button(f6, bg=couleurs[0], width=20, fg='black', text='Afficher sur Google Earth', font='Times 12 italic',
                  command=display_on_map)
btnlambert = Button(f6, bg=couleurs[0], width=8, fg='black', text='Recalculer', font='Times 12 italic',
                    command=bouton_f6)
btnlambert.place(x=500, y=220)
afficher.place(x=150, y=220)
btnRESET_1 = Button(f6, bg=couleurs[0], width=8, fg='black', text='Exporter', font='Times 12 italic',
                    command=exporter)

labelf6 = Label(f6, bg='#025669', fg=couleurs[8], text="Conversion en coodonnées UTM", font='Times 16 italic')
labelf6.place(x=360, y=1)

# variabes Lambert résultats#################################

Xm_1_f6 = StringVar()
Ym_1_f6 = StringVar()

lab_Xm_f6 = Label(f6, bg=couleurs[8], width=20, textvariable=Xm_1_f6, fg='darkblue', font='Times 13 bold')

label_Ym_f6 = Label(f6, bg=couleurs[8], width=20, textvariable=Ym_1_f6, fg='darkblue', font='Times 13 bold')

label_alt = StringVar()

label_altération = Label(f6, bg=couleurs[8], textvariable=label_alt, fg='darkblue', font='Times 13 bold')

# frame7 ###################################################################################

afficherf7 = Button(frame7, bg=couleurs[0], width=20, fg='black', text='Afficher sur Google Earth',
                    font='Times 12 italic',
                    command=display_on_map)
labelframe7 = Label(frame7, bg=couleurs[8], width=5, text="E_0 = ", font='Times 13 bold')
labelframe7.place(x=105, y=30)

labelframe_7 = Label(frame7, bg=couleurs[8], width=4, text="E =", font='Times 13 bold')
labelframe_7.place(x=410, y=50)

entryframe7 = Entry(frame7, width=10, font='Times 14 italic')
entryframe7.place(x=460, y=50)

entryframe_7 = Entry(frame7, width=10, font='Times 14 italic')
entryframe_7.place(x=460, y=100)

lblf7 = StringVar()
lblf_7 = StringVar()

labelframe_7phi = Label(frame7, fg='steelblue', bg=couleurs[8], textvariable=lblf7, font='Times 14 bold')

labelframe_7ld = Label(frame7, bg=couleurs[8], fg='steelblue', textvariable=lblf_7, font='Times 14 bold')

labelframe_7_E0 = Label(frame7, bg=couleurs[8], width=5, text="N_0 =", font='Times 13 bold')
labelframe_7_E0.place(x=105, y=80)

f7E0 = StringVar()
f7E0.set(600000)

entryframe7_E0 = Entry(frame7, textvariable=f7E0, width=10, font='Times 14 italic')
entryframe7_E0.place(x=165, y=30)

f7N0 = StringVar()
f7N0.set(200000)

labelframe_7N0 = Label(frame7, bg=couleurs[8], width=4, text="N =", font='Times 13 bold')
labelframe_7N0.place(x=410, y=100)

entryframe_7N0 = Entry(frame7, textvariable=f7N0, width=10, font='Times 14 italic')
entryframe_7N0.place(x=165, y=80)

btngéo = Button(frame7, bg=couleurs[0], width=8, fg='black', text='Convertir', font='Times 12 italic',
                command=convertir_frame7)
btngéo.place(x=140, y=220)
btnRESET_f7 = Button(frame7, bg=couleurs[0], width=8, fg='black', text='Exporter', font='Times 12 italic',
                     command=exporter)

labelframe_7_mu_0 = Label(frame7, bg=couleurs[8], width=5, text="μ_0 =", font='Times 13 bold')
labelframe_7_mu_0.place(x=105, y=130)

μ_0 = StringVar()
μ_0.set(0.999877341)

entryframe7mu_0 = Entry(frame7, width=10, textvariable=μ_0, font='Times 14 italic')
entryframe7mu_0.place(x=165, y=130)

# frame8 ###########################################################################################################

afficherf8 = Button(frame8, bg=couleurs[0], width=20, fg='black', text='Afficher sur Google Earth',
                    font='Times 12 italic',
                    command=display_on_map)
lblf8 = StringVar()
lblf_8 = StringVar()

labelframe_8phi = Label(frame8, fg='steelblue', bg=couleurs[8], textvariable=lblf8, font='Times 14 bold')

labelframe_8ld = Label(frame8, bg=couleurs[8], fg='steelblue', textvariable=lblf_8, font='Times 14 bold')

labelframe_8_E0 = Label(frame8, bg=couleurs[8], width=5, text="N_0 =", font='Times 13 bold')
labelframe_8_E0.place(x=105, y=80)

entE08 = StringVar()
entN08 = StringVar()
entN08.set(0)
entE08.set(500000)
entryframe8_E0 = Entry(frame8, width=10, textvariable=entE08, font='Times 14 italic')
entryframe8_E0.place(x=165, y=30)

labelframe_8N0 = Label(frame8, bg=couleurs[8], width=4, text="N =", font='Times 13 bold')
labelframe_8N0.place(x=410, y=100)

entryframe_8N0 = Entry(frame8, width=10, textvariable=entN08, font='Times 14 italic')
entryframe_8N0.place(x=165, y=80)

btngéo1 = Button(frame8, bg=couleurs[0], height=1, width=7, fg='black', text='Convertir', font='Times 12 italic',
                 command=convertir_frame8)
btngéo1.place(x=140, y=220)
btnRESET_f8 = Button(frame8, bg=couleurs[0], height=1, width=7, fg='black', text='Exporter', font='Times 12 italic',
                     command=exporter)

labelframe_8_mu_0 = Label(frame8, bg=couleurs[8], width=5, text="μ_0 =", font='Times 13 bold')
labelframe_8_mu_0.place(x=105, y=130)

μ_10 = StringVar()
μ_10.set(0.9996)

entryframe8mu_0 = Entry(frame8, width=10, textvariable=μ_10, font='Times 14 italic')
entryframe8mu_0.place(x=165, y=130)

labelframe8 = Label(frame8, bg=couleurs[8], width=5, text="E_0 = ", font='Times 13 bold')
labelframe8.place(x=105, y=30)

labelframe_8 = Label(frame8, bg=couleurs[8], width=4, text="E =", font='Times 13 bold')
labelframe_8.place(x=410, y=50)

entryframe8 = Entry(frame8, width=10, font='Times 14 italic')
entryframe8.place(x=460, y=50)

entryframe_8 = Entry(frame8, width=10, font='Times 14 italic')
entryframe_8.place(x=460, y=100)

# navbar frame #####################################################################################################


nav_label = Label(f_navbar, fg='white', text='Convertir un fichier de points\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',
                  image=na_image, compound=CENTER, font='Times 14 bold').place(relheight=1, relwidth=1)
exitbutton = Button(f_navbar, image=exit_ico, height=30, bg='darkblue', activebackground='darkblue', width=30,
                    command=file_name)
exitbutton.place(x=215, y=105)
filename = StringVar()
filename.set("Ouvrir un fichier texte")
nav_labelfile_name = Label(f_navbar, fg='white', textvariable=filename, height=30, width=200, image=na_image,
                           compound=CENTER, font='Times 10 italic')
nav_labelfile_name.place(x=5, y=105)
nav_séparateur = Label(f_navbar, fg='white', text='Séparateur 1 :', height=20, width=100, image=na_image,
                       compound=CENTER, font='Times 12 bold')
nav_séparateur.place(x=5, y=205)
spteurs = ['Tabulation', 'Espace', 'Virgule', 'Deux-points', 'Point-virgule', 'Tiret']
DISption = ['(#nom, X, Y, Z)', '(#nom, X, Y)', '(X, Y,Z)', '( X, Y)']
nav_sp1 = Spinbox(f_navbar, font='Times 12 bold', width=11, values=spteurs)
nav_sp1.place(x=120, y=205)
nav_séparateur2 = Label(f_navbar, fg='white', text='Séparateur 2 :', height=20, width=100, image=na_image,
                        compound=CENTER, font='Times 12 bold')
nav_séparateur2.place(x=5, y=245)
spteur = {"Tabulation": '\t', "Virgule": ',', "Point-virgule": ';', "Deux-points": ':', "Espace": ' ', 'Tiret': '-'}
nav_sp2 = Spinbox(f_navbar, font='Times 12 bold', width=11, values=spteurs)
nav_sp2.place(x=120, y=245)
nav_sp3 = Spinbox(f_navbar, font='Times 12 bold', width=11, values=spteurs)
nav_sp3.place(x=120, y=285)
nav_séparateur3 = Label(f_navbar, fg='white', text='Séparateur 3 :', height=20, width=100, image=na_image,
                        compound=CENTER, font='Times 12 bold')
nav_séparateur3.place(x=5, y=285)

nav_convert = Button(f_navbar, fg=couleurs[0], cursor='hand2', text='Convertir', font='Times 11', command=ask_string)
nav_convert.place(x=15, y=370)

nav_afficher = Button(f_navbar, fg=couleurs[0], cursor='hand2', text='Afficher sur Google Earth', font='Times 11',
                      command=displayfilepoint)
nav_afficher.place(x=90, y=370)

# création changement de couleur quand le curseur est dessus


butons = [bton3, bton5, bton6, bton4, bton11, btnf1, btnf2, btnUTM, btnRESET, btnlambert,
          btnRESET_1, btngéo, btnRESET_f7, afficher, afficherf5, afficherf7, btngéo1, afficherf8, btnRESET_f8]

for bton in butons:
    parcourir_bouton(bton)
    bton.config(cursor="hand2")
root.protocol('WM_DELETE_WINDOW', quitter)

if __name__ == '__main__':
    root.mainloop()
