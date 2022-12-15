#Archivo que se encarga de descargar los archivos cifrados que se obtienen del servicio de almacenamiento "Google drive" asignado,


#Librerias importadas
import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

#Información necesaria para poder lograr la transmisión de archivos con un "Google drive" específico. 
CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

#Función necesaria para poder lograr una conexion con la nube, fue necesario ingresarle las credenciales.
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#driveQuery se encarga de filtrar los tipos de videos que se quiere descargar, el archivo requerido es de tipo ".txt",se filtrara de esa manera.
driveQuery ="(mimeType = 'text/plain')"

fieldsString= 'files(id, mimeType, parents , name)'

response = service.files().list(
    pageSize=1000,
    q=driveQuery,
    fields=fieldsString
).execute()

lstFiles = response['files']

#Token, que funciona como puntero, que se encarga de verificar si existe algun archivo en la siguiente posicion de la lista.
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    #Revisa si los archivos cumple las condiciones a descargar, como por ejemplo, que sea del tipo pedido.
    response = service.files().list(
        pageSize=1000,
        q=driveQuery,
        fields=fieldsString,
        pageToken=nextPageToken
).execute()
lstFiles.extend(response ['files'])
nextPageToken=response.get('nextPageToken')

#Itera por todos los archivos que cumplen las condiciones.
for item in lstFiles:
    if not item['name'].startswith('~$'):
        #Verificación para descargar solo el archivo cifrado.
        if  item['name'].startswith('cifrado1.'):
        
            #Obtiene la ID del archivo.
            request = service.files().get_media(fileId=item['id'])
        
            #Se encarga de la descarga de los archivos
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload (fh,request)

            #Sección que se encarga de mostrar continuamente, en porcentajes, el progreso de descarga de cada uno de los archivos.
            done=False
            while not done:
                status, done=downloader.next_chunk()
                print('Download progress {0: .0%}'.format((status.progress()*1)))
            
            fh.seek(0)
            #Obtiene el nombre del archivo.
            file_name = item['name']

            #PARTE IMPORTANTE 
            #"./Analista/Descarga_Drive" Tiene que ser cambiado por la carpeta en la cual se quieren guardar los archivos descargados, que se mantienen con el mismo nombre.
            with open(os.path.join('./Analista/Descarga_Drive', file_name), 'wb') as f:
                f.write(fh.read())
                f.close()  
           
#Indica que el proceso de descargas terminó.             
print("Finished")            

#https://www.youtube.com/watch?v=SmNTLSkJYfA&list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz&index=13 Video guia para lograr la descarga.