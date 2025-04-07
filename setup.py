from setuptools import setup, find_packages

setup(
    name='YT-HourGen',  # Le nom de ton projet
    version='0.1',  # Version initiale
    packages=find_packages(),  # Pour inclure tous les packages dans le répertoire
    install_requires=[  # Les dépendances nécessaires
        'pytube',  # Exemple, tu peux ajouter ici toutes les dépendances listées dans requirements.txt
        'moviepy',
    ],
    entry_points={  # Permet de définir une commande dans le terminal
        'console_scripts': [
            'yt-hourgen=main:main',  # Cette ligne permet d'exécuter `yt-hourgen` depuis le terminal
        ],
    },
    include_package_data=True,  # Permet d'inclure les fichiers supplémentaires (comme assets)
)
