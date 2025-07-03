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

### Cron Jobs
- Create a cron job

    ```bash
    crontab -e
    ```

    ```bash
    0 8 * * * /bin/bash /user/owen/FreeGame-Scraper/automated.sh
    ```

- View cron jobs

    ```bash
    crontab -l
    ```

- Remove all cron jobs

    ```bash
    crontab -r
    ```

    Or you can type `crontab -e` again to remove the cron job