"""Kalkulator ryzyka odejścia klienta: drzewo decyzyjne z laboratorium 7 (eksploracja danych)."""
import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

CECHY = ["liczba_zamowien", "wydatki_zl", "sredni_koszyk_zl", "dni_od_ostatniego",
         "udzial_promocji", "udzial_internet", "liczba_kategorii", "zwroty"]


@st.cache_resource
def naucz_model():
    df = pd.read_csv("klienci_odejscia.csv", sep=";", decimal=",")
    X_ucz, X_test, y_ucz, y_test = train_test_split(df[CECHY], df["odszedl"], test_size=0.3,
                                                    stratify=df["odszedl"], random_state=42)
    model = DecisionTreeClassifier(max_depth=3, min_samples_leaf=20, random_state=0).fit(X_ucz, y_ucz)
    return model, model.score(X_test, y_test)


model, trafnosc = naucz_model()

st.title("Kto odejdzie z programu lojalnościowego?")
st.caption(f"Drzewo decyzyjne: głębokość 3, min. 20 klientów w liściu. Trafność na zbiorze testowym: {100 * trafnosc:.1f}%. Dane syntetyczne.")

st.sidebar.header("Klient")
liczba = st.sidebar.number_input("liczba zamówień (12 mies.)", 1, 60, 3)
koszyk = st.sidebar.number_input("średni koszyk [zł]", 10.0, 5000.0, 200.0, step=10.0)
dni = st.sidebar.slider("dni od ostatniego zamówienia", 0, 364, 60)
promo = st.sidebar.slider("udział zamówień z promocją", 0.0, 1.0, 0.3)
net = st.sidebar.slider("udział zamówień przez internet", 0.0, 1.0, 0.5)
kat = st.sidebar.slider("liczba kategorii", 1, 5, 2)
zwroty = st.sidebar.number_input("zwroty", 0, 20, 0)
prog = st.sidebar.slider("próg wysyłki kuponu", 0.05, 0.95, 0.40, step=0.05)

klient = pd.DataFrame([{"liczba_zamowien": liczba, "wydatki_zl": liczba * koszyk, "sredni_koszyk_zl": koszyk,
                        "dni_od_ostatniego": dni, "udzial_promocji": promo, "udzial_internet": net,
                        "liczba_kategorii": kat, "zwroty": zwroty}])[CECHY]
ryzyko = model.predict_proba(klient)[0, 1]

c1, c2 = st.columns(2)
c1.metric("ryzyko odejścia", f"{100 * ryzyko:.0f}%")
c2.metric("decyzja", "wyślij kupon" if ryzyko >= prog else "bez kuponu")

# ścieżka klienta w drzewie
st.subheader("Dlaczego? Ścieżka w drzewie")
drzewo = model.tree_
wezly = model.decision_path(klient).indices
for w in wezly:
    if drzewo.children_left[w] == -1:
        n0, n1 = drzewo.value[w][0]
        st.write(f"**Liść:** w danych uczących odeszło {100 * n1 / (n0 + n1):.0f}% klientów z tej grupy ({drzewo.n_node_samples[w]} klientów).")
    else:
        cecha, prog_w = CECHY[drzewo.feature[w]], drzewo.threshold[w]
        tak = klient.iloc[0][cecha] <= prog_w
        st.write(f"{cecha} = {klient.iloc[0][cecha]:.2f} {'≤' if tak else '>'} {prog_w:.2f}")

with st.expander("Całe drzewo jako reguły"):
    st.code(export_text(model, feature_names=CECHY))
