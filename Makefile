# Define the default target
.DEFAULT_GOAL=make
VENV=venv
PYTHON=python3
DIR=venv/bin/activate
Sou=source

# Define the target for building the project
.PHONY: make
make:
    $(PYTHON) -m $(VENV) venv && \
    $(Sou) $(DIR)


# Define the target for cleaning the project
.PHONY: clean
clean:
      rm -r $(VENV)
