## Automated Fetch Steam Free Games Script
A lighteight script to grab steam free games from SteamDB. You can integrate the script within your pipeline/cron jobs.


### Installation: Windows
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

### Installation: Linux/Mac OS
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

### Be aware
Currently, `fetch_v3.py` is the stable one.