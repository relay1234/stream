# ======================================================
# SECURE MPV STREAM PLAYER
# terminal interface + encrypted catalog
# Categories + Search + Dead stream detection
# ======================================================

import subprocess
import sys
import msvcrt
import json
import requests
import os
import time
from cryptography.fernet import Fernet

# ============================
# CONFIG
# ============================
CATALOG_FILE = "catalog.enc"
KEY_FILE = "key.key"
ADAPTIVE_QUALITY = True
AUTHOR = "TuNombre"
VERSION = "1.0"

index = 0
items = []
filtered_items = []
categories = []
username = ""

# ============================
# TERMINAL HELPERS
# ============================

def clear():
    subprocess.call("cls", shell=True)


def wait_key():
    return msvcrt.getch()


def set_colors():
    os.system("color 0B")

# ============================
# USER LOGIN
# ============================

def ask_username():

    global username

    clear()

    print("=====================================")
    print("      SECURE STREAM TERMINAL")
    print("=====================================\n")

    username = input("Ingresa tu nombre de usuario: ")

# ============================
# HACKER WELCOME SCREEN
# ============================

def splash():

    clear()

    print(r"""
 ███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗
 ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║
 ███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║
 ╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║
 ███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║
 ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
""")

    print(f"\nBienvenido {username} 🚀\n")

    print("Inicializando entorno seguro...")

    time.sleep(1)

# ============================
# LOADING ANIMATION
# ============================

def loading_sequence():

    steps = [
        f"Autenticando usuario {username}",
        "Inicializando motor de streaming",
        "Cargando modulo AES",
        "Descifrando catalogo",
        "Preparando interfaz"
    ]

    clear()

    for s in steps:

        print(s + " ...")
        time.sleep(0.7)

    time.sleep(0.5)

    rocket_animation()

# ============================
# ROCKET ASCII
# ============================

def rocket_animation():

    clear()

    print(f"\nLanzando sistema para {username}\n")

    rocket = [
"        ^",
"       /^\\",
"       |- |",
"       |  |",
"       |  |",
"      /|  |\\",
"     /_|__|_\\",
"       /::\\",
"      /::::\\",
"       ||||",
"       ||||",
"      /_||_\\"
    ]

    for line in rocket:

        print(line)
        time.sleep(0.15)

    print(f"\nSistema listo. Bienvenido {username}.\n")

    time.sleep(1.5)

# ============================
# CRYPTO
# ============================

def load_key():

    with open(KEY_FILE,"rb") as f:
        return f.read()


def decrypt_catalog():

    key = load_key()

    f = Fernet(key)

    with open(CATALOG_FILE,"rb") as c:
        data = c.read()

    dec = f.decrypt(data)

    return json.loads(dec.decode())

# ============================
# STREAM CHECK
# ============================

def stream_alive(url):

    try:

        r = requests.head(url,timeout=5)

        return r.status_code < 400

    except:

        return False

# ============================
# PLAYER
# ============================

def play(url):

    if not stream_alive(url):

        print("\n⚠ Stream caido")
        input("ENTER para volver")

        return

    cmd = [
        "mpv",
        "--cache=yes",
        "--cache-secs=30",
        "--demuxer-max-bytes=100M",
        "--demuxer-readahead-secs=30",
        "--profile=low-latency",
        "--hls-bitrate=0",
        url
    ]

    subprocess.call(cmd)

# ============================
# SEARCH
# ============================

def search_menu():

    global filtered_items

    clear()

    print("===== BUSCAR =====\n")

    q = input("Titulo: ").lower()

    filtered_items = [x for x in items if q in x["title"].lower()]

    movie_menu()

# ============================
# MOVIE MENU
# ============================

def movie_menu():

    global index

    while True:

        clear()

        print(f"=========== CATALOGO ({username}) ===========\n")

        print("↑ ↓ navegar | ENTER reproducir")
        print("B buscar | C categorias | M menu | Q salir\n")

        if not filtered_items:

            print("No hay resultados\n")

        for i,m in enumerate(filtered_items):

            prefix = ">" if i==index else " "

            print(f"{prefix} {m['title']}")

        key = wait_key()

        if key == b"q":
            sys.exit()

        if key == b"m":
            return

        if key == b"b":
            search_menu()

        if key == b"c":
            category_menu()

        if key == b"\r" and filtered_items:
            play(filtered_items[index]["url"])

        if key == b"\xe0":

            k = wait_key()

            if k == b"H":
                index = (index-1) % len(filtered_items)

            if k == b"P":
                index = (index+1) % len(filtered_items)

# ============================
# CATEGORY MENU
# ============================

def category_menu():

    pos = 0

    while True:

        clear()

        print("=========== CATEGORIAS ===========\n")

        for i,c in enumerate(categories):

            prefix = ">" if i==pos else " "

            print(f"{prefix} {c}")

        print("\nENTER seleccionar | M volver")

        key = wait_key()

        if key == b"m":
            return

        if key == b"\r":

            select_category(categories[pos])
            return

        if key == b"\xe0":

            k = wait_key()

            if k == b"H":
                pos = (pos-1) % len(categories)

            if k == b"P":
                pos = (pos+1) % len(categories)

# ============================
# FILTER CATEGORY
# ============================

def select_category(cat):

    global filtered_items

    filtered_items = [x for x in items if x["category"]==cat]

# ============================
# MAIN MENU
# ============================

def main_menu():

    options = [
        "Ver catalogo",
        "Buscar",
        "Categorias",
        "Salir"
    ]

    pos = 0

    while True:

        clear()

        print(f"=========== MENU PRINCIPAL ({username}) ===========\n")

        for i,o in enumerate(options):

            prefix = ">" if i==pos else " "

            print(f"{prefix} {o}")

        key = wait_key()

        if key == b"\r":

            if pos == 0:
                movie_menu()

            if pos == 1:
                search_menu()

            if pos == 2:
                category_menu()

            if pos == 3:
                sys.exit()

        if key == b"\xe0":

            k = wait_key()

            if k == b"H":
                pos = (pos-1) % len(options)

            if k == b"P":
                pos = (pos+1) % len(options)

# ============================
# INIT
# ============================

set_colors()

ask_username()

splash()

loading_sequence()

items = decrypt_catalog()

filtered_items = items

categories = sorted(list(set([x["category"] for x in items])))

main_menu()
