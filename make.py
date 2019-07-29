import json
import requests
import re
import os
import subprocess
import time


def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels/"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    for i in res_json["tunnels"]:
        if i['name'] == 'command_line':
            return i['public_url']

    return None

def main():
    ngrok = subprocess.Popen(['ngrok', 'http', '5005'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)

    time.sleep(5)

    new_url = get_ngrok_url()
    if(new_url == None):
        return

    file_name = "credentials.yml"
    credentials = open(file_name).read()
    credentials = re.sub(r'https://[^\.]+\.ngrok\.io', new_url, credentials)
    f = open(file_name, 'w')
    f.write(credentials)
    f.close()

    rasa_action = subprocess.Popen(['rasa', 'run', 'actions'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)    

    rasa_server = subprocess.Popen(['rasa', 'run'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)                

    input("Press Enter to finish...")

    rasa_server.kill()
    rasa_action.kill()
    ngrok.kill()


if(__name__ == '__main__'):
    main()