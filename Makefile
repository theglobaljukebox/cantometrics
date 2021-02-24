
# install python venv and install python libraries
env:
	python3 -m venv env
	./env/bin/python3 ./env/bin/pip3 install -r requirements.txt

update: env
	./env/bin/python3 ./env/bin/pip3 install --upgrade -r requirements.txt


help:
	@printf "\nIf you are an authenticated user and you want to update the data from Google Drive, run: make download\n\n"
	@printf "To build the dataset into CLDF format, run: make process (currently not working)\n\n"
	@printf "To validate the dataset, run: make validate (currently not working)\n\n"

download: env
	@printf "Collecting data from google drive is only available to authenticated users."
	mkdir -p raw/
	./env/bin/python3 download_googledrive.py

process: env
	mkdir -p cldf/
	@printf "TODO: create alternative file with new codings"
	@printf "convert data to long format to make compatible with CLDF framework"
	./env/bin/python3 to_long.py
	cp raw/societies.csv cldf/
	cp raw/songs.csv cldf/
	./env/bin/python3 rename_andsubset.py


test: env
	./env/bin/cldf validate ./cldf/StructureDataset-metadata.json 2>&1 | tee cldf.log
	#./env/bin/python3 -m pytest

# clean:
# 	rm -rf raw/

