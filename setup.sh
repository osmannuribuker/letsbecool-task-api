#!/bin/bash
# Colors
green=`tput setaf 2`
reset=`tput sgr0`

PROJECT=${letsbecool-api}

echo "${green}>>> Remove .venv${reset}"
rm -rf .venv

echo "${green}>>> Creating virtualenv${reset}"
python3 -m venv venv
echo "${green}>>> .venv is created.${reset}"

# active
sleep 2
echo "${green}>>> activate the .venv.${reset}"
source ./venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\033[00m$ "
sleep 2

# install requirements
echo "${green}>>> Installing the requirements${reset}"
pip3 install -r requirements.txt

# migrate
python manage.py makemigrations authentication
python manage.py makemigrations app
python manage.py migrate

# createuser
echo "${green}>>> Creating a 'admin' user ...${reset}"
echo "${green}>>> The password must contain at least 8 characters.${reset}"
echo "${green}>>> Password suggestions: djangoadmin${reset}"
python manage.py createsuperuser --username='admin' --email='admin@admin.com'


# tests
echo "${green}>>> Starting tests...${reset}"
python manage.py test core/apps/services/tests

sleep 2
echo "${green}>>> Done${reset}"
sleep 2

# run
python manage.py runserver