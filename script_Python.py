#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:43:27 2022

@author: secke
"""
import mysql.connector
#import random


##############la fonction des numéros ####################
def numero(x):
    """la fonction pour vérifier la validité des numéros
    """
    from string import ascii_uppercase as Majuscul
    chiffre=['0','1','3','4','5','6','7','8','9']
    if (([i for i in Majuscul  if (i in x)==True]) and ([j for j in chiffre if (j in x)==True])) and (len(x)==7):
        return True
    else:
        return False

############ la fonction des prenoms et celle des noms ################
def prenom(x):
    """la fonction pour valider les prénoms obtenus
    """
    from string import ascii_letters
    
    if ([i for i in ascii_letters  if x[0]==i]) and len(x)>=3:
        return True
    else:
        return False
def nom(x):
    """
    la fonction pour valider les noms obtenus"""
    from string import ascii_letters
    if ([i for i in ascii_letters  if x[0]==i]) and len(x)>=2:
        return True
    else:
        return False
############### la fonction des calsse ########################
def classe(x:str()):
    """la fonction pour la validité du format des classes
    """
    collez=['6em A','6em B','5em A','5em B','4em A','4em B','3em A','3em B']
    if x in collez:
        return True
    else:
        return False


############### fonctions pour les dates #####################
def formattaz(x):
    """
    la fonction de formattage des dates"""
    
    for i in x:
        if ('/'==i) or (' '==i) or ('_'==i) or (','==i) or (';'==i) or (':'==i) or ('.'==i):
            x=x.replace(i,'-') 
    return x


def ConverMois(x):
    """
    cette fonction nous permet de convertir les mois """
    
    xo=x.split("-")
    if len(xo)==3 and (xo[1] in 'janvier'):
        xo[1]='01'
    elif len(xo)==3 and (xo[1] in 'fevrier'):
        xo[1]='02'
    elif len(xo)==3 and (xo[1] in 'mars'):
        xo[1]='03'
    elif len(xo)==3 and (xo[1] in 'avril'):
        xo[1]='04'
    elif len(xo)==3 and (xo[1] in 'mai'):
        xo[1]='05'
    elif len(xo)==3 and (xo[1] in 'juin'):
        xo[1]='06'
    elif len(xo)==3 and (xo[1] in 'juillet'):
        xo[1]='07'
    elif len(xo)==3 and (xo[1] in 'aout'):
        xo[1]='08'
    elif len(xo)==3 and (xo[1] in 'septembre'):
        xo[1]='09'
    elif len(xo)==3 and (xo[1] in 'octobre'):
        xo[1]='10'
    elif len(xo)==3 and (xo[1] in 'novembre'):
        xo[1]='11'
    elif len(xo)==3 and (xo[1] in 'decembre'):
        xo[1]='12'
    return xo

def reformataz(x):
    #xo=x.split('-')
    annee=int(x[2])
    #mois=xo[1]
    #jour=xo[0]
    if annee>20:
        annee='19' + str(annee)
        ma_date=annee + '-' + str(x[1])+'-' + str(x[0])
        return ma_date
    elif annee<20 and annee<10:
        annee='200' + str(annee)
        ma_date=annee + '-' + str(x[1])+'-' + str(x[0])
        return ma_date
    elif annee<20 and annee>=10:
        annee='20' + str(annee)
        ma_date=annee + '-' + str(x[1])+'-' + str(x[0])
        return ma_date


def DateValid(jour,mois,an):
    """ 
    La fonction pour vérifier la validité des dates """

    if (jour.isnumeric()==True) and (an.isnumeric()==True):
        jour=int(jour)
        mois=int(mois)
        an=int(an)
        if (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12) and (jour<=31):
            return True
        elif (mois==4 or mois==6 or mois==9 or mois==11) and (jour<=30):
            return True
        elif (mois==2) and (an%4==0 and an%100!=0) and (jour<=29):
            return True
        elif (mois==2) and (an%4!=0 or an%100==0) and (jour<=28):
            return True
    else:
        return False

######### Programme Principal pour le traitement des données(valides vs invalides) #############
import csv
taf=open('Projet_Python.csv', 'r')
cles=["CODE","Numero","Nom","Prénom","Date de naissance","Classe","Note","Moyenne générale"]
cles_inv=["CODE","Numero","Nom","Prénom","Date de naissance","Classe","Note"]
lire=csv.DictReader(taf)
n0=0
n1=0
valide=open('fichier_valid.csv','w')
ecrire=csv.DictWriter(valide, fieldnames=cles)
ecrire.writeheader()
invalide=open('fichier_invalid.csv','w')
ecrire_inv=csv.DictWriter(invalide, fieldnames=cles_inv)
ecrire_inv.writeheader()



ma_connex=mysql.connector.connect(host="localhost", user="root", password="secke2022", database="info_etudiant", auth_plugin="mysql_native_password")
crayon=ma_connex.cursor()

crayon.execute("select id_etudiant, numero from etudiant")
list_id_etu=[]
for s in crayon.fetchall():
    val_id_etu=s[0]
    val_num_etu=s[1]
    list_id_etu.append((val_id_etu,val_num_etu))

#print("test deuxieme", list_id_etu)   
crayon.execute("select id_matiere, nom from matiere")
list_id_mat=[]
for t in crayon.fetchall():
    val_id_mat=t[0]
    val_num_mat=t[1]
    list_id_mat.append((val_id_mat,val_num_mat))
#print("secke",list_id_mat)



for l in lire:
    l['Date de naissance']=formattaz(l['Date de naissance'])
    Date_cvt=ConverMois(l["Date de naissance"])
    if (numero(l["Numero"])==True) and (DateValid(Date_cvt[0],Date_cvt[1],Date_cvt[2])==True) and (prenom(l["Prénom"])==True) and (nom(l["Nom"])==True) and (classe(l["Classe"])==True):
        yyyy=reformataz(Date_cvt)
        l['Date de naissance']=yyyy
        note=l["Note"].split("#")
        n_mat=0
        s_mat=0
        Note=[]
        ##
        nom_matiere_sql=[]
        for matiere in note:
            se=matiere.split("[")[1].split(']')[0]
            nom_mat=matiere.split("[")[0]
            se1=se.split(":")
            ntt0=se1[0].split(";")
            ntt0.append(se1[1])
            ntt=ntt0
            nouv_nt=[]
            for carac in ntt:
                for c in carac:
                    if c==',':
                        vv=carac.replace(c,'.')
                        carac=vv
                nouv_nt.append(carac)
                matiere=list(map(float,nouv_nt))
            nom_matiere_sql.append(nom_mat)
       
            Note.append([matiere,nom_mat])
            
        #### c'est ici que je vais prendre les data de ma BDmySQL(table matières) ###    
        
                
        #for z in range(len(Note)):
         #   val_d1=Note[z][0][0]
          #  val_d2=Note[z][0][1]
           # val_d3=l['Note'][u][2]
           # val_ex=Note[z][0][-1]
            #val_nom=Note[z][1]
            #val_col_matiere.append((val_nom,val_d1,val_d2,val_ex))
            #print(Note[z][0][0])
        
        
        
        col_bulletin="insert into bulletin(notes, type, id_edu, id_mat) values(%s,%s,%s,%s)"
        val_col_bull=[]
        
        list_matiere=[]
        for z in range(len(Note)):
           
            val_nom_mat=Note[z][1].strip()
            #print(val_nom)
            
            if val_nom_mat[0:3] in 'Français':
                val_nom_mat='Français'
                list_matiere.append(val_nom_mat)
            else:
                list_matiere.append((val_nom_mat))

            
            #val_col_matiere.append((val_nom,))

            
        #print(val_col_matiere)
 
        
        
        
        #crayon.executemany(col_matiere,val_col_matiere)
        #ma_connex.commit()
        ####################### FIN ###############################
        
        
        note=[Note[i][0] for i in range(len(Note))]
        n=0
        som=0
        nm_matiere=nom_matiere_sql[0]
        for s in range(len(note)):
            n_mat=n_mat+1
            j=note[s]
            for i in range(len(j)-1):
                n=n+1
                som=som+j[i]
            moy=((som/n)+2*j[-1])/3
            s_mat=s_mat+moy
            moy_gen=s_mat/n_mat
            
            ## je dois enlever les commentaire ci-dessous pour un bon l'affichage de la colonne note.
            
            #note.insert(note0.index(j),f"{Note[s][1]}:{j} moyenne[{round(moy,2)}]")
            #del note[note.index(j)]
        l["Note"]=note
        l["Moyenne générale"]=round(moy_gen,2)
        
        ecrire.writerow(l)
        n0=n0+1
        ###################### les données des tables bulletin et étudiant ###############"""
       
        ############################## table étudiant ######################
        col="insert into etudiant(code, numero, nom, prenom, date_naissance,classe) values(%s,%s,%s,%s,%s,%s)"
        val_col=[]
        
        ########################" table note ################################
        #col_note="insert into note(moyenne_general) values(%s)"
        #val_col_note=[]
        
       ############# data étudiant ##################
        val_code=l['CODE']
        val_num=l['Numero']
        #print(val_num)
        val_nom=l['Nom']
        val_pre=l['Prénom']
        val_dn=l['Date de naissance']
        val_clas=l['Classe']
        #print(l['CODE'])
        
        #print(val_nom)
            
        val_col.append((val_code,val_num,val_nom,val_pre,val_dn,val_clas)) 
            
        ####### ##################### INSERTION DONNÉES TABLE BULLETIN ################
        col_bulletin="insert into bulletin(notes, type, id_edu, id_mat) values(%s,%s,%s,%s)"
        val_col_bull=[]
  
        big_list=[]
        big_list_Ex=[]
        for z in Note:
            #val_ex=Note[z][0][-1]
            val_ex=z[0][-1]
            #print(id_et[z])
            #val_id_etu=ma_list_et[z]
            #val_id_mat=ma_list_mat[z]
            nom_mmt=z[1].strip()
            
            if nom_mmt[0:3] in 'Français':
                nom_mmt='Français'
                #list_matiere.append(val_nom_mat)
            devrs=z[0][:-1]
            
            for nam in list_id_mat:
                #print(nam)
                if nam[1]==nom_mmt:
                    id_nom_mat=nam[0]   
                    #print(id_nom_mat,nom_mmt, "testing\n")
            
            for k in devrs:
                for etu in list_id_etu:
                    if val_num == etu[1]:
                        id_et = etu[0]
                        #print(id_et)
                
                big_list.append((k,'devoir',id_et,id_nom_mat))
                #print(k,'devoir',id_et,id_nom_mat,val_num)
            #print(big_list)   
            big_list_Ex.append((val_ex,'Examen',id_et,id_nom_mat))
            #print(big_list_Ex)  
        #crayon.executemany(col_bulletin,(big_list_Ex))
        #crayon.executemany(col_bulletin,big_list)
        #ma_connex.commit()
