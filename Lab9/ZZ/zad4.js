
// Pobieramy elementy z dokumentu HTML
const rows = document.querySelectorAll("tr");
const startBtn = document.querySelector("button#start");
const resetBtn = document.querySelector("button#reset");
const pointsEl = document.querySelector("#points");
const gameOverEl = document.querySelector("#end");

// Definiujemy zmienne

// Kolumny początkowe
const Kolumny_Poczatkowe = 2;
// Tyle mamy kolumn na początku
let noColumns = Kolumny_Poczatkowe;
// Liczba puntków
let punkty = 0;
let columnsIntervalID;
let cellIntervalID;

// Tworzenie losowej liczby z zakresu
const generateRandomInt = function(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};

// Funkcja odpowiadająca za tworzenie komórek
const createCell = function() {
    // Tworzona jest komórka
    const cell = document.createElement("td");
    // Generujemy losowe liczby z zakresu i zaleznie od wylosowanej liczby bedzie zalezec wartosc wpisana do komórki
    const randomNum = generateRandomInt(0, 2); // 0 -> 0, 1 -> 1, 2 -> -1
    switch (randomNum) {
        case 0:
            cell.textContent = "0";
            break;
        case 1:
            cell.textContent = "1";
            break;
        case 2:
            cell.textContent = "-1";
    }

    // Obserwator wydarzenia - jezeli klikniemy odpowiednia komórke dodajemy lub odejmujemy punkty
    cell.addEventListener("click", function(e) {
        // Funkcja parsująca zawartosc komórki w zaleznosci od liczby dodajemy lub odejmujemy punkty
        punkty += parseInt(e.target.textContent);
        // Zdobyte przez nas punkty wypisywane są w konsoli
        console.log(punkty);
    });
    // Zwracamy komórkę
    return cell;
};

// Generowanie kolumn z losowymi wartościami
const wygeneruj_kolumne = function() {
    rows.forEach(function(row) {
        // Dla każdego wiersza w kolumnie musimy stworzyć komórkę
        for (let i = 0; i < Kolumny_Poczatkowe; i++) {
            row.appendChild(createCell());
        }
    });
};

// Wywołujemy funkcje aby stworzyć 2 początkowe kolumny
wygeneruj_kolumne();

  // Funkcja generująca losowe wartości dla komórek
const wygeneruj_losowa_wartosc_komorki = function() {
    // Losowo wybierany index wiersza
    const rowIndex = generateRandomInt(0, 9);
    // Losowo wybieramy index kolumny zależy on od zmiennej noColumns -1 bo tyle mamy kolumn
    const colIndex = generateRandomInt(0, noColumns - 1);

    // Funkcja generująca nową wartość do komórek
    const newValue = generateRandomInt(0, 2);
    const cell = rows[rowIndex].querySelectorAll("td")[colIndex];
    switch (newValue) {
        case 0:
            cell.textContent = "0";
            break;
        case 1:
            cell.textContent = "1";
            break;
        case 2:
            cell.textContent = "-1";
    }
};

// Funkcja która dodaje losową kolumne w losowym interwale czasowym po lewej lub prawej stronie
const Dodaj_Losowa_Kolumne = function() {
    let addOnEnd = undefined;
    // Generujemy losową liczbe z zakresu
    const helper = generateRandomInt(0, 1);
    // Zaleznie od wyniku co jest w zmiennej helper kolumna zostanie dodana na poczatku lub koncu
    addOnEnd = helper === 0 ? false : true;


    rows.forEach(function(row) {
        if (addOnEnd) {
            row.appendChild(createCell());
        } else {
            row.insertAdjacentElement("afterbegin", createCell());
        }
    });

    // Zwiekszamy liczbe kolumn
    noColumns++;

    // Jeżeli liczba kolumn osiągnie 10 gra kończy swoje działnie
    if (noColumns === 10) {
        // Resetujemy ustawienia Interval
        clearInterval(columnsIntervalID);
        clearInterval(cellIntervalID);
        // Konwertujemy liczbę punktów do stringa
        pointsEl.textContent = punkty.toString();
        // Wyświetlamy napis koniec gry
        gameOverEl.textContent = "Koniec gry!";
    }
};

// Dodajemy obserwatora do przycisku start
startBtn.addEventListener("click", function() {
    // Po kliknieciu uruchamiamy funkcje ktora dodaje kolumne
    columnsIntervalID = setInterval(Dodaj_Losowa_Kolumne, 1000);
    // Co 0,05s zmieniamy wartosc losową
    cellIntervalID = setInterval(wygeneruj_losowa_wartosc_komorki, 50);
    // Wyświetlamy na ekranie napis
    gameOverEl.textContent = "Miłej Gry!!";
});

// Dodajemy obserwatora do przycisku reset
resetBtn.addEventListener("click", function() {
    noColumns = Kolumny_Poczatkowe;
    // Zerujemy punkty
    punkty = 0;
    pointsEl.textContent = "0";
    gameOverEl.textContent = "";
    rows.forEach(function(row) {
        row.innerHTML = "";
    });
    // Czyścimy funkcje dodająca kolumny
    clearInterval(columnsIntervalID);
    // Czyścimy funkcje genurjącą losową wartość
    clearInterval(cellIntervalID);
    // Generujemy nowe kolumny
    wygeneruj_kolumne();
});

