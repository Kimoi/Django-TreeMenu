
# Django TreeMenu Project

**Implementation of tree menu using Django's 
custom template tags functionality**

## 💪Built with
![Static Badge](https://img.shields.io/badge/Django-1?style=flat&logo=Django&labelColor=0c4b33&color=187f58&link=https%3A%2F%2Fwww.djangoproject.com%2F)
![Static Badge](https://img.shields.io/badge/Python-1?style=flat&logo=Python&labelColor=ffd847&color=3776ab&link=https%3A%2F%2Fwww.python.org%2F)
![Static Badge](https://img.shields.io/badge/PostgreSQL-1?style=flat&logo=PostgreSQL&labelColor=ffffff&color=336791&link=https%3A%2F%2Fwww.postgresql.org%2F)
![Static Badge](https://img.shields.io/badge/Docker-1?style=flat&logo=Docker&labelColor=ffffff&color=1d63ed&link=https%3A%2F%2Fwww.docker.com%2F)

## ✨Give it a try

*Expected to use **Bash** or similar shell alternatives*

<details><summary>Docker / PostgreSQL</summary>

</details>

<details><summary>Django / SQLite</summary>

clone repo >> generate .env >> edit (optional)

```bash
git clone https://github.com/Kimoi/Django-TreeMenu.git && \
cp env_example_sqlite .env && \
nano .env
```

<br>

Activate venv Linux / macOS

`python -m venv venv && source venv/bin/activate`

Activate venv Windows

```python -m venv venv && source venv/Scripts/activate```

<br>

requirements >> migrate >> populate db >> createsuperuser >> runserver

```bash
python -m pip install --upgrade pip && \
pip install -r requirements.txt && \
python manage.py migrate && \
python manage.py loaddata menu/sample_data.yaml && \
python manage.py createsuper && \
python manage.py runserver
```

### ⚡Example endpoints

*log: super / pas: super*

- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- [http://127.0.0.1:8000/menu/](http://127.0.0.1:8000/menu/)

### ⚠️Erase project

`deactivate && cd .. && rm -fr Django-TreeMenu`

</details>
