Stream para todos desde linea de comandos.

Herramienta sencilla para reproducir streams, canales de tv desde distintos entornos:

- 📱 Android (usando Termux + APK HLS Player)
- 💻 PC (usando MPV + CMD)

---

## ⚙️ Requisitos

### 📱 Android (Termux + HLSplayer)

- Aplicación **HLS Player**
- Descargar APK:
  https://www.mediafire.com/file/pu2amjkrli6r2eh/HLS_PLAYER.apk/file
  
- Aplicación **Termux**
- Descargar PLAY STORE:
  https://play.google.com/store/apps/details?id=com.termux

### 💻 Windows (CMD + mpv )

- Reproductor **MPV**
- Descargar desde:
  https://mpv.io/installation/
  https://sourceforge.net/projects/mpv-player-windows/files/64bit/
  
- python
- visual studio code O Notepad 
---

## 🚀 Uso

### ▶️ En Android (Termux + HLS Player)

1. Instala el APK **HLS Player**
2. Abre Termux
3. Ejecuta el siguiente comando para clonar el repositorio <mark>git clone https://github.com/relay1234/stream.git</mark>
4. Actualizamos los paquetes y repositorios de termux con el comando >pkg update \&\& pkg upgrade
5. Ejecutamos este comando para usar librerias y herramientas que vamos a necesitar pkg install rust binutils python-cryptography libffi openssl
6. instalamos requests con pip install requests   O   pkg install pyhon-requests
7. Ahora para conceder el acceso a todos los archivos del dispositivos solo si es necesitarios tipeamos el siguiente comando termux-setup-storage
8. accedemos al archivo que clonamos y enlistamos con ls
9. lo corremos con Python multiSO.py
10. Listo seleccionamos el stream que mas nos guste.

