# aiogram crypto bot

telegram bot for checking current cryptocurrencies(bitcoin, ethereum, solana) price and percentage price changing in periods(1h, 24h, 7d, 30d)

## how to run

- rename `.env.dist` to `.env` and fill in the appropriate fields

### pip

- install dependencies: `pip install -r requirements.txt`
- run `src/main.py`: `python src/main.py`

### poetry

- install poetry: `pip install poetry`
- install dependencies: `poetry install`
- run `src/main.py` in poetry venv: `poetry run python src/main.py`

### docker

- build image: `docker build . --tag {tag}`
- run image: `docker run {tag}`