#!/bin/bash

source ../venv/bin/activate
coverage run -m unittest -v && coverage report -m