# Web Scraping Lab

Projekt „Web Scraping Lab” prezentuje praktyczne przykłady pobierania i analizowania stron WWW za pomocą Pythona.

## 📂 Struktura katalogu `zadanie_5`

```
python-intro/
└── zadanie_5/
    ├── examples/
    │   ├── example_requests.py  # pobieranie HTML (wątkowo, zapisywanie do plików)
    │   └── example_bs4.py       # parsowanie nagłówków, linków, tabel, eksport danych
    ├── requirements.txt        # lista bibliotek: requests, beautifulsoup4, pandas, openpyxl
    ├── README.md               # ten plik: instrukcja uruchomienia i opisu projektu
    └── raport.md               # raport z wykonania zadania
```

## ⚙️ Wymagania

* Python 3.7 lub nowszy
* Moduły Python:

  * `requests`
  * `beautifulsoup4`
  * `pandas`
  * `openpyxl`

Zainstalujesz je poleceniem:

```bash
pip install -r requirements.txt
```

## 🚀 Uruchomienie

1. **Sklonuj repozytorium**

 

git clone [https://github.com/mastiv525/python-intro.git](https://github.com/mastiv525/python-intro.git)
cd python-intro/zadanie\_5

````
2. **(Opcjonalnie) Utwórz i aktywuj** środowisko wirtualne:
   ```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
````

3. **Zainstaluj zależności**

   ```bash
   pip install -r requirements.txt
   ```



````
4. **Uruchom przykład pobierania HTML**
   ```bash
python examples/example_requests.py <URL1> <URL2> -t 4 -o prefix
````

5. **Uruchom parsowanie HTML**

   ```bash
   python examples/example\_bs4.py <URL>
   ```


6. **Wnioski**
```

## 📄 Opis skryptów
- **example_requests.py**
  - Pobiera wiele stron równolegle (ThreadPoolExecutor)
  - Mierzy czas pobrania i zapisuje każdy HTML do pliku `prefix_<url>.html`
  - Używa `argparse` (URL, --threads, --output-prefix) i `logging` dla czytelnych komunikatów

- **example_bs4.py**
  - Parsuje pobrany HTML (BeautifulSoup)
  - Wylicza liczbę nagłówków H1–H3 i zapisuje je do `headings.csv`
  - Zbiera wszystkie linki `http` i zapisuje do `links.txt` i `links.csv`
  - Ekstraktuje tabele HTML (pandas.read_html) i zapisuje do arkusza `tables.xlsx`

## ⚠️ Ograniczenia
- `requests` nie renderuje JavaScript — strony dynamiczne (SPA) mogą być niekompletne
- Brak automatycznej obsługi `robots.txt` i nagłówków przeglądarki — może dojść do blokad serwera
- Skrypty nie obsługują paginacji ani nawigacji przez wiele podstron
- Struktura HTML różni się w zależności od serwisu — nie wszystkie tabele i nagłówki zostaną poprawnie zidentyfikowane

## 🔮 Możliwe usprawnienia
- Integracja z Selenium lub Playwright dla stron wymagających JavaScript
- Dodanie cache lokalnego, by unikać wielokrotnych zapytań do tych samych stron
- Obsługa paginacji i automatyczne śledzenie linków wewnętrznych
- Rozszerzenie nagłówków HTTP i zarządzanie sesjami (ciasteczka, tokeny)
- Automatyczne testy jednostkowe i integracyjne dla crawlera

---
*Autor: mastiv525*

```
