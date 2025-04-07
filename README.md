Setup:
- `pip install -r requirements.txt`
- `pip install fastapi[standard]`
- `pip install --no-deps pipreqs`
- `pip install yarg==0.1.9 docopt==0.6.2`

Quick local test:
- Run `fastapi dev` from the root repo directory.
- Open browser and visit http://127.0.0.1:8000 to verify server is working.
- Visit http://127.0.0.1:8000/get_stock_winners for API.

Running pytests:
- Run `pytest -vv` from the root repo directory.

About this repository:
- `requirements.txt` was generated using `pipreqs`
- The CSV database (see the sample in the sample_data folder) is assumed to have the columns `Date`, `Kod`, and `Kurs`.
- Python Modules used are
	- `pandas` for CSV data operations
	- `fastapi` for lightweight REST API
	- `pytest` for test-driven development

TODO (2025-04-07):
- Decide how to deploy application
- How to properly configure csv databse? Test context vs production