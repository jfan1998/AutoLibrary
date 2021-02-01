# AutoLibrary
- DSC180B A04 G03 - Capstone Project (Winter 2021)
- Note: This is an application of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

## Docker
- The docker repository is jfan1998/dsc180a-docker.
- Note: The docker uses dsmlp base container. Please login to a dsmlp jumpbox before entering the command below.
```
launch-scipy-ml.sh -i jfan1998/dsc180a-docker:latest
```

## Default Run
```
python run.py
```
### Target 1: Convert the input .pdf file into .txt
```
python run.py data
```
### Target 2: Run AutoPhrase on the input file
```
python run.py autophrase
```
### Target 3: Apply weight to the quality scores of phrases according the corresponding quality score in its domain
```
python run.py weight
```
### Target 4: Web Scraping
```
python run.py webscrape
```
### Target 5: Activating the website
```
python run.py website
```
The local website is hosted on `http://127.0.0.1:8000/autolibrary/`

## TBC-->
### Target 5: Run Report 
- Note: 
  - This report is futher exploration on AutoPhrase results. Paper report link is stored in references.
  - Report requires manual labeling high-quality phrases. The result CSV file for DBLP.txt is stored in references directory and the result CSV file for test_raw.txt is stored in test directory.
- The writings in the output html file explain and investigate AutoPhrase results of DBLP.txt dataset. Only look the graphs/tables if you use another dataset.
```
python run.py report
```
### Target 6: Test All previous targets on test data
Note: For the test run, raw test data is in test/testdata directory.
```
python run.py test
```
### Target 7: Run All the targets
```
python run.py all
```

## Responsbilities: 
