from telegram.ext import Updater, CommandHandler, MessageHandler, Filters                                                                                                                      
TOKEN='1083753366:AAGiGStMb_eehD5KTRp4hc-gdB9FmTb3g6Y'                                                                                                                                         
archivo=open("database.txt","r") #archivo base de datos                                                                                                                                        
megalista=[]



def start(bot, update):
  update.message.reply_text("Bienvenido al nuevo RamoBOT\n Aqui encontraras informacion sobre tus clases online. Este es un bot en desarrollo, por lo que cualquier error, o sugerencia por favor contactarme a https://t.me/Urra_Aldunate . El codigo sera publicado en unos dias. escribe '\start' para ver este mensaje denuevo, escribe 'comandos' para ver comandos")


def entregar_datos_en_lista(archivo):
    j=[]
    r=[]
    for linea in archivo:
        linea=linea.split()
        t=[]
        for j in linea:   ##j es un elemento de la lista linea
            j=j.replace("_"," ")
            t.append(j)
        r.append(t)
    archivo.close()
    return(r)
    
megalista=entregar_datos_en_lista(archivo)
#print(megalista)


def encontrar(megalista,clave):
    resultados=[]
    for j in megalista: #j es una lista que incluye datos de un curso
        for k in j:    #k es un elemento de dicha lista
            temporal=[]
            if clave in k:
                temporal.append(j)
            resultados.append(temporal)
    resultados2=[]
    for a in resultados: #a es una lista que incluye datos de un curso
        if len(a)>0:
           resultados2.append(a[0])    
    return(resultados2)
  
  
#==============================================================================================
def program(bot, update):
    k=update.message.text.lower()
    k=k.split()
    if (k[0]=="ayuda" or k[0]=="help") :
        update.message.reply_text("Bienvenido al nuevo RamoBOT\n Aqui encontraras informacion sobre tus clases online. Este es un bot en desarrollo, por lo que cualquier error, o sugerencia por favor contactarme a https://t.me/Urra_Aldunate .El codigo sera publicado pronto. Para ver los comandos escribe **comandos**")
      
    if (k[0]=="comandos"):
       update.message.reply_text("'comandos' muestra este menu.\n 'help' muestra el menu de bienvenida.\n 'zoom' para mostrar informacion sobre un ramo.\n 'zoom agregar' para agregar informacion sobre un ramo (en desarrollo) ")
       return 0

    if (k[1]=="agregar"):
       update.message.reply_text("Para agregar info de un ramo, en un mensaje agregar la siguiente informacion:\n sigla nombre_apellido dia-hora ZoomID password")
       return 0

    if (k[0]=="zoom"):
       if len(k[1])<4:
          update.message.reply_text("Por favor ingresar un argumento con mas de 3 caracteres, para buscar un ramo debes ingresar:\n 'zoom dato'\n cambiando dato por la sigla del ramo, o el apellido del profesor, o el ID de zoom.\n Como ejemplo puedes ingresar el comando 'zoom ipm263' ")
          return 0
 
    if (k[0]=="zoom"):
        if encontrar(megalista,k[1])==[]:
           update.message.reply_text("No se han encontrado resultados, puedes agregar info del ramo con el comando 'zoom agregar'")
           return 0
      

    if (k[0]=="zoom"):
       for j in encontrar(megalista,k[1]):
           r1=str("Sigla: "+str(j[0]))
           r2=str("Nombre del ramo: "+str(j[5]))
           r3=str("Docente: "+str(j[1]))
           r4=str("Horarios: "+str(j[2]))
           r5=str("Zoom ID: "+str(j[3]))
           r6=str("Clave: "+str(j[4]))
           
           rt=r1+"\n"+r2+"\n"+r3+"\n"+r4+"\n"+r5+"\n"+r6
           
           update.message.reply_text(rt) 
           '''
           update.message.reply_text(r2) 
           update.message.reply_text(r3) 
           update.message.reply_text(r4) 
           update.message.reply_text(r5)
           update.message.reply_text(r6) 
           '''
#==============================================================================================
    
def entregar_datos(archivo,clave): ##Retorna una lista (de listas) que incluye informacion del(los) ramo(s) coincidentes.
    j=[]
    r=[]
    for linea in archivo:
        if clave in linea:
           linea=linea.split()
           t=[]
           for j in linea:   ##j es un elemento de la lista linea
               j=j.replace("_"," ")
               t.append(j)
           r.append(t)
    return(r)
  
def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(TOKEN)
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  upper_case = MessageHandler(Filters.text, program)
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(upper_case)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()
