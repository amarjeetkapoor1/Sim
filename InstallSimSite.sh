echo -n password:
read -s pass
mysql -u$1 -p$pass -e "create database Sim;"
cd  Sim_site
python manage.py makemigrations Sim
python manage.py migrate 

