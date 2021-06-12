# Heart Attack Prediction - SPA

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 12.0.4.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.

## Deploy

Create an account on [Heroku](https://signup.heroku.com/login), download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Execute command `heroku login` and enter credentials to login to Hiroku CLI.

Execute command `heroku create your-app-name` to create a new application. (https://your-app-name.hirokuapp.com will be your URL)

## Deploy cont.

![Deploy Animation](animations/animation-2.gif)

Now execute following commands one after the other. (change `your-app-name` in line 2 to the name you have given in the previous step)
```
git init
heroku git:remote -a your-app-name
git add .
git commit -m "initial commit"
git push heroku master
```
Last command will push your code to heroku platform and start deploying. Hereafter whenever you want to create a new build, just execute last 3 commands only, i.e.
```
git add .
git commit -m "initial commit"
git push heroku master
```

Optional command `heroku logs --tail` to view realtime logs of the deployement server.