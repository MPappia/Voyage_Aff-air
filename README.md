# Voyage d'Aff'air - Dataviz Application

M2 TNAH group project - Application for highlighting data concerning the travel of French Presidents and Prime Ministers, from 1945 to the present day.

## Pour démarrer notre application, suivez les étapes ci-dessous :

1.**Configuration de la base de données**
    - Dans le fichier app/__init__.py : 
        - ligne 15 : app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////[chemin absolu de la db]/Voyage_Aff-air/app/data/db_intern1.db'
            - Remplacer chemin absolu de la base de donnée en réalisant un clique droit, copier le chemin, sur la base de données dans le fichier data de app.

2. **Ouvrir le premier terminal**
    - **Sous macOS ou Linux** : Utilisez le raccourci `Ctrl+Alt+T` (sous Linux) ou `Cmd+Space` pour ouvrir Spotlight, puis tapez `Terminal` et appuyez sur `Entrée` (sous macOS).
    - **Sous Windows** : Appuyez sur `Win+R`, tapez `cmd` et appuyez sur `Entrée` pour ouvrir l'invite de commande, ou tapez `powershell` pour ouvrir PowerShell.

    *Créer et activer un environnement virtuel :*
    ```bash
    virtualenv env -p python3
    source env/bin/activate
    ```

    *Installer les dépendances pour dashapp :*
    ```bash
    pip install dash
    pip install plotly
    pip install pandas
    ```

    *Démarrer dashapp :*
    ```bash
    cd dashapp
    python app.py
    ```

3. **Ouvrir un nouveau terminal**
    Pour ouvrir un nouveau terminal, les instructions varient en fonction de votre système d'exploitation :

    - **Sous macOS** : Faites un clic droit sur l'icône du terminal dans le dock, puis sélectionnez « Nouvelle fenêtre » pour ouvrir un nouveau terminal.
    - **Sur VSCode** : Allez dans `Terminal` -> `Nouveau terminal` pour ouvrir un nouveau terminal.

    *Créer et activer un environnement virtuel :*
    ```bash
    virtualenv env -p python3
    source env/bin/activate
    ```

    *Installer les dépendances :*
    ```bash
    pip install flask
    pip install flask_sqlalchemy
    pip install flask_migrate
    pip install flask_login
    pip install flask_admin
    pip install flask_wtf
    pip install flask_paginate
    pip install pandas
    pip install plotly
    ```

    *Démarrer l'application :*
    ```bash
    python3 run.py
    ```
