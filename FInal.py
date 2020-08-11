# -*- coding: utf-8 -*-

#Ramon Antonio Melo Olivero
#2019-7588
from urllib.request import urlopen
from pathlib import Path
import json,datetime
from datetime import date
from playsound import playsound
import os,sys
from os import system
import webbrowser as wb
import matplotlib.pyplot as plt
import telebot
casos=[]
info=[]
_not_repeat=1


def Main():
    global casos
    global info
    global _not_repeat
    info.clear()
    ubicacion=Path("Datos.txt")
    if ubicacion.exists():
          if os.stat("Datos.txt").st_size == 0:
             print("Favor Borrar El Documento llamado Datos.txt...")
             mover()
    if ubicacion.exists():
     archivo2=open("Datos.txt",'r')
     datos4=archivo2.read()
     archivo2.close()
     casos=json.loads(datos4)
    os.system("cls")
    print("Programa que Registra Casos de Corona Virus..")
    if (_not_repeat==1):
        playsound("audios/Saludos.mp3")
        _not_repeat+=1
    print("Agregar Casos:1")
    print("Editar Casos:2")
    print("Borrar Caso:3")
    print("Ver Casos Guardados:4")
    print("Exportar:5")
    print("Salir:6")
    playsound("audios/OpcVal.mp3")
    opcion=input("Ingrese una opcion: ")
    if (opcion=="1"):
        agregar()
    elif (opcion=="2"):
        editar()
    elif (opcion=="3"):
        borrar()
    elif (opcion=="4"):
        ver()
    elif (opcion=="5"):
        exportar()
    elif (opcion=="6"):
        playsound("audios/Hasta.mp3")
        print("Adios")
        sys.exit()
    else:
        playsound("audios/OpcVal.mp3")
        input("Opcion Incorrecta pulse enter para continuar")
        Main()


def agregar():
    global info
    global casos
    os.system("cls")
    info.clear()
    print("Datos del Caso")
    playsound("audios/Datos.mp3")
    cedula=(input("Digite una cedula Dominicana: "))
    link="http://173.249.49.169:88/api/test/consulta/"+cedula
    datos= urlopen(link)
    info2= json.loads(datos.read())  
    if("Cedula" in info2):
        print("Cedula Valida..")
        info.append(cedula)
        info.append(input("Nombre(s): "))
        info.append(input("Apellido(s): "))
        info.append(input("Sigla del Sexo (M) (F) o (O): "))
        info.append(input("Fecha de Registro: "))
        info.append(input("Nacionalidad: "))
        info.append(input("Estado del Caso(Enfermo-Recuperado-Fallecido): "))
        info.append(input("Telefono: "))
        info.append(input("Correo: "))
        info.append(input("Provincia de Caso: "))
        q=open("Ubc/provincias.txt",'r')
        a=q.read()
        q.close()
        comprobar=json.loads(a)
        if (info[9] in comprobar) == False:
            playsound("audios/Error.mp3")
            print("Error provincia invalida..")
            mover()
        info.append(input("Latitud: "))
        info.append(input("Longitud: "))
        print("Caso Registrado")
        casos.append(info)
        datos1=json.dumps(casos)
        archivo=open("Datos.txt","w")
        archivo.write(datos1)
        archivo.close()
        num1=0
        for info in casos:
            num1=num1+1
        TOKEN = '1146105232:AAG5gAvvawWJTReztJlbeC2JLvbjAHcpurY' # Ponemos nuestro Token generado con el @BotFather
        tb = telebot.TeleBot(TOKEN) 
        tb.send_message('-1001376560541', 'ALERTA!'+'\n'+'Se ha Registrado un nuevo Caso de COVD-19'+'\n'+"Hasta el momento hay "+str(num1)+" Casos Registrado...")
        print("Arlerta Enviada")
        wb.open_new("https://t.me/s/proyectofinal2020")
        playsound("audios/CasoGuardado.mp3")
        mover()
    else:
        print("Cedula Invalida...")
        playsound("audios/OpcVal.mp3")
        elc=int(input("Si quiere volver al a intentarlo 1 si desea Volver al Menu del programa 2: "))
        if elc==1:
            agregar()
        elif elc==2:
            Main()
        else:
            playsound("audios/Error.mp3")
            print("Numero incorrecto")
            mover()
        mover()
