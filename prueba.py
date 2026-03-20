# ======================================================
# SECURE MPV STREAM PLAYER
# Cross-platform (Windows + Termux Android)
# Windows -> mpv
# Termux -> Android Player (com.example.hlplayer)
# ======================================================

import subprocess
import sys
import json
import requests
import os
import time
from cryptography.fernet import Fernet

# ============================
# PLATFORM SELECTOR
# ============================

PLATFORM = None

def select_platform():

    global PLATFORM

    print("=================================")
    print("   SELECCIONA TU TERMINAL")
    print("=================================\n")

    print("1) Windows CMD")
    print("2) Termux / Android\n")

    opt = input("Seleccion: ")

    if opt == "1":
        PLATFORM = "windows"
    else:
        PLATFORM = "termux"


# ============================
# KEYBOARD INPUT
# ============================

def wait_key():

    if PLATFORM == "windows":

        import msvcrt
        return msvcrt.getch()

    else:

        import tty
        import termios

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)

        try:

            tty.setraw(fd)
            ch = sys.stdin.read(1)

            if ch == "\x1b":
                ch += sys.stdin.read(2)

            return ch.encode()

        finally:

            termios.tcsetattr(fd, termios.TCSADRAIN, old)


# ============================
# CONFIG
# ============================

CATALOG_FILE = "catalog.enc"
KEY_FILE = "key.key"

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

    if PLATFORM == "windows":
        os.system("cls")
    else:
        os.system("clear")


def set_colors():

    if PLATFORM == "windows":
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
# SPLASH
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
# LOADING
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

    # WINDOWS -> MPV
    if PLATFORM == "windows":

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

    # TERMUX -> ANDROID PLAYER
    else:

        cmd = f'am start -a android.intent.action.VIEW -d "{url}" com.example.hlplayer'

        subprocess.call(cmd, shell=True)


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

            prefix = ">" if i == index else " "

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

        # WINDOWS ARROWS
        if key == b"\xe0":

            k = wait_key()

            if k == b"H":
                index = (index-1) % len(filtered_items)

            if k == b"P":
                index = (index+1) % len(filtered_items)

        # TERMUX ARROWS
        if key == b"\x1b[A":
            index = (index-1) % len(filtered_items)

        if key == b"\x1b[B":
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

            prefix = ">" if i == pos else " "

            print(f"{prefix} {c}")

        print("\nENTER seleccionar | M volver")

        key = wait_key()

        if key == b"m":
            return

        if key == b"\r":

            select_category(categories[pos])
            movie_menu()
            return

        # WINDOWS
        if key == b"\xe0":

            k = wait_key()

            if k == b"H":
                pos = (pos-1) % len(categories)

            if k == b"P":
                pos = (pos+1) % len(categories)

        # TERMUX
        if key == b"\x1b[A":
            pos = (pos-1) % len(categories)

        if key == b"\x1b[B":
            pos = (pos+1) % len(categories)


# ============================
# FILTER CATEGORY
# ============================

def select_category(cat):

    global filtered_items

    filtered_items = [x for x in items if x["category"] == cat]


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

            prefix = ">" if i == pos else " "

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

        # WINDOWS
        if key == b"\xe0":

            k = wait_key()

            if k == b"H":
                pos = (pos-1) % len(options)

            if k == b"P":
                pos = (pos+1) % len(options)

        # TERMUX
        if key == b"\x1b[A":
            pos = (pos-1) % len(options)

        if key == b"\x1b[B":
            pos = (pos+1) % len(options)


# ============================
# INIT
# ============================

select_platform()

set_colors()

ask_username()

splash()

loading_sequence()

items = decrypt_catalog()

filtered_items = items

categories = sorted(list(set([x["category"] for x in items])))

main_menu()