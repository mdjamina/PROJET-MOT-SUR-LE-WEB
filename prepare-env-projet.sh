#!/bin/bash

python3 -m pip install --upgrade pip >>prepare-env-projet.log 

python3 -m pip install -r requirements.txt >>prepare-env-projet.log 




python3 <<EOF >>prepare-env-projet.log 2>&1
#!/bin/python3
import nltk
nltk.download('punkt')

EOF

echo "creation des répertoires du projet ..."

mkdir -p ./CONTEXTES;
mkdir -p ./CONTEXTES;
mkdir -p ./DUMP-TEXT;
mkdir -p ./IMAGES;
mkdir -p ./PAGES-ASPIREES;
mkdir -p ./PROGRAMMES;
mkdir -p ./TABLEAUX;
mkdir -p ./URLS;

echo "fin ..."

echo "------------"
tree .

