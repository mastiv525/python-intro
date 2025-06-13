# Raport z Laboratorium 5 – Web Scraping

## 1. Wprowadzenie

Celem laboratorium było stworzenie prostych skryptów w Pythonie do pobierania i parsowania zawartości stron internetowych. W projekcie wykorzystaliśmy dwie popularne biblioteki:

* **requests** – do obsługi zapytań HTTP (GET)
* **BeautifulSoup** – do parsowania i przetwarzania drzewa HTML

Ponadto rozszerzyliśmy funkcjonalność podstawowych przykładów o:

* wielowątkowe pobieranie stron
* pomiar czasu i zapisywanie zawartości do pliku
* dynamiczny interfejs CLI (`argparse`)
* zaawansowane logowanie zdarzeń (`logging`)
* eksport danych (nagłówki, linki, tabele) do plików CSV, TXT i XLSX

## 2. Zawartość skryptów

### 2.1 `example_requests.py`

1. **Interfejs linii poleceń**: wykorzystanie modułu `argparse` pozwala na podanie:

   * listy adresów URL do pobrania (`urls`)
   * liczby wątków (`--threads`)
   * opcjonalnego prefiksu pliku wyjściowego (`--output-prefix`)
2. **Wielowątkowe pobieranie**: `concurrent.futures.ThreadPoolExecutor` umożliwia równoległe zapytania, co znacząco przyspiesza proces przy większej liczbie URL.
3. **Pomiar czasu**: funkcja `fetch_html` mierzy czas wykonania żądania HTTP.
4. **Zapis HTML**: pobrany kod strony zapisywany jest do pliku o nazwie z prefiksem i sanitizowanym URL-em.
5. **Logowanie**: moduł `logging` rejestruje zdarzenia (INFO) z timestampami, co ułatwia monitorowanie przebiegu skryptu.

### 2.2 `example_bs4.py`

1. **Dynamiczny CLI**: `argparse` definiuje argumenty:

   * URL do analizy
   * nazwy plików wynikowych (`--headings-csv`, `--links-txt`, `--links-csv`, `--tables-xlsx`)
2. **Parsowanie nagłówków**: funkcja `extract_headings` liczy wystąpienia tagów `<h1>`, `<h2>`, `<h3>` i zapisuje statystyki w CSV.
3. **Wyciąganie linków**:

   * `extract_links` zbiera wszystkie linki z atrybutem `href` zachowując tylko te zaczynające się od `http`.
   * Linki wypisywane są na konsolę (pierwsze 10) i zapisywane do TXT oraz CSV.
4. **Ekstrakcja tabel**: funkcja `extract_tables` wykorzystuje `pandas.read_html` do konwersji tabel HTML na obiekty `DataFrame` i zapisuje je do arkusza Excel (`.xlsx`).
5. **Logowanie**: podobnie jak w `example_requests.py`, komunikaty o przebiegu działania są rejestrowane przy pomocy `logging`.

## 3. Instrukcja uruchomienia

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/TwojUser/scraping-lab.git
   cd scraping-lab
   ```
2. Utwórz i aktywuj środowisko wirtualne:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Zainstaluj zależności:

   ```bash
   pip install -r requirements.txt
   ```
4. Uruchom skrypt pobierający HTML (przykład z wieloma URL):

   ```bash
   python examples/example_requests.py https://example.com https://python.org -t 5 -o mysite
   ```
5. Uruchom skrypt parsujący HTML:

   ```bash
   python examples/example_bs4.py https://en.wikipedia.org/wiki/Web_scraping
   ```

## 4. Ograniczenia i wyzwania

1. **Statyczne pobieranie** – `requests` nie wykonuje JavaScript. Strony wymagające renderingu (SPA, AJAX) nie zostaną poprawnie pobrane.
2. **Zachowanie stron** – brak symulacji przeglądarki (nagłówki, cookies, sesje), co może skutkować blokadą (np. CAPTCHA, `403 Forbidden`).
3. **Brak obsługi paginacji** – skrypty pobierają tylko jedną stronę, bez iteracji po kolejnych.
4. **Brak polityki `robots.txt`** – należy ręcznie sprawdzać legalność i dopuszczalne limity pobrań.
5. **Wątkowość** – dla bardzo dużej liczby URL może wymagać throttlingu lub ograniczeń, by nie przeciążyć serwera.
6. **Parsing tabel** – nie każda tabela w HTML jest dobrze ustrukturyzowana; `pandas.read_html` może rzucić błąd.

## 5. Możliwe usprawnienia

* Integracja z **Selenium** lub **Playwright** dla stron dynamicznych.
* Dodanie **cache** lokalnego, by unikać wielokrotnego pobierania tych samych zasobów.
* Obsługa **paginacji** i nawigacji po linkach wewnętrznych.
* Zaawansowany **parser treści** (np. wyciąganie danych z JSON lub API w tle).
* Implementacja **limitów zapytań** według `robots.txt` i przerw między żądaniami.
* Rozbudowany **monitoring** i **metryki** (np. średni czas odpowiedzi, liczba błędów).

## 6. Podsumowanie

W ramach laboratorium powstały dwa skrypty demonstrujące różne aspekty web scraping’u:

* **example\_requests.py** – skupia się na efektywnym pobieraniu i zapisywaniu zawartości stron.
* **example\_bs4.py** – pokazuje techniki parsowania HTML, ekstrakcji nagłówków, linków i tabel.

Oba narzędzia można łatwo rozszerzać i integrować w większe aplikacje czy automatyczne procesy ekstrakcji danych. Dokumentacja i modularna budowa kodu ułatwiają dalszy rozwój i utrzymanie.
