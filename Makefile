process: parse generate pdf

parse:
	python parse_jds.py

generate:
	python generate.py

pdf:
	python make_pdf.py -a

black:
	black -l 86 $$(find * -name '*.py')