def editar():
        os.system("cls")
        global info
        global casos
        ubicacion=Path("Datos.txt")
        if ubicacion.exists():
              if os.stat("Datos.txt").st_size == 0:
                 print("Favor Borrar El Documento llamado Datos.txt...")
                 mover()
        if ubicacion.exists():
         archivo2=open("Datos.txt",'r')
         datos4=archivo2.read()
         archivo2.close()
         casos=json.loads(datos4)
        else:
            print("No hay Datos para editar..")
            playsound("audios/Noed.mp3")
            mover()
        datos1=[]
        conteo=1
        os.system("cls")
        if os.stat("Datos.txt").st_size == 2:
            print("No Hay Datos Para Editar...")
            playsound("audios/Noed.mp3")
            mover()
        for info in casos:
                print("Caso#"+str(conteo))
                print("Nombre: "+info[1]+"\n"+"Apellidos: "+info[2]+"\n"+"Fecha: "+info[4]+"\n"+
"Estado: "+info[6]+ "\n"+"Provincia: "+info[9]+"\n")
                conteo=conteo+1
        conteo2=conteo-1
        playsound("audios/CasE.mp3")
        opcion=int(input("Cual Caso quiere Editar? "))
        opcion4=opcion-1
        prueba=[]
        if opcion>0 and opcion<=conteo2:
            opcion2=int(input("Si Desea Editar Ingrese #1  Si no lo quiere Editar #2: "))
            if opcion2==1:
                os.system("cls")
                print("Datos del Casos")
                playsound("audios/Datos.mp3")
                cedula=(input("Digite una cedula Dominicana: "))
                link="http://173.249.49.169:88/api/test/consulta/"+cedula
                datos= urlopen(link)
                info2= json.loads(datos.read())
                if("Cedula" in info2):
                    prueba.append(cedula)
                    prueba.append(input("Nombre(s): "))
                    prueba.append(input("Apellido(s): "))
                    prueba.append(input("Sigla del Sexo (M) (F) o (O): "))
                    prueba.append(input("Fecha de Registro: "))
                    prueba.append(input("Nacionalidad: "))
                    prueba.append(input("Estado del Caso(Enfermo-Recuperado-Fallecido): "))
                    prueba.append(input("Telefono: "))
                    prueba.append(input("Correo: "))
                    prueba.append(input("Provincia de Caso: "))
                    q=open("Ubc/provincias.txt",'r')
                    a=q.read()
                    q.close()
                    comprobar=json.loads(a)
                    if (prueba[9] in comprobar) == False:
                        playsound("audios/Error.mp3")
                        print("Error provincia invalida..")
                        mover()
                    prueba.append(input("Latitud: "))
                    prueba.append(input("Longitud: "))
                    playsound("audios/CasoEd.mp3")
                    print("Caso Editado")
                    info=prueba
                    casos[opcion4]=info
                    datos1=json.dumps(casos)
                    archivo=open("Datos.txt","w")
                    archivo.write(datos1)
                    archivo.close()
                    mover()
                else:
                    playsound("audios/OpcVal.mp3")
                    print("Cedula Invalida...")
                    elc=int(input("Si quiere volver al a intentarlo 1 si desea Volver al Menu del programa 2: "))
                    if elc==1:
                        agregar()
                    elif elc==2:
                        Main()
                    else:
                        playsound("audios/OpcVal.mp3")
                        print("Numero incorrecto")
                        mover()
            else:
                mover()
        else:
            playsound("audios/Error.mp3")
            input("Error pulse Enter para Continuar...")
            mover()
def borrar():
        datos=[]
        global info
        global casos
        conteo=1
        os.system("cls")
        ubicacion=Path("Datos.txt")
        if not os.path.exists(ubicacion):
            playsound("audios/Nobo.mp3")
            print("No hay Datos para borrar..")
            mover()
        if os.stat("Datos.txt").st_size == 2:
            playsound("audios/Nobo.mp3")
            print("No Hay Datos Para Borrar...")
            mover()
        for info in casos:
                print("Caso#"+str(conteo))
                print("Nombre: "+info[1]+"\n"+"Apellidos: "+info[2]+"\n"+"Fecha: "+info[4]+"\n"+
"Estado: "+info[6]+ "\n"+"Provincia: "+info[9]+"\n")
                conteo=conteo+1
        conteo2=conteo-1
        playsound("audios/CasB.mp3")
        opcion=int(input("Cual Caso quiere borrar? "))
        if opcion>0 and opcion<=conteo2:
            opcion2=int(input("Si Desea Borrarlo Ingrese #1  Si no lo quiere borrar #2: "))
            if opcion2==1:
               opcion3=opcion-1
               datos=[]
               archivo2=open("Datos.txt",'r')
               datos=archivo2.read()
               casos=json.loads(datos)
               del casos[opcion3]
               archivo2.close()
               datos1=json.dumps(casos)
               archivo=open("Datos.txt","w")
               archivo.write(datos1)
               archivo.close()
               playsound("audios/CasoBorrado.mp3")
               print("Caso Borrado..")
               mover()
            else:
                mover()
        else:
            playsound("audios/OpcVal.mp3")
            input("Error pulse Enter para Continuar...")
            mover()
def ver():
        global info
        global casos
        conteo=1
        a=[]
        os.system("cls")
        ubicacion=Path("Datos.txt")
        if not os.path.exists(ubicacion):
            print("No hay Datos para Ver..")
            playsound("audios/Nover.mp3")
            mover()
        if os.stat("Datos.txt").st_size == 2:
            print("No Hay Datos Para Ver...")
            playsound("audios/Nover.mp3")
            mover()
        for info in casos:
                print("Caso#"+str(conteo))
                print("Cedula: "+info[0]+"\n"+"Nombre: "+info[1]+"\n"+"Apellidos: "+info[2]+"\n"+"Sexo: "+info[3]+"\n"+"Fecha: "+info[4]+"\n"+
"Nacionalidad: "+info[5]+"\n"+"Estado: "+info[6]+ "\n"+"Telefono: "+info[7]+"\n"+"Correo: "+info[8]+"\n"+"Provincia: "+info[9]+"\n"
                "Latitud: "+info[10]+"\n"+"Longitud: "+"\n")
                conteo=conteo+1
        print("Si desea ver los Casos en Mapa Ingrese#1\n"+"Si desea Ver las Estadistica Mistica Ingrese#2 \n"+"Volver al Menu Ingrese#3")
        playsound("audios/OpcVal.mp3")
        opcion=input("Ingrese una Opcion: ")
        if opcion=="1":
            ubicacion=Path("Mapa/Mapa.html")
            if ubicacion.exists():
                arch=open("Mapa/Mapa.html",'r')
                cont=arch.read()
                arch.close()
            for info in casos:
                if info[6]=="Recuperado":
                    tmp="""L.marker(["""+info[10]+""","""+info[11]+"""]).addTo(map).bindPopup('Nombre: """+info[1]+""".<br>Fecha: """+info[4]+ """.<br>Estado: """+info[6]+""".').openPopup();
                    L.circle(["""+info[10]+""","""+info[11]+"""],{color:'green',fillColor:'#3cff00',fillOpacity:0.5,radius:500}).addTo(map);"""
                    a.append(tmp)
                elif info[6]=="Fallecido":
                    tmp="""L.marker(["""+info[10]+""","""+info[11]+"""]).addTo(map).bindPopup('Nombre: """+info[1]+""".<br>Fecha: """+info[4]+ """.<br>Estado: """+info[6]+""".').openPopup();
                    L.circle(["""+info[10]+""","""+info[11]+"""],{color:'black',fillColor:'#00',fillOpacity:0.5,radius:500}).addTo(map);"""
                    a.append(tmp)
                else:
                    tmp="""L.marker(["""+info[10]+""","""+info[11]+"""]).addTo(map).bindPopup('Nombre: """+info[1]+""".<br>Fecha: """+info[4]+ """.<br>Estado: """+info[6]+""".').openPopup();
                    L.circle(["""+info[10]+""","""+info[11]+"""],{color:'red',fillColor:'#f03',fillOpacity:0.5,radius:500}).addTo(map);"""
                    a.append(tmp)
            sep=' '
            tmp =sep.join(a)  
            cont=cont.replace("{asd}",tmp)
            arch=open("Mapa/Mapa2.html",'w')
            arch.write(cont)
            arch.close()
            abrir2="/Mapa/Mapa2.html"
            f=os.getcwd()
            d=f+abrir2
            wb.open_new(d)
            playsound("audios/CasoEX.mp3")
            print("Datos Exportado abra el Mapa2.html")
            mover()
        elif opcion=="2":
            lista=["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","libra","Escorpion","Sagitario"]
            valores=[0,0,0,0,0,0,0,0,0,0,0,0]
            cap=0
            ac=0
            pis=0
            Ari=0
            Tau=0
            Gem=0
            Can=0
            Leo=0
            vrg=0
            lb=0
            sc=0
            saj=0
            conteo=1
            for info in casos:
                link="http://173.249.49.169:88/api/test/consulta/"+info[0]
                datos= urlopen(link)
                info2= json.loads(datos.read())
                fecha=info2["FechaNacimiento"]
                tiempo= datetime.datetime.strptime(fecha,'%Y-%m-%d %H:%M:%S.%f')
                newfecha=tiempo.date()
                print("Fecha de Nacimiento del caso #"+str(conteo)+"\n"+str(newfecha))
                dia=tiempo.day
                mes=tiempo.month
                conteo=conteo+1
                if(mes==12 and dia>=22or mes==1 and dia<=19):
                    cap=cap+1
                    valores[0]=(cap)                
                elif(mes==1 and dia>=20or mes==2 and dia<=18):
                    ac=ac+1
                    valores[1]=(ac)  
                elif(mes==2 and dia>=19or mes==3 and dia<=20):
                    pis=pis+1
                    valores[2]=(pis)  
                elif(mes==3 and dia>=21or mes==4 and dia<=19):
                    Ari=Ari+1
                    valores[3]=(Ari)  
                elif(mes==4 and dia>=20or mes==5 and dia<=20):
                    Tau=Tau+1
                    valores[4]=(Tau)  
                elif(mes==5 and dia>=21or mes==6 and dia<=20):
                    Gem=Gem+1
                    valores[5]=(Gem)  
                elif(mes==6 and dia>=21or mes==7 and dia<=22):
                    Can=Can+1
                    valores[6]=(Can)  
                elif(mes==7 and dia>=23or mes==8 and dia<=22):
                    Leo=Leo+1
                    valores[7]=(Leo)  
                elif(mes==8 and dia>=23or mes==9 and dia<=22):
                    vrg=vrg+1
                    valores[8]=(vrg)  
                elif(mes==9 and dia>=23or mes==10 and dia<=22):
                    lb=lb+1
                    valores[9]=(lb)  
                elif(mes==10 and dia>=23or mes==11 and dia<=21):
                    sc=sc+1
                    valores[10]=(sc)  
                elif(mes==11 and dia>=22or mes==12 and dia<=21):
                    saj=saj+1
                    valores[11]=(saj)
            print("Cierre la Ventana de las grafica para continuar...")
            playsound("audios/Expanda.mp3")
            plt.plot(lista,valores,"ro")
            plt.title("Grafica de Casos de COVID-19 por Signo Zodical")
            plt.show()
            mover()        
        elif opcion=="3":
            Main()
        else:
            playsound("audios/Error.mp3")
            print("Opcion Incorrecta..")
            mover()
       
def exportar():
    global info
    global casos
    conteo=1
    os.system("cls")
    ubicacion=Path("Datos.txt")
    if not os.path.exists(ubicacion):
        print("No hay Datos para Ver..")
        playsound("audios/Noex.mp3")
        mover()
    if os.stat("Datos.txt").st_size == 2:
        playsound("audios/Noex.mp3")
        print("No Hay Datos Para Ver...")
        mover()
    for info in casos:
        print("Caso#"+str(conteo))
        print("Cedula: "+info[0]+"\n"+"Nombre: "+info[1]+"\n"+"Apellidos: "+info[2]+"\n"+"Sexo: "+info[3]+"\n"+"Fecha: "+info[4]+"\n"+
"Nacionalidad: "+info[5]+"\n"+"Estado: "+info[6]+ "\n"+"Telefono: "+info[7]+"\n"+"Correo: "+info[8]+"\n"+"Provincia: "+info[9]+"\n"
        "Latitud: "+info[10]+"\n"+"Longitud: "+"\n")
        conteo=conteo+1
    conteo2=conteo-1
    print("Si desea Exportar Un caso Ingrese#1\n"+"Si desea Exportar todos los casos Ingrese#2 \n"+"Volver al Menu Ingrese#3")
    playsound("audios/OpcVal.mp3")
    opcion=input("Ingrese una Opcion: ")
    if opcion=="1":
        playsound("audios/CasEx.mp3")
        elc=int(input("Numero del caso que desea Exportar: "))
        if elc>0 and elc<=conteo2:
            exp=elc-1
            datos=casos[exp]
            c=datos
            link="http://173.249.49.169:88/api/test/consulta/"+c[0]
            datoss= urlopen(link)
            info2= json.loads(datoss.read())
            Nom=info2["Nombres"]
            Apll1=info2["Apellido1"]
            Apll2=info2["Apellido2"]
            lugar=info2["LugarNacimiento"]
            fecha=info2["FechaNacimiento"]
            tiempo= datetime.datetime.strptime(fecha,'%Y-%m-%d %H:%M:%S.%f')
            newfecha=tiempo.date()
            foto='http://173.249.49.169:88/api/test/foto/'+c[0]
            d=date.today()
            a=newfecha.year
            if date.month==newfecha.month and d.day>newfecha.day:
                edad=d.year-a
            else:
                edad=d.year-a-1
            if c[6]=="Enfermo":
                color="red"
            elif c[6]=="Recuperado":
                color="green"
            else:
                color="black"

            asd="""
<html>
        <title>  Caso en Especifico </title>
        <body>
        <body background=https://image.freepik.com/foto-gratis/fondo-gris-pintado_53876-94041.jpg >
            <center>
            <h1><font color="""+str(color)+""">Caso#"""+str(elc)+"""</font></h1>
            <h1>Datos de la Persona</h1>
            <img src="""+foto+""" width="250" height="250"/>
           <br>
            <h2>Nombres:</h2>
            <h3>"""+str(Nom)+"""</h3>
            <h2>apellidos:</h2>
           <h3>"""+str(Apll1)+""" """+str(Apll2)+"""</h3>
            <h2>Fecha de Nacimiento :</h2>
            <h3>"""+str(newfecha)+"""</h3>
            <h2>Lugar de Nacimiento:</h2>
            <h3>"""+str(lugar)+"""</h3>
            <h2>Estado:</h2>
            <h1><font color="""+str(color)+""">"""+str(c[6])+"""</font></h1>
            <h1>"""+str(edad)+""" Años</h1>
            </center>

        </body>

</html>"""
            archivo=open("Datos Exportados/"+c[0]+".html","w")
            archivo.write(asd)
            archivo.close()
            abrir=("\Datos Exportados")
            abrir2=abrir+"/"+c[0]+".html"
            f=os.getcwd()
            d=f+abrir2
            wb.open_new(d)
            playsound("audios/CasoEX.mp3")        
            print("Datos Exportados")
            mover()           
        else:
            playsound("audios/OpcVal.mp3")
            input("Error pulse Enter para Continuar...")
            mover()
    elif opcion=="2":
        conteo=1
        for info in casos:
            link="http://173.249.49.169:88/api/test/consulta/"+info[0]
            datoss= urlopen(link)
            info2= json.loads(datoss.read())
            Nom=info2["Nombres"]
            Apll1=info2["Apellido1"]
            Apll2=info2["Apellido2"]
            lugar=info2["LugarNacimiento"]
            fecha=info2["FechaNacimiento"]
            tiempo= datetime.datetime.strptime(fecha,'%Y-%m-%d %H:%M:%S.%f')
            newfecha=tiempo.date()
            foto='http://173.249.49.169:88/api/test/foto/'+info[0]
            d=date.today()
            a=newfecha.year
            if date.month==newfecha.month and d.day>newfecha.day:
                edad=d.year-a
            else:
                edad=d.year-a-1
            if info[6]=="Enfermo":
                color="red"
            elif info[6]=="Recuperado":
                color="green"
            else:
                color="black"
            asd=f"""
<html>
            
        <title>  Caso#{conteo} </title>
        <body>
        <body background=https://image.freepik.com/foto-gratis/fondo-gris-pintado_53876-94041.jpg >
            <center>
            <h1><font color={color}>Caso#{conteo}</font></h1>
            <h1>Datos de la Persona</h1>
            <img src={foto} width="250" height="250"/>
           <br>
            <h2>Nombres:</h2>
            <h3>{Nom}</h3>
            <h2>apellidos:</h2>
           <h3>{Apll1}{Apll2}</h3>
            <h2>Fecha de Nacimiento :</h2>
            <h3>{newfecha}</h3>
            <h2>Lugar de Nacimiento:</h2>
            <h3>{lugar}</h3>
            <h2>Estado:</h2>
            <h1><font color={color}>{info[6]}</font></h1>
            <h1>{edad}Años</h1>
            </center>

        </body>

</html>     """
            archivo=open("Datos Exportados/Caso#"+str(conteo)+".html","w")
            archivo.write(asd)
            archivo.close()
            abrir=("\Datos Exportados")
            abrir2=abrir+"/Caso#"+str(conteo)+".html"
            f=os.getcwd()
            d=f+abrir2
            wb.open_new(d)
            conteo=conteo+1
        playsound("audios/CasoEx.mp3") 
        print("Datos Exportados")
        mover()
    elif opcion=="3":
        Main()
    else:
        playsound("audios/Error.mp3")
        print("Error")
        mover()
def mover():
    playsound("audios/OpcVal.mp3")
    elc=int(input("Si quiere volver al menu ingrese 1 si desea salir del programa 2: "))
    if elc==1:
        Main()
    elif elc==2:
        playsound("audios/Hasta.mp3")
        print("Bye...")
        sys.exit()
    else:
        playsound("audios/Error.mp3")
        print("Numero incorrecto")
        mover()
Main()
