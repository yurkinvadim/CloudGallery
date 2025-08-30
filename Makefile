.PHONY: run
run:
	python manage.py runserver

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: test
test:
	python manage.py test

.PHONY: su
su:
	python manage.py createsuperuser

.PHONY: coverage
coverage:
	coverage run manage.py test
	coverage report

.PHONY: sort
sort:
	isort .

.PHONY: freeze
freeze:
	pip freeze > requirements.txt
