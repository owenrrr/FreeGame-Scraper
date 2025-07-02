## Automated Fetch Steam Free Games Script

### Windows
```bash
# Use virtual env
python -m venv myvenv
.\myvenv\Scripts\activate

# install libraries
pip install -r requirements.txt

# install playwright-specific browsers
playwright install

# run
python .\fetch_v2.py

# quit virtual env
deactivate
```

### Linux/Mac OS
```bash
# Use virtual env
python -m venv myvenv
source myvenv/Scripts/activate

# install libraries
pip install -r requirements.txt

# install playwright-specific browsers
playwright install

# run
python fetch_v2.py

# quit virtual env
deactivate
```