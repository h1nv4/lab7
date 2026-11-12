# Laboratorium 7: drzewa decyzyjne – kto odejdzie z programu lojalnościowego?

## Krok po kroku
1. **Use this template / Fork** to repozytorium na swoje konto GitHub.
2. **Code → Codespaces → Create codespace on main**. Poczekaj, aż otworzy się VS Code w przeglądarce.
3. W terminalu (na dole ekranu):
   ```bash
   pip install -r requirements.txt
   ```
4. Otwórz `lab7_student.ipynb`, wybierz jądro **Python 3** i wykonuj komórki po kolei (*Shift + Enter*). Uzupełnij luki `___`.
5. Aplikacja (zadanie Z10):
   ```bash
   streamlit run app.py
   ```
   Codespaces zaproponuje otwarcie portu **8501**: kliknij *Open in Browser*.
6. Zapisz pracę w repozytorium:
   ```bash
   git add .
   git commit -m "Lab 7: drzewa decyzyjne"
   git push
   ```
7. **Render:** *New → Web Service* → wybierz swoje repozytorium. Ustawienia są w `render.yaml` (plan *Free*).
   Pierwsze uruchomienie trwa kilka minut. Link do aplikacji wklej do karty zadań.

## Pliki
| Plik | Co to jest |
|---|---|
| `lab7_student.ipynb` | notatnik z zadaniami Z1–Z10 |
| `klienci_odejscia.csv` | 1206 klientów programu lojalnościowego (dane syntetyczne) |
| `dziesieciu_klientow.csv` | 10 klientów do rozgrzewki (Z1) |
| `app.py` | kalkulator ryzyka odejścia (Streamlit) |
| `requirements.txt`, `render.yaml` | biblioteki i ustawienia wdrożenia na Render |
