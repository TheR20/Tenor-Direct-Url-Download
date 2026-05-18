# Tenor GIF Downloader / Descargador de GIFs de Tenor

## English

This project downloads multiple GIFs from Tenor automatically using a list of URLs.

It helps you avoid downloading GIFs one by one manually. You only need to paste your Tenor links into a `urls.txt` file, run the Python script, and the downloaded files will be saved inside a folder called `tenor_gifs`.

### Requirements

You need:

- Python 3
- pip

Python libraries used:

- `requests`
- `beautifulsoup4`

### Project structure

Your project folder should look like this:

```txt
tenor-gif-downloader/
├─ descargar_tenor.py
└─ urls.txt
```

After running the script, a new folder will be created automatically:

```txt
tenor-gif-downloader/
├─ descargar_tenor.py
├─ urls.txt
└─ tenor_gifs/
```

### How to use

#### 1. Create the `urls.txt` file

Inside `urls.txt`, paste the Tenor URLs you want to download.

Use one URL per line:

```txt
https://tenor.com/view/example-gif-123456
https://tenor.com/es-MX/view/another-gif-987654
https://media.tenor.com/xxxxxx/tenor.gif
```

#### 2. Install dependencies

Open the terminal inside your project folder and run:

```bash
pip install requests beautifulsoup4
```

If that does not work, try:

```bash
python -m pip install requests beautifulsoup4
```

On Windows, this may also work:

```bash
py -m pip install requests beautifulsoup4
```

#### 3. Run the script

Run:

```bash
python descargar_tenor.py
```

On Windows, if `python` does not work, try:

```bash
py descargar_tenor.py
```

### Result

The script will read every URL inside `urls.txt`, try to find the GIF file, and download it into:

```txt
tenor_gifs/
```

Downloaded files will use automatic names to avoid duplicates, for example:

```txt
001_a1b2c3d4.gif
002_e5f6g7h8.gif
003_9abc1234.gif
```

### Notes

- The script tries to download the `.gif` file when available.
- It can also download direct files from `media.tenor.com`.
- If one URL fails, the script will show an error and continue with the rest.
- Use it only for personal backup or content you have the right to save and use.

---

## Español

Este proyecto descarga automáticamente varios GIFs de Tenor usando una lista de URLs.

Sirve para evitar descargar GIFs manualmente uno por uno. Solo necesitas pegar tus links de Tenor en un archivo `urls.txt`, ejecutar el script de Python y los archivos descargados se guardarán en una carpeta llamada `tenor_gifs`.

### Requisitos

Necesitas tener instalado:

- Python 3
- pip

Librerías de Python utilizadas:

- `requests`
- `beautifulsoup4`

### Estructura del proyecto

La carpeta del proyecto debe verse así:

```txt
descargador-gifs-tenor/
├─ descargar_tenor.py
└─ urls.txt
```

Después de ejecutar el script, se creará automáticamente una nueva carpeta:

```txt
descargador-gifs-tenor/
├─ descargar_tenor.py
├─ urls.txt
└─ tenor_gifs/
```

### Cómo usarlo

#### 1. Crear el archivo `urls.txt`

Dentro de `urls.txt`, pega las URLs de Tenor que quieres descargar.

Debe haber una URL por línea:

```txt
https://tenor.com/view/ejemplo-gif-123456
https://tenor.com/es-MX/view/otro-gif-987654
https://media.tenor.com/xxxxxx/tenor.gif
```

#### 2. Instalar dependencias

Abre la terminal dentro de la carpeta del proyecto y ejecuta:

```bash
pip install requests beautifulsoup4
```

Si ese comando no funciona, prueba:

```bash
python -m pip install requests beautifulsoup4
```

En Windows, también puede funcionar:

```bash
py -m pip install requests beautifulsoup4
```

#### 3. Ejecutar el script

Ejecuta:

```bash
python descargar_tenor.py
```

En Windows, si `python` no funciona, prueba:

```bash
py descargar_tenor.py
```

### Resultado

El script leerá todas las URLs dentro de `urls.txt`, intentará encontrar el archivo GIF y lo descargará en:

```txt
tenor_gifs/
```

Los archivos descargados tendrán nombres automáticos para evitar duplicados, por ejemplo:

```txt
001_a1b2c3d4.gif
002_e5f6g7h8.gif
003_9abc1234.gif
```

### Notas

- El script intenta descargar el archivo `.gif` cuando está disponible.
- También puede descargar archivos directos desde `media.tenor.com`.
- Si una URL falla, el script mostrará un error y continuará con las demás.
- Úsalo solo para respaldo personal o contenido que tengas derecho a guardar y usar.
