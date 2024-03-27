# Voyage d'Aff'air - Dataviz Application

M2 TNAH group project - Application for highlighting data concerning the travel of French Presidents and Prime Ministers, from 1945 to the present day.

## Pour démarrer notre application, suivez les étapes ci-dessous :

1. **Ouvrir le premier terminal**
    - **Sous macOS ou Linux** : Utiliser le raccourci `Ctrl+Alt+T` (sous Linux) ou `Cmd+Space` pour ouvrir Spotlight, puis taper `Terminal` et appuyer sur `Entrée` (sous macOS).
    - **Sous Windows** : Appuyer sur `Win+R`, taper `cmd` et appuyer sur `Entrée` pour ouvrir l'invite de commande, ou taper `powershell` pour ouvrir PowerShell.

    *Créer et activer un environnement virtuel :*
    ```bash
    virtualenv env -p python3
    source env/bin/activate
    ```

    *Installer les dépendances pour dashapp :*
    ```bash
    pip install dash
    pip install plotly
    ```

    *Démarrer dashapp :*
    ```bash
    cd dashapp
    python app.py
    ```

2. **Ouvrir un nouveau terminal**
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
