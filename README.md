# Install instructions
## Docker
Du trenger følgene programmer installert:
* docker
* docker-compose

1. `git clone git@gitlab.stud.idi.ntnu.no:programvareutvikling-v19/gruppe-37.git pu && cd pu`
2. `docker-compose up -d`

## Uten docker (for Winodws)
Du trenger følgene programmer intallert:
* Python
* pip
1. `git clone git@gitlab.stud.idi.ntnu.no:programvareutvikling-v19/gruppe-37.git pu && cd pu`
2. `python3 -m venv venv & source venv/bin/activate`
3. `pip install -r requirements.txt && cd src`
4. `flask run`

# Andre kommandoer
`docker-compose exec flask pytest` kjører testene, eller `pytest` hvis du kjører appen utenfor docker

[Git cheatsheet](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-37/wikis/Git-cheatsheet)

# Gruppe 37
TODO: Masse greier
TODO: Putte inn i wiki: https://sethrobertson.github.io/GitBestPractices/
