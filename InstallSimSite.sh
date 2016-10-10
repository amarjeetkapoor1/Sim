echo "Enter DataBase User"
read user
echo -n Enter DataBase Password:
read -s pass
mysql -u$user -p$pass -e "create database Sim;"
cd  Sim_site
python manage.py makemigrations Sim
python manage.py migrate 

