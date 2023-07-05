```
conda create -p venv python=3.8 -y
```
```
source activate ./venv
```
```
git init
```
```
touch .gitignore
```
add venv to .gitignore
```
touch README.md
```
add steps to README.md
```
touch requirements.txt
```
add required libraries to requirements.txt
```
pip install -r requirements.txt
```
```
dvc init
```
```
touch dvc.yaml
```
update dvc.yaml file
```
dvc repro
```
```
dvc dag
```
```
dvc add <filename>
```
```
git add <filename> && git commit -m "message"
```
```
dvc remote add -d myremote <any remote location>
```
```
dvc push
```
```
dvc pull
```
dvc documentation https://dvc.org/doc 


