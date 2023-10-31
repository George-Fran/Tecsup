# Inatalar dependencias
pip install -r requirements.txt

# Run Migration
python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate