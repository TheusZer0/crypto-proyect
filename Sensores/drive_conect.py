#Archivo que se encarga de,tanto conectar como subir archivos a la carpeta asignada, dentro del servicio de almacenamiento "Google drive".

#Importaciones necesarias para lograr la conexión con "Google drive".
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

#Información necesaria para poder lograr la transmisión de archivos con un "Google drive" específico, gracias a las credenciales obtenidas en "client_secrets.json". 
CLIENT_SECRET_FILE = 'Sensores/client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

#Función necesaria para poder lograr una conexión con la nube, fue necesario ingresarle las credenciales específicas.
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


#Se le entrega la ID específica de la carpeta con la cual trabajar.
folder_id = '1gg3ZsIix1xO2rwG1OVYkNHRrC_SA3x_C'
#Nombre del archivo el cual se subirá.
file_name = 'cifrado1.encode'
#Se especifica de que tipo es el video indicado.
mime_type = 'text/plain'

file_metadata = {
    'name': file_name,
    'parents': [folder_id],
}
#Revisa la carpeta "Sensores" y verifica si existe algún archivo que cumple el nombre y el tipo especificado, de ser así, es subido a la plataforma.
#Al momento de querer correr esta sección, hay que cambiar "'../crypto-project-main/Sensores/'" por el nombre de la carpeta en la cual se trabajará.
media = MediaFileUpload('../crypto-project-main/Sensores/{0}'.format(file_name), mimetype=mime_type)

service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
    ).execute()

print("Finished")

#https://www.youtube.com/watch?v=kFR-O8BHIH4&list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz&index=9 video en el cual se basó para lograr conexion con google drive