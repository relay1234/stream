# 🎬 Stream

Stream para todos desde línea de comandos.

Herramienta sencilla para reproducir streams, canales de TV desde distintos entornos:

- 📱 Android (usando Termux + APK HLS Player)
- 💻 PC (usando MPV + CMD)

---

## ⚙️ Requisitos

### 📱 Android (Termux + HLS Player)

- Aplicación **HLS Player**  
https://www.mediafire.com/file/pu2amjkrli6r2eh/HLS_PLAYER.apk/file

- Aplicación **Termux**  
https://play.google.com/store/apps/details?id=com.termux

---

### 💻 Windows (CMD + MPV)

- Reproductor **MPV**  
https://mpv.io/installation/  
https://sourceforge.net/projects/mpv-player-windows/files/64bit/

- Python  
- Visual Studio Code o Notepad  

---

## 🚀 Uso

### ▶️ En Android (Termux + HLS Player)

1. Instala el APK **HLS Player**  
2. Abre Termux  
3. Ejecuta el siguiente comando para clonar el repositorio <mark>git clone https://github.com/relay1234/stream.git</mark>  
4. Actualiza los paquetes con <mark>pkg update && pkg upgrade</mark>  
5. Instala dependencias con <mark>pkg install rust binutils python-cryptography libffi openssl</mark>  
6. Instala requests con <mark>pip install requests</mark> o <mark>pkg install python-requests</mark>  
7. (Opcional) Da permisos con <mark>termux-setup-storage</mark>  
8. Entra a la carpeta con <mark>cd stream</mark> y lista con <mark>ls</mark>  
9. Ejecuta el script con <mark>python multiSO.py</mark>  
10. Listo, selecciona el stream que más te guste  

---

## ✅ Resultado

<mark>Reproducción del stream directamente en HLS Player</mark>
