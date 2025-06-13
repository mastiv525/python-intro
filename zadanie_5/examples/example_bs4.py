#!/usr/bin/env python3
import argparse
import logging
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_soup(url):
    """
    Pobiera stronę i zwraca obiekt BeautifulSoup.
    """
    resp = requests.get(url)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

def extract_headings(soup):
    """
    Liczy wszystkie nagłówki H1, H2, H3 i zwraca słownik {1: count1, 2: count2, 3: count3}.
    """
    return {level: len(soup.find_all(f"h{level}")) for level in (1, 2, 3)}

def extract_links(soup):
    """
    Zwraca listę wszystkich href z tagów <a>, które zaczynają się od 'http'.
    """
    return [
        tag["href"]
        for tag in soup.find_all("a", href=True)
        if tag["href"].startswith("http")
    ]

def extract_tables(soup):
    """
    Zwraca listę par (index, DataFrame) dla każdej napotkanej tabeli HTML.
    """
    dfs = []
    for idx, table in enumerate(soup.find_all("table"), start=1):
        df = pd.read_html(str(table))[0]
        dfs.append((idx, df))
    return dfs

def main():
    parser = argparse.ArgumentParser(
        description="Parsowanie nagłówków, linków i tabel z HTML"
    )
    parser.add_argument("url", help="adres URL do przetworzenia")
    parser.add_argument(
        "--headings-csv", default="headings.csv",
        help="plik CSV dla statystyk nagłówków"
    )
    parser.add_argument(
        "--links-txt", default="links.txt",
        help="plik TXT ze wszystkimi linkami"
    )
    parser.add_argument(
        "--links-csv", default="links.csv",
        help="plik CSV ze wszystkimi linkami"
    )
    parser.add_argument(
        "--tables-xlsx", default="tables.xlsx",
        help="plik Excel (.xlsx) z wyodrębnionymi tabelami"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    soup = fetch_soup(args.url)

    # === Statystyki nagłówków ===
    headings = extract_headings(soup)
    print("Nagłówki na stronie:")
    for lvl, cnt in headings.items():
        print(f"  H{lvl}: {cnt}")
    with open(args.headings_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Level", "Count"])
        for lvl, cnt in headings.items():
            writer.writerow([f"H{lvl}", cnt])
    logging.info(f"Nagłówki zapisano do {args.headings_csv}")

    # === Linki ===
    links = extract_links(soup)
    print(f"\nZnaleziono {len(links)} linków. Pierwsze 10:")
    for link in links[:10]:
        print(" ", link)
    # TXT
    with open(args.links_txt, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")
    # CSV
    with open(args.links_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Link"])
        for link in links:
            writer.writerow([link])
    logging.info(f"Linki zapisano do {args.links_txt} i {args.links_csv}")

    # === Tabele HTML ===
    tables = extract_tables(soup)
    if tables:
        with pd.ExcelWriter(args.tables_xlsx) as writer:
            for idx, df in tables:
                sheet = f"Table{idx}"
                df.to_excel(writer, sheet_name=sheet, index=False)
        logging.info(f"Tabele zapisano do {args.tables_xlsx}")
    else:
        logging.info("Nie znaleziono żadnych tabel na stronie.")

if __name__ == "__main__":
    main()