############################### FIN #################################################
        
######################### REMPLISSAGE TABLE MOYENNE_GENERAL #########################       
        
        val_col_note=[]
        moy_gen=l['Moyenne générale']
        col_note="insert into moyenne_general(moyenne) values(%s)"
        val_col_note.append((moy_gen,))
        #crayon.executemany(col_note,val_col_note)
        #ma_connex.commit()
################################ FIN ######################
       
       ############# avoir ###########"
        #crayon.execute("select id_etudiant from etudiant")
        #val_id_etu=[]
        #val_id_not=[]
        #for av in crayon.fetchall():
         #   val_id_etu.append(av)

        #crayon.execute("select id_note from note")
        
        #for g in crayon.fetchall():
         #   val_id_not.append(g)
        #col_avoir1="insert into avoir(id_etudiant) values(%s)"
        #col_avoir2="insert into avoir(id_note) values(%s)"
        #val_col_avoir=[]
        #val_col_avoir.append((val_id_etu,val_id_not))
        
        #crayon.executemany(col,val_col)
        #crayon.executemany(col_note,val_col_note)
        #ma_connex.commit()

    else:
        ecrire_inv.writerow(l)
        n1=n1+1        
        
############################# REMPLISSAGE TABLE MATIÈRE ########################
col_matiere="insert into matiere(nom) values(%s)"
val_col_matiere=[]
for k in list_matiere:
    val_col_matiere.append((k,))
#print(val_col_matiere)
#crayon.executemany(col_matiere,val_col_matiere)
#ma_connex.commit()
############################ brouillon ##########################""""
#col_bulletin="insert into bulletin(notes, type, id_edu, id_mat) values(%s,%s,%s,%s)"
#val_col_bull=[]

    
 

#print(list_id_etu)



#for z in range(len(Note)):
 #   val_ex=Note[z][0][-1]
            #print(z)
            #print(Note[z][0])
            
  #  devs= Note[z][0][:-1]
   # crayon.execute(col_bulletin,(val_ex,2,val_id_etu,val_id_mat))
            
   # for dev in devs:
                #print(dev)
    #    crayon.execute(col_bulletin,(dev,1,val_id_etu,val_id_mat))
###################################################################################
        #print(Note)
#col_avoir1="insert into avoir(id_etudiant) values(%s)"
#col_avoir2="insert into avoir(id_note) values(%s)"
#crayon.execute("insert into avoir(id_etudiant) values(val_id_etu1)")
#crayon.executemany(col_avoir1,val_id_etu1)
#crayon.executemany(col_avoir2,val_id_not1)
#ma_connex.commit()
    



    



taf.close()
valide.close()
invalide.close()


################################## Menu ########################################

def Menu():
    
    def choice():
        """
        la fonction pour choisir l'affichage des données valides 
        ou invalides"""
        import csv
        val=open('fichier_valid.csv','r')
        lectur=csv.DictReader(val)
        inval=open('fichier_invalid.csv','r')
        lectur_inv=csv.DictReader(inval)
   
        c=str(input("Veuiller tapez $ pour les infos valides ou £ pour les infos invalides : "))
        if c=='$':
            for a in lectur:
                print(a)  


         
            
        elif c=='£':
            for b in lectur_inv:
                if not (numero(b["Numero"])==True):
                    raise Exception("le format du numéro est incorrect!",b)
                elif not (prenom(b["Prénom"])==True):
                    raise Exception("le prénom est incorrect",b)
                elif not (nom(b["Prénom"])==True):
                    raise Exception("le nom est incorrect",b)
                elif not (classe(b["Classe"])==True):
                    raise Exception("le format de la classe n'est pas bon",b)
                else:
                    raise Exception("la date n'est pas valide",b)
                print(b)
        
    def InfoNum():
        """
        Cette fonction permet d'afficher les informations par numéro saisi au clavier """
        x=input("Veuillez entrer le numéro: ")
        import csv
        learn=open("fichier_valid.csv","r")
        lire=csv.DictReader(learn)
        for p in lire:
            if x==p["Numero"]:
                print(p)
                break
        
    def cinq():
        """
        la fonction pour afficher les cinqs premiers """
        import csv
        val=open('fichier_valid.csv','r')
        lectur=csv.DictReader(val)
        ordonne=[]
        for l in lectur:
            ordonne.append(l)
        from operator import itemgetter
        ordonne=sorted(ordonne, key=itemgetter('Moyenne générale'), reverse=True)
        print(ordonne[1:6])
    
    while True:
        print("1: Pour afficher les données valides ou invalides")
        print("2: Pour afficher les informations par numéro")
        print("3: Pour afficher les cinqs premiers")
        print("0: Pour quitter")
        x=input("Entrer votre choix: ")
        if x=='1':
            choice()
        elif x=='2':
            InfoNum()
        elif x=='3':
            cinq()
        elif x=='0':
            break
