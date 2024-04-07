from googleapiclient.discovery import build
from oauth2client.file import Storage
from main import main

# Load credentials and create gmail object
credentials = Storage('credentials.json').get()
service = build('gmail', 'v1', credentials=credentials)

# email subjetcs to filter by


def email_subjects_by_bank():
    return {'zinli': 'Resumen de movimientos del mes de',
            'fiwind': 'Reporte de actividad',
            'mp': 'Ya podés conciliar todas tus transacciones',
            'brubank': 'tu estado de cuenta ya se encuentra disponible',
            'littio': '¡Tus extractos Littio están listos!'}


def get_message_id():
    subjects = [v for k, v in email_subjects_by_bank().items() if k in main()]
    for s in subjects:
        messages = service.users().messages().list(
            userId='me', q=f'subject:{s}').execute()


# Obtén el ID del mensaje
message_id = messages['messages'][0]['id']
