from os import path, makedirs, sep

DATA_FOLDER_PATH = path.expandvars(r'%LOCALAPPDATA%\ProdApp')
CONFIG_PATH = DATA_FOLDER_PATH + sep + "Config.txt"
CONFIG_FILE = None
CODE = None
IS_ACTIVATED = False


def init():
    global CONFIG_FILE, CODE
    if not path.exists(DATA_FOLDER_PATH):
        makedirs(DATA_FOLDER_PATH)
    with open(CONFIG_PATH, "a") as CONFIG_FILE:
        pass
    CODE = get_code()


def get_code() -> str:
    global CONFIG_FILE, CODE
    with open(CONFIG_PATH, "r+", encoding="utf-8") as CONFIG_FILE:
        raw_data = CONFIG_FILE.read()
    for line in raw_data.split("\n"):
        if "ActivationCode: " in line:
            CODE = line.replace("ActivationCode: ", "")
    print(CODE)
    return CODE


def save_code() -> bool:
    global CONFIG_FILE, CODE
    with open(CONFIG_PATH, "a", encoding="utf-8") as CONFIG_FILE:
        CONFIG_FILE.write(f"ActivationCode: {CODE}\n")
    return True


def reset_code():
    global CONFIG_FILE, CODE, IS_ACTIVATED
    CODE = None
    IS_ACTIVATED = False
    with open(CONFIG_PATH, "w") as CONFIG_FILE:
        pass


def set_code(code):
    global CODE
    CODE = code