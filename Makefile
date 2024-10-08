.PHONY: build-image test linter up

PYTHON=.venv/bin/python
APPNAME=example_api
TESTDIR=./test
SRCDIR=./src

build-image:
	docker build -t "${APPNAME}"  -f ./docker/Dockerfile .

test:
	"${PYTHON}" -m pytest "${TESTDIR}"

linter:
	"${PYTHON}" -m flake8 "${SRCDIR}" "${TESTDIR}"

up:
	docker run -p 8000:8000 -d "${APPNAME}"
