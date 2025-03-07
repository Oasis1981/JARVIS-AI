
def process_command(command):
    if "accendi la luce" in command:
        return "domotica", "accendi_luce"
    elif "apri browser" in command:
        return "app", "apri_browser"
    elif "crea repository" in command:
        return "github", "crea_repository"
    else:
        return None, None
