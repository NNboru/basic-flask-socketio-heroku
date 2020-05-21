# An absolute basic python3 flask flask-socketio app deployment on heroku.


### git - cloning this repo to your local computer (install git first)

```git clone https://github.com/NNboru/basic-flask-socketio-heroku.git
cd basic-flask-socketio-heroku
```



### heroku CLI (install heroku CLI first)

login to heroku
```heroku login```

create your app
```heroku create mera-pehla-app-12345```	_you can use your custom name_

deploying code to your app (ie. the code above)
```git push heroku master```
it will show link of your app - https://mera-pehla-app-12345.herokuapp.com

open by command shortcut
```heroku open```

view your logs
```heroku logs```



### other commands

view your active apps
```heroku apps```

destroying your app
```heroku apps:destroy mera-pehla-app-12345 -c mera-pehla-app-12345```

10 recent logs only (can be any number)
```heroku logs -10```

logs sent by your app only
```heroku logs --app```

view git-repo's linked to your git-remote
```git remote -v```

just in case you have any other app linked to your git-remote
```git remote remove heroku```
linking your app to your git-remote
```git remote add heroku https://git.heroku.com/mera-pehla-app-12345.git```

