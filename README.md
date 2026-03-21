Stream para todos desde linea de comandos.

Herramienta sencilla para reproducir streams, canales de tv desde distintos entornos:

- 📱 Android (usando Termux + APK HLS Player)
- 💻 PC (usando MPV + CMD)

---

## ⚙️ Requisitos

### 📱 Android (Termux)

- Aplicación **HLS Player**
- Descargar APK:
  https://www.mediafire.com/file/pu2amjkrli6r2eh/HLS_PLAYER.apk/file
  
- Aplicación **Termux**
- Descargar PLAY STORE:
  https://play.google.com/store/apps/details?id=com.termux
---

### 💻 PC (Windows - CMD)

- Reproductor **MPV**
- Descargar desde:
  https://mpv.io/installation/

---

## 🚀 Uso

### ▶️ En Android (Termux + HLS Player)

1. Instala el APK **HLS Player**
2. Abre Termux
3. Ejecuta el script o comando del stream
4. Se abrirá automáticamente en HLS Player

Ejemplo:

```bash
am start -a android.intent.action.VIEW -d "URL_DEL_STREAM"
