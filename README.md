# Cours Python de Dimitri Merejkowsky

Ce dépôt contient les sources de mon cours de programmation sur Python, disponible
à l'adresse suivante:

https://dmerej.info/python

## Contribuer

Si vous trouvez des erreurs dans le cours ou avez des idées d'amélioration, vous pouvez:

* Ouvrir un ticket sur https://todo.sr.ht/~dmerej/python-course

* Envoyer des correctifs sur https://lists.sr.ht/~dmerej/cours-python -
  voir https://git-send-email.io/ pour les instructions.

* Ou bien me contacter directement : https://dmerej.info/blog/fr/pages/about

En tout cas, toute contribution, même minime, est la bienvenue !

Note: si jamais git-send-email ne fonctionne pas chez vous, vous pouvez utiser le mirror GitHub pour faire une pull request : https://github.com/dmerejkowsky/cours-python

## Génération du code html et du pdf

```
poetry install
poetry run python build.py --help
```

