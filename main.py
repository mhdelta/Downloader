from subprocess import check_output
from subprocess import call
import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = 'AIzaSyAtz5apOykU5OoDjjl0XosOXudEOnqoAm0'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def MenuPrincipal():
	print '\n\nMENU PRINCIPAL'
	print 'Ingrese una opcion...'
	print '[1]. Buscar una cancion'
	print '[0]. Salir'

def MenuBuscarCancion():
	print '\n'
	nom_cancion = raw_input('Deme el nombre de la cancion\n')

	BuscarCancion(str(nom_cancion))

def BuscarCancion(nombre):
	print 'Buscando la cancion...'
	search_response = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
			developerKey=DEVELOPER_KEY).search().list(
		q=nombre,
		part='id,snippet',
		maxResults=1
	).execute()
	videos = []
	for search_result in search_response.get('items', []):
		if search_result['id']['kind'] == 'youtube#video':
			videos.append('%s (%s)' % (search_result['snippet']['title'],
										search_result['id']['videoId']))
			song_id = search_result['id']['videoId']								
	#subprocess.check_output(['ls','-l']) #all that is technically needed...
	print call("youtube-dl -x --audio-format mp3 " + ' -o C:\Users\PERSONAL\Desktop\mp6\Musica\%(title)s.%(ext)s ' + song_id, shell=True)
fin = False

while (fin == False):
	MenuPrincipal()
	op = input()
	if op == 0:
		print 'Hasta luego'
		fin = True
	elif op == 1:
		MenuBuscarCancion()
	elif op == 2:
		print 'Chao!'
		




