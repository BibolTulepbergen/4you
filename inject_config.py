import os

api_key    = os.environ['FIREBASE_API_KEY']
auth_domain= os.environ['FIREBASE_AUTH_DOMAIN']
project_id = os.environ['FIREBASE_PROJECT_ID']
storage    = os.environ['FIREBASE_STORAGE_BUCKET']
sender_id  = os.environ['FIREBASE_MESSAGING_SENDER_ID']
app_id     = os.environ['FIREBASE_APP_ID']
cloud_name = os.environ['CLOUDINARY_CLOUD_NAME']
upload_preset = os.environ['CLOUDINARY_UPLOAD_PRESET']

config_script = (
    '<script>'
    'window.FIREBASE_CONFIG={'
    'apiKey:"' + api_key + '",'
    'authDomain:"' + auth_domain + '",'
    'projectId:"' + project_id + '",'
    'storageBucket:"' + storage + '",'
    'messagingSenderId:"' + sender_id + '",'
    'appId:"' + app_id + '"'
    '};'
    'window.CLOUDINARY_CONFIG={'
    'cloud_name:"' + cloud_name + '",'
    'upload_preset:"' + upload_preset + '"'
    '};'
    '</script>'
)

for fname in ['constructor.html', 'card.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('</head>', config_script + '</head>', 1)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Injected config into ' + fname)