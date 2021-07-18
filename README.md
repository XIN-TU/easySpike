# Flask-VueJs-Template 🌶️✌

update

[![Build Status](https://travis-ci.org/gtalarico/flask-vuejs-template.svg?branch=master)](https://travis-ci.org/gtalarico/flask-vuejs-template)
[![codecov](https://codecov.io/gh/gtalarico/flask-vuejs-template/branch/master/graph/badge.svg)](https://codecov.io/gh/gtalarico/flask-vuejs-template)

_Flask + Vue.js Web Application Template_

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")


## Demo Access
[Live Demo](https://ttds-project.herokuapp.com/)

---
## API:
### Recipe Entry 定义：
以基于['id', 'time', 'comments', 'serving', 'Extra', 'calories', 'img_link', 'title', 'ingredients', 'instructions'] 为列的pandas Dataframe. **具体参见 app/api/func.py. 和output文件**


### 算法模块入口： app/api/engine.py

```
app/api/engine.py:

输入： 
- keywords -> String :: 用户于搜索框中输入的查询语句
- paras -> List ::用户勾选的高级搜索选项; 前端预定义 (Vegi, Quick&Easy, etc.)

输出：
- List<Dict> 基于pandas的json.load()结果；后端可以直接读取。
	* 生成语句：    
		result = data.to_json(orient='records')
    	parsed = json.loads(result)

```
*以上 data 为基于['id', 'title', 'content', 'time', 'comments', 'serving', 'Extra', 'calories', 'img_link', 'title', 'ingredients', 'instructions'] 为列的pandas Dataframe. **具体参见 app/api/func.py. 和output文件***


---
## Engine Version

**V1搜索引擎：**

数据来源：293条爬虫数据 （有效数据少于290条）， 从csv中直接读取

使用指南：
* 读取两个数字参数 INDEX STEP (中间空格分割)
* 不符合条件：默认为INDEX=0 STEP=10，输出同样的结果
* 符合条件: 输出第INDEX个起，STEP个结果

e.g., 1 2 returns item 1,2; 2 3 returns 2,3,4

\# Note because some entries are EMPTY, it could return fewer entries than STEP defined. 

---
---
## Features
* Minimal Flask 1.0 App
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* Starter [PyTest](http://pytest.org) test suite
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) + yarn
* [Vuex](https://vuex.vuejs.org/)
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://github.com/axios/axios/) for backend communication
* Sample Vue [Filters](https://vuejs.org/v2/guide/filters.html)
* Heroku Configuration with one-click deployment + Gunicorn





## Template Structure

The template uses Flask & Flask-RestPlus to create a minimal REST style API,
and let's VueJs + vue-cli handle the front end and asset pipline.
Data from the python server to the Vue application is passed by making Ajax requests.

### Application Structure

#### Rest Api

The Api is served using a Flask blueprint at `/api/` using Flask RestPlus class-based
resource routing.

#### Client Application

A Flask view is used to serve the `index.html` as an entry point into the Vue app at the endpoint `/`.

The template uses vue-cli 3 and assumes Vue Cli & Webpack will manage front-end resources and assets, so it does overwrite template delimiter.

The Vue instance is preconfigured with Filters, Vue-Router, Vuex; each of these can easilly removed if they are not desired.

#### Important Files

| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/app`               | Flask Application                          |
| `/app/api`           | Flask Rest Api (`/api`)                    |
| `/app/client.py`     | Flask Client (`/`)                         |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point (`/`)         |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build` |


## Installation

##### Before you start

Before getting started, you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv (optional)
- [X] Heroku Cli (if deploying to Heroku)

##### Template and Dependencies

* Clone this repository:

	```
	$ git clone https://github.com/gtalarico/flask-vuejs-template.git
	```

* Setup virtual environment, install dependencies, and activate it:

	```
	$ pipenv install --dev
	$ pipenv shell
	```

* Install JS dependencies

	```
	$ yarn install
	```


## Development Server

Run Flask Api development server:

```
$ python run.py
```

From another tab in the same directory, start the webpack dev server:

```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Flask Api
and static files will be served from `localhost:5000`.

The dual dev-server setup allows you to take advantage of
webpack's development server with hot module replacement.

Proxy config in `vue.config.js` is used to route the requests
back to Flask's Api on port 5000.

If you would rather run a single dev server, you can run Flask's
development server only on `:5000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python run.py
```


## Production Server

This template is configured to work with Heroku + Gunicorn and it's pre-configured
to have Heroku build the application before releasing it.

#### JS Build Process

Heroku's nodejs buidlpack will handle install for all the dependencies from the `packages.json` file.
It will then trigger the `postinstall` command which calls `yarn build`.
This will create the bundled `dist` folder which will be served by whitenoise.

#### Python Build Process

The python buildpack will detect the `Pipfile` and install all the python dependencies.

#### Production Sever Setup

Here are the commands we need to run to get things setup on the Heroku side:

	```
	$ heroku apps:create flask-vuejs-template-demo
	$ heroku git:remote --app flask-vuejs-template-demo
	$ heroku buildpacks:add --index 1 heroku/nodejs
	$ heroku buildpacks:add --index 2 heroku/python
	$ heroku config:set FLASK_ENV=production
	$ heroku config:set FLASK_SECRET=SuperSecretKey

	$ git push heroku
	```

### Heroku deployment - One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gtalarico/flask-vuejs-template)


# First use:
'''
1. yarn upgrade
2. yarn install 
3. yarn serve
4. 
'''

