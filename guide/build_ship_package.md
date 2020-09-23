# README
## Setup Virtual Environment
Se devi fare delle prove, falle sempre in un virtual environment che puoi cancellare.
Ecco come si fa:
- crea una nuova directory, esempio: mkdir test
- cd test
- python -m venv test_env crea il virtual environment
- .\test_env\Scripts\activate per attivarlo sotto Windows
- adesso puoi fare tutte le prove che vuoi.
- per uscire dal virtual environment scrivi deactivate

## Package your package
Quando il tuo Python package ha la struttura giusta e pensi sia ora di distribuirlo 
ecco cosa devi fare:
- attiva il virtual environment
- pip install setuptools, wheel se non ce li hai
- spostati nella cartella che contiene il file setup.py

da qui hai due scelte

1. python setup.py sdist

Crea una distribuzione non compilata del tuo pacchetto. Si trova in un file tarball.

2. python setup.py bdist_wheel

Crea una versione compilata del pacchetto. Si trova in un file .whl

Per verificare di riuscire a installare il pacchetto puoi entrare nella nuova cartella dist:
- cd dist
- da qui fare pip install pacchetto

