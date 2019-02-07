collection="mytest123"

dep:
	pip install -r requirements.txt

run:
	python3 main.py

coll:
	python3 rekker/make_collection.py --collection-id $(collection)
