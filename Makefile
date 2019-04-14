test-all:
	@ echo '- removing old data'
	@ rm -f -R tests/db/
	@ echo '- creating new tests/db/ (required for tests)'
	@ mkdir -p tests/db/
	@ pytest --cov-report term-missing --cov=. tests/