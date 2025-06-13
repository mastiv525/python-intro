#!/usr/bin/env python3
import argparse
import logging
import time
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_html(url):
    """
    Pobiera stronę pod podanym URL-em, zwraca HTML i czas pobrania.
    """
    start = time.time()
    resp = requests.get(url)
    resp.raise_for_status()
    elapsed = time.time() - start
    logging.info(f"Pobrano {len(resp.text)} bajtów z {url} w {elapsed:.2f}s")
    return resp.text

def save_html(html, filename):
    """
    Zapisuje ciąg HTML do pliku o podanej nazwie.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    logging.info(f"Zapisano HTML do {filename}")

def fetch_to_file(url, prefix):
    """
    Pobiera i zapisuje stronę: tworzy plik <prefix>_<url_sanitized>.html
    """
    html = fetch_html(url)
    safe = url.replace("://", "_").replace("/", "_")
    filename = f"{prefix or 'download'}_{safe}.html"
    save_html(html, filename)
    return filename

def main():
    parser = argparse.ArgumentParser(
        description="Pobieranie jednej lub wielu stron HTML równolegle"
    )
    parser.add_argument(
        "urls", nargs="+",
        help="adres(y) URL do pobrania"
    )
    parser.add_argument(
        "-o", "--output-prefix",
        help="prefiks nazwy pliku wynikowego (domyślnie 'download')"
    )
    parser.add_argument(
        "-t", "--threads", type=int, default=4,
        help="liczba wątków do pobierania (domyślnie 4)"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {
            executor.submit(fetch_to_file, url, args.output_prefix): url
            for url in args.urls
        }
        for future in futures:
            fname = future.result()
            print(f"Pobrano i zapisano: {fname}")

if __name__ == "__main__":
    main()
