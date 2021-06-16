# Dev notes
    python -m venv .venv  
    .\.venv\Scripts\Activate.ps1  
    .venv\scripts\python.exe -m pip install --upgrade pip  
    pip install poetry  
    git init .  

*First commit here*

This project is a bit of an exploration of what poetry offers.


# Build
poetry build 

# Publish 
poetry publish


# Track 
poetry show --tree

poetry show --latest


# update poetry
poetry self update

pip list --outdated
pip list --outdated --format=freeze | ForEach { pip3 install -U $_.split("=")[0] }

