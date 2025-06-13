# Raport z Zadania 5 – Web Scraping

Poniższy plik `raport.md` znajduje się w katalogu `zadanie_5` repozytorium „python-intro”:

```
https://github.com/mastiv525/python-intro/tree/main/zadanie_5
```

## 1. Cel zadania

* Napisanie dwóch skryptów Pythona do pobierania i analizy stron [WWW](http://WWW).
* Użycie bibliotek: `requests`, `BeautifulSoup`, `pandas`.
* Rozszerzenie funkcjonalności: wątkowość, CLI (`argparse`), pomiar czasu, logowanie (`logging`), eksport do plików (HTML, CSV, TXT, XLSX).

## 2. Struktura katalogu `zadanie_5`

```
python-intro/
└── zadanie_5/
    ├── examples/
    │   ├── example_requests.py
    │   └── example_bs4.py
    ├── requirements.txt
    ├── README.md
    └── raport.md
```

## 3. Opis plików

* **requirements.txt** – `requests`, `beautifulsoup4`, `pandas`, `openpyxl`.
* **examples/example\_requests.py** – pobiera listę URL równolegle, mierzy czas, zapisuje każdy HTML do pliku.
* **examples/example\_bs4.py** – parsuje HTML: liczy nagłówki H1–H3, wyciąga linki, odczytuje tabele do arkusza Excel.
* **README.md** – instrukcja uruchomienia zadania.
* **raport.md** – ten dokument.

## 4. Instrukcja uruchomienia

1. `git clone https://github.com/mastiv525/python-intro.git`
2. `cd python-intro/zadanie_5`
3. (opcjonalnie) `python -m venv venv` & aktywacja środowiska:

   * Windows: `venv\Scripts\activate`
   * macOS/Linux: `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python examples/example_requests.py <URL1> <URL2> -t 4 -o prefix`
6. `python examples/example_bs4.py <URL>`

## 5. Działanie skryptów

1. **example\_requests.py**

   * **argparse**: lista URL, `--threads`, `--output-prefix`.
   * **wątkowość**: `ThreadPoolExecutor` przyspiesza pobieranie.
   * **pomiar czasu**: `time.time()`.
   * **zapis HTML**: do plików `prefix_url.html`.
   * **logging**: komunikaty INFO z timestampem.

2. **example\_bs4.py**

   * **argparse**: URL i nazwy plików wynikowych.
   * **parsowanie**: `BeautifulSoup`.
   * **nagłówki**: liczba H1–H3, zapisywane do `headings.csv`.
   * **linki**: wszystkie `href` rozpoczynające się od `http`, zapis do `links.txt` i `links.csv`.
   * **tabele**: `pandas.read_html`, zapis do `tables.xlsx`.

## 6. Ograniczenia

* **Brak JS**: `requests` nie renderuje JavaScript.
* **Blokady**: brak obsługi nagłówków przeglądarki, może wystąpić `403` lub CAPTCHA.
* **Paginacja**: skrypty obsługują tylko jedną stronę.
* **Legalność**: brak automatycznej weryfikacji `robots.txt`.
* **Struktura HTML**: niespójne tabele i nagłówki mogą powodować błędy.

## 7. Propozycje usprawnień

* **Selenium/Playwright** do stron dynamicznych.
* **Cache** lokalne, by unikać wielokrotnego pobierania.
* Obsługa **paginacji** i linkowania między stronami.
* Rozszerzone **nagłówki HTTP** i sesje.
* **Automatyczne testy** funkcjonalne.

---

*Autor: mastiv525*