#############################" Remplissage tables #####################################
        
  

#### c'est ici que je vais prendre les data de ma BDmySQL ###
 
 #ma_connex=mysql.connector.connect(host="localhost", user="root", password="secke2022", database="info_etudiant", auth_plugin="mysql_native_password")
 #crayon=ma_connex.cursor()
 #col_matiere="insert into matiere(devoir1, devoir2, exam) values(%s,%s,%s)"
 #val_col_matiere=[]
 #print(Note[0][1])

 #for u in range(len(l['Note'])):
     
  #   val_d1=l['Note'][u][0]
   #  val_d2=l['Note'][u][1]
    # val_d3=l['Note'][u][2]
     #val_ex=l['Note'][u][-1]
     #n_matiere=nom_matiere_sql[u]
    # print(l['Note'][u])
   
    # val_col_matiere.append((val_d1,val_d2,val_ex))

 
 #print(nm_matiere)
 #print(val_col_matiere)
 #crayon.execute("insert into matiere(nom) values(nm_matiere)")
# crayon.executemany(col_matiere,val_col_matiere)
 #ma_connex.commit()




####### ##################### INSERTION DONNÉES TABLE BULLETIN ################

        #print("test troisieme", list_id_etu)  
        #ma_list_et=[]
        #ma_list_mat=[]
        #for etu in list_id_etu:
         #   if val_num == etu[1]:
          #      id_et = etu[0]
           #     ma_list_et.append(id_et)
                #print(id_et)
        #for nam in list_id_mat:
         #   if nam[1]==val_nom_mat:
          #      id_nom_mat=nam[0]
           #     ma_list_mat.append(id_nom_mat)