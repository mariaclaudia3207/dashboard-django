<h1 align="center">Dashboard em Django</h1>


Dashboard contendo login, registro de usuário e tabela.

:small_blue_diamond: Passos de construção 

Tutorial em https://mkdev.me/posts/fundamentals-of-front-end-django

1 - Instalar python3 e Django na máquina

2 - Executar os seguintes comandos no terminal:
django-admin startproject dashboard
cd dashboard
python3 manage.py starapp core

3 - Adicionar 'core.apps.CoreConfig' em INSTALLED_APPSsettings.py

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

:small_blue_diamond: Modificações nos arquivos

1 - download do bootstrap em https://startbootstrap.com/template/sb-admin
2 - Anexar arquivos index e login.html em core/templates
3 - Adicionar visualização do index.html em views.py
4 - Adicionar rota em urls.py

5 - Adicionar em /core/static as pastas css, js e vendor e adicionar o caminho dos arquivos
em /static/ a index e login.html

6 - Adicionar rota para login.html em urls.py
7 - Adicionar uma view para login em views.py
