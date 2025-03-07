
from voice_recognition import listen, speak
from command_processor import process_command
from domotica import accendi_luce
from app_management import apri_browser
from github_automation import crea_repository

def main():
    speak("Ciao, come posso aiutarti?")
    while True:
        command = listen()
        if command:
            module, action = process_command(command)
            if module == "domotica" and action == "accendi_luce":
                accendi_luce()
                speak("Luce accesa")
            elif module == "app" and action == "apri_browser":
                apri_browser()
                speak("Browser aperto")
            elif module == "github" and action == "crea_repository":
                url = crea_repository("nuovo_repo")
                speak(f"Repository creato: {url}")
            else:
                speak("Comando non riconosciuto")

if __name__ == "__main__":
    main()
