Setup:
- `pip install -r requirements.txt`
- `pip install fastapi[standard]`

Quick test:
- `fastapi dev main.py`
- Open browser and visit http://127.0.0.1:8000 to verify server is working.
- Visit http://127.0.0.1:8000/get_stock_winners.

About this repository:
- `requirements.txt` was generated using `pipreqs`
- The CSV database (see the sample in the sample_data folder) is assumed to have the columns `Date`, `Kod`, and `Kurs`.
- Python Modules used are
	- `pandas` for CSV data operations
	- `fastapi` for lightweight REST API
	- `pytest` for test-driven development

TODO (2025-04-02):
- Write tests using pytest
- Decide how to deploy application