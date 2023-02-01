env:
	python3 -m venv env || (rm -rf $@ && false)

env/package_stamp.txt: requirements.txt | env
	env/bin/pip install --upgrade pip setuptools wheel
	env/bin/pip install -r requirements.txt
	touch $@

env/dl.stamp: env/package_stamp.txt
	./env/bin/python -m spacy download en_core_web_md
	touch $@

run: env/package_stamp.txt env/dl.stamp
	./env/bin/python main.py
