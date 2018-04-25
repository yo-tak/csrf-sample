# csrf-sample
A sample project to support hands-on learning about CSRF attack.
Under `attack-target` is a non-secure EC service, and under `attacker` is an easy page to successfully attack `csrf-sample` service, and create a fraud purchase transaction for the user.

## basic operations
### how to start attack-target
```
cd ./attack-target
pip install -r requirements.txt
python manager.py
```

### create DB and initial data
```
python
>>> from app.models.model_def import init
>>> init()
>>> from app.models.model_def import Accounts, db
>>> user = Accounts(username='admin', password='password')
>>> db.session.add(user)
>>> db.session.commit()
>>> Accounts.query.all()
```

### how to start attacker
```
cd ./attacker
python server.py
```

## How to proceed CSRF attack
1. Have player1 start `attack-target` server, and login with any user.
2. Have player2 start `attacker` server.
3. Get url for dummy.html of `attacker` server(it should be like `<ip>:8000/dummy.html`),
  and open the page in player1's browser.
4. Have player1 click "Purchase" button.
5. Attack done!
