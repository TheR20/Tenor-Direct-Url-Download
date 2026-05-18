import os
import re
import time
import hashlib
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

CARPETA_SALIDA = "tenor_gifs"
ARCHIVO_URLS = "urls.txt"

os.makedirs(CARPETA_SALIDA, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def extension_de_url(url):
    path = urlparse(url).path.lower()
    for ext in [".gif", ".mp4", ".webm", ".webp"]:
        if ext in path:
            return ext
    return ".gif"

def nombre_archivo(url, ext, index):
    h = hashlib.md5(url.encode("utf-8")).hexdigest()[:8]
    return f"{index:03d}_{h}{ext}"

def es_media_directa(url):
    return "media.tenor.com" in urlparse(url).netloc

def encontrar_media_en_pagina(html, preferir_gif=True):
    soup = BeautifulSoup(html, "html.parser")

    candidatos = []

    # Metadatos comunes: og:image suele apuntar a GIF/imagen; og:video a MP4
    for prop in ["og:image", "og:video", "twitter:image", "twitter:player:stream"]:
        tag = soup.find("meta", attrs={"property": prop}) or soup.find("meta", attrs={"name": prop})
        if tag and tag.get("content"):
            candidatos.append(tag["content"])

    # Búsqueda de respaldo dentro del HTML
    regexes = [
        r"https://media\.tenor\.com/[^\"'\s<>]+\.gif[^\"'\s<>]*",
        r"https://media\.tenor\.com/[^\"'\s<>]+\.mp4[^\"'\s<>]*",
        r"https://media\.tenor\.com/[^\"'\s<>]+\.webp[^\"'\s<>]*",
        r"https://media\.tenor\.com/[^\"'\s<>]+\.webm[^\"'\s<>]*",
    ]

    for rgx in regexes:
        candidatos.extend(re.findall(rgx, html))

    # Quitar duplicados conservando orden
    vistos = set()
    candidatos = [c for c in candidatos if not (c in vistos or vistos.add(c))]

    if preferir_gif:
        for c in candidatos:
            if ".gif" in urlparse(c).path.lower():
                return c

    return candidatos[0] if candidatos else None

def descargar(url, index):
    url = url.strip()
    if not url:
        return

    try:
        if es_media_directa(url):
            media_url = url
        else:
            r = requests.get(url, headers=HEADERS, timeout=20)
            r.raise_for_status()
            media_url = encontrar_media_en_pagina(r.text, preferir_gif=True)

            if not media_url:
                print(f"[ERROR] No encontré media en: {url}")
                return

        ext = extension_de_url(media_url)
        archivo = os.path.join(CARPETA_SALIDA, nombre_archivo(media_url, ext, index))

        if os.path.exists(archivo):
            print(f"[SKIP] Ya existe: {archivo}")
            return

        with requests.get(media_url, headers=HEADERS, stream=True, timeout=30) as resp:
            resp.raise_for_status()
            with open(archivo, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

        print(f"[OK] {archivo}")

        # Pequeña pausa para no pegarle demasiado rápido a Tenor
        time.sleep(0.5)

    except Exception as e:
        print(f"[ERROR] {url} -> {e}")

def main():
    with open(ARCHIVO_URLS, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Descargando {len(urls)} URLs...")
    for i, url in enumerate(urls, start=1):
        descargar(url, i)

    print("Listo.")

if __name__ == "__main__":
    main()