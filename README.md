# Progetto sull'onion routing riguardo la rete Tor

🇮🇹 [Italiano](#italiano) | 🇬🇧 [English](#english)

---

<a id="italiano"></a>

## 🇮🇹 Italiano

### 📌 Descrizione

Progetto scolastico realizzato per la materia di **Inglese (madrelingua)** sul tema dell'**onion routing**, la tecnica alla base della rete **Tor**. Il progetto contiene un **simulatore in Python** (con testi e commenti in inglese) che mostra come un messaggio viene cifrato a "strati", come una cipolla, e poi decifrato uno strato alla volta dai nodi della rete.

**Come funziona il simulatore (versione offline):**
1. L'utente sceglie il numero di nodi (strati) da usare (Tor ne usa di solito 3) e conferma la scelta con Y/N.
2. Per ogni nodo viene generata una coppia di chiavi **RSA a 2048 bit**.
3. L'utente scrive un messaggio segreto e lo conferma con Y/N.
4. Il messaggio viene cifrato a strati: per ogni nodo si genera una chiave **AES a 128 bit** (modalità EAX), che cifra i dati, mentre la chiave AES stessa viene cifrata con la chiave pubblica RSA del nodo (**PKCS1_OAEP**).
5. Il messaggio "a cipolla" viene poi elaborato nodo per nodo: a ogni passaggio il programma stampa in esadecimale la chiave AES cifrata, il nonce, il testo cifrato, il tag e i dati decifrati, fino a mostrare il messaggio originale nel nodo finale.

> Il programma è una simulazione locale e didattica: tutti i "nodi" sono eseguiti nello stesso processo, senza alcuna connessione di rete reale.

### 📂 Contenuto della repository

| Percorso | Descrizione |
|---|---|
| `Versione offline/Onion routing simulator for Tor network (offline version).py` | Codice sorgente Python del simulatore |
| `Versione offline/Onion routing simulator for Tor network (offline version).ipynb` | Lo stesso programma come notebook Jupyter, diviso in sezioni commentate |
| `Versione offline/Onion routing simulator for Tor network (offline version).pdf` | Esportazione PDF del notebook con un esempio di esecuzione completa (3 nodi) |
| `Versione offline/Onion routing simulator for Tor network (offline version).exe` | Versione eseguibile per Windows del simulatore (creata con PyInstaller, non richiede Python installato) |
| `Versione online (rete locale)/` | Cartella segnaposto (contiene solo un file vuoto `File 0`) |
| `Versione online (rete Tor)/` | Cartella segnaposto (contiene solo un file vuoto `File 0`) |
| `.gitignore` | Esclude file temporanei di Python, editor e ambienti virtuali |

### 🛠️ Tecnologie utilizzate

- **Python 3** (il notebook indica Python 3.11)
- **PyCryptodome** (modulo `Crypto`): RSA, PKCS1_OAEP, AES
- **Jupyter Notebook**

### ▶️ Come eseguirlo

**Script Python:**
```bash
pip install pycryptodome
cd "Versione offline"
python "Onion routing simulator for Tor network (offline version).py"
```

**Notebook:** apri il file `.ipynb` con Jupyter Notebook / JupyterLab o VS Code ed esegui le celle in ordine.

**Eseguibile (Windows):** fai doppio clic sul file `.exe` nella cartella `Versione offline`.

**PDF:** consultabile con qualsiasi lettore PDF per vedere codice e output di esempio senza eseguire nulla.

### 📋 Requisiti

- Python 3 con la libreria `pycryptodome` (per `.py` e `.ipynb`)
- Jupyter per aprire il notebook
- Windows per l'eseguibile `.exe`

### 👤 Autore

**Matteo** – [MatteoMgr2008](https://github.com/MatteoMgr2008)

---

<a id="english"></a>

## 🇬🇧 English

### 📌 Description

School project made for the **English (native-speaker teacher)** subject on the topic of **onion routing**, the technique behind the **Tor** network. The project contains a **Python simulator** (with English prompts and comments) that shows how a message is encrypted in "layers", like an onion, and then decrypted one layer at a time by the network nodes.

**How the simulator works (offline version):**
1. The user chooses the number of nodes (layers) to use (Tor usually uses 3) and confirms with Y/N.
2. A **2048-bit RSA** key pair is generated for each node.
3. The user types a secret message and confirms it with Y/N.
4. The message is encrypted in layers: for each node a **128-bit AES** key (EAX mode) encrypts the data, while the AES key itself is encrypted with the node's RSA public key (**PKCS1_OAEP**).
5. The onion message is then processed node by node: at each step the program prints, in hexadecimal, the encrypted AES key, nonce, ciphertext, tag and decrypted data, until the original message is shown at the final node.

> The program is a local, educational simulation: all "nodes" run in the same process, with no real network connection.

### 📂 Repository contents

| Path | Description |
|---|---|
| `Versione offline/Onion routing simulator for Tor network (offline version).py` | Python source code of the simulator |
| `Versione offline/Onion routing simulator for Tor network (offline version).ipynb` | The same program as a Jupyter notebook, split into commented sections |
| `Versione offline/Onion routing simulator for Tor network (offline version).pdf` | PDF export of the notebook with a full sample run (3 nodes) |
| `Versione offline/Onion routing simulator for Tor network (offline version).exe` | Windows executable version of the simulator (built with PyInstaller, no Python installation needed) |
| `Versione online (rete locale)/` | Placeholder folder ("online version – local network"; contains only an empty `File 0`) |
| `Versione online (rete Tor)/` | Placeholder folder ("online version – Tor network"; contains only an empty `File 0`) |
| `.gitignore` | Excludes Python temp files, editor files and virtual environments |

### 🛠️ Technologies used

- **Python 3** (the notebook reports Python 3.11)
- **PyCryptodome** (`Crypto` module): RSA, PKCS1_OAEP, AES
- **Jupyter Notebook**

### ▶️ How to run it

**Python script:**
```bash
pip install pycryptodome
cd "Versione offline"
python "Onion routing simulator for Tor network (offline version).py"
```

**Notebook:** open the `.ipynb` file with Jupyter Notebook / JupyterLab or VS Code and run the cells in order.

**Executable (Windows):** double-click the `.exe` file in the `Versione offline` folder.

**PDF:** open it with any PDF reader to see the code and a sample output without running anything.

### 📋 Requirements

- Python 3 with the `pycryptodome` library (for `.py` and `.ipynb`)
- Jupyter to open the notebook
- Windows for the `.exe` executable

### 👤 Author

**Matteo** – [MatteoMgr2008](https://github.com/MatteoMgr2008)
