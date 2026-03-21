# 🎬 Stream

Stream para todos desde línea de comandos.

Herramienta sencilla para reproducir streams, canales de TV desde distintos entornos:

- 📱 Android (usando Termux + APK HLS Player)
- 💻 PC (usando MPV + CMD)

---


## 🛠️ Tecnologías

[![Autor](https://img.shields.io/badge/Autor-TAVO⠀AGUILAR-181717?style=for-the-badge&logo=github)](https://github.com/relay1234)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Version](https://img.shields.io/badge/version-1.0-blue?style=for-the-badge)

![Platform](https://img.shields.io/badge/platform-Android%20%7C%20Windows-lightgrey?style=for-the-badge)


---




## ⚙️ Requisitos

### 📱 Android (Termux + HLS Player)

- Aplicación **HLS Player**  
https://www.mediafire.com/file/pu2amjkrli6r2eh/HLS_PLAYER.apk/file

- Aplicación **Termux**  
https://play.google.com/store/apps/details?id=com.termux


### 💻 Windows (CMD + MPV)

- Reproductor **MPV**  
https://mpv.io/installation/  
https://sourceforge.net/projects/mpv-player-windows/files/64bit/

- Python  
- Visual Studio Code o Notepad  

---

## 🚀 Uso

### ▶️ En Android (Termux + HLS Player)


🔹 Instala el APK **HLS Player**  

🔹 Abre Termux  

🔹 Ejecuta el siguiente comando para clonar el repositorio ```git clone https://github.com/relay1234/stream.git``` 

🔹 Actualiza los paquetes con ```pkg update && pkg upgrade``` 

🔹 Instala dependencias con ```pkg install rust binutils python-cryptography libffi openssl``` 

🔹 Instala requests con ```pip install requests</mark> o <mark>pkg install python-requests``` 

🔹 (Opcional) Da permisos con ```termux-setup-storage```

🔹 Entra a la carpeta con ```cd stream``` y lista con ```ls```  

🔹 Ejecuta el script con ```python multiSO.py```

🔹 Listo, selecciona el stream que más te guste

### ▶️ En Windows (cmd + MPV)
🔹 Descarga e instala python

🔹 Decarga e instala el MPV

🔹 Instala las librerias requests y cryptography con ```pip install requests cryptography```

🔹 Ejecuta el siguiente comando para clonar el repositorio ```git clone https://github.com/relay1234/stream.git```

🔹 Ejecutas el proyecto ya sea con el comando ```python multiSO.py``` y escoges <mark>Windows</mark> o bien puedes ejecutar ```python app.py``` 

> ⚠️ NOTA: Crea una carpeta especifica donde alojaras el proyecto. Si lo quieres guardar en una carpeta dentro del escritorio tipea: cd desktop y presionas enter luego escribes mkdir "proyecto" en donde proyecto equivale al nombre que le quieras dar a la carpeta, despues de crear la carpeta te dirijes a ella con cd proyectos, por ultimo clona el repositorio dentro de esta carpeta y listo.

> ⚠️ NOTA: Para facilitar el uso de MPV, mueve el archivo ZIP descargado al disco C:\. Luego descomprímelo y agrega la carpeta de MPV al PATH del sistema.

---

## ✅ Resultado

- <mark>Reproducción del stream directamente en HLS Player</mark> **EN ANDROID**

* <mark>Reproducción del stream directamente en MVP Player</mark> **EN WINDOWS**

