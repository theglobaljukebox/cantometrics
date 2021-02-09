
# install python venv and install python libraries
env:
	python3 -m venv env
	./env/bin/python3 ./env/bin/pip3 install -r requirements.txt

update: env
	./env/bin/python3 ./env/bin/pip3 install --upgrade -r requirements.txt

download: env
	@echo Collecting data from google drive is only available to authenticated users. 
	mkdir -p raw/
	./env/bin/python3 download_googledrive.py

process:

tests:
	./env/bin/python3 -m pytest

clean:
	rm -rf raw/

