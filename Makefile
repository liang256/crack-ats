parse:
	python parse_jds.py

generate:
	python generate.py

pdf:
	python make_pdf.py

black:
	black -l 86 $$(find * -name '*.py')
