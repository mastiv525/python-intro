# Web Scraping Lab

Projekt „Web Scraping Lab” pokazuje, jak za pomocą Pythona pobierać i przetwarzać zawartość stron [WWW](http://WWW).

## 📁 Struktura projektu

```
scraping-lab/
├── examples/                # Przykładowe skrypty
│   ├── example_requests.py  # Pobieranie HTML (wielowątkowo)
│   └── example_bs4.py       # Parsowanie nagłówków, linków i tabel
├── requirements.txt         # Lista zależności
├── README.md                # Ten plik
└── raport.md                # Raport z laboratorium
```

## ⚙️ Wymagania

* Python 3.7+
* Biblioteki: `requests`, `beautifulsoup4`, `pandas`, `openpyxl`

Zainstalujesz je poleceniem:

```bash
pip install -r requirements.txt
```

## 🚀 Instalacja i uruchomienie

1. Sklonuj repozytorium:

  

git clone [https://github.com/TwojUser/scraping-lab.git](https://github.com/TwojUser/scraping-lab.git)
cd scraping-lab

````
2. Utwórz i aktywuj wirtualne środowisko (opcjonalnie):
   ```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
````

3. Zainstaluj zależności:

   ```bash
   ```

pip install -r requirements.txt

````
4. Uruchom przykładowe skrypty:
   - Pobieranie HTML (wątkowo):
     ```bash
python examples/example_requests.py https://example.com https://python.org -t 5 -o mysite
````

* Parsowanie HTML:

  ```bash
  ```

python examples/example\_bs4.py [https://en.wikipedia.org/wiki/Web\_scraping](https://en.wikipedia.org/wiki/Web_scraping)

```

## 📄 Opis plików

- `examples/example_requests.py` – skrypt pobiera strony podane w argumencie, mierzy czas, zapisuje HTML do plików.
- `examples/example_bs4.py` – skrypt parsuje nagłówki (H1–H3), linki oraz tabele, zapisując je do CSV, TXT i XLSX.
- `requirements.txt` – lista bibliotek potrzebnych do działania skryptów.
- `raport.md` – szczegółowy raport opisujący wykonane zadania, ograniczenia i możliwe usprawnienia.

## 📝 Licencja

Pliki w tym repozytorium są dostępne na licencji MIT.

---

Dalsze informacje i instrukcje znajdziesz w pliku `raport.md`.

```
