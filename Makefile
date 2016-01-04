test:
	@echo "Run the real tests.";
	@py.test --cov-report term-missing --cov=tldr/ --pep8 -vs tests/ tldr/;

create:
	@python setup.py sdist bdist_wheel

upload:
	@python setup.py sdist bdist_wheel upload
