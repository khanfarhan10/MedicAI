   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:35:59] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Jan/2021 17:36:06] "GET / HTTP/1.1" 200 -

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:36:54] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Jan/2021 17:37:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Jan/2021 17:39:49] "GET / HTTP/1.1" 200 -

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:40:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Jan/2021 17:40:34] "GET / HTTP/1.1" 200 -

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:40:47] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
Traceback (most recent call last):
  File "C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp\FlaskApplication.py", line 61, in <module>
    app.add_url_rule('/favicon.ico',
  File "C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\lib\site-packages\flask\helpers.py", line 307, in url_for
    "Attempted to generate a URL without the application context being"
RuntimeError: Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:42:48] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
  File "C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp\FlaskApplication.py", line 64
    redirect_to=)
                ^
SyntaxError: invalid syntax

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
Traceback (most recent call last):
  File "FlaskApplication.py", line 61, in <module>
    favicon_link = url_for('assets', filename='favicon.ico')
  File "C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\lib\site-packages\flask\helpers.py", line 307, in url_for
    "Attempted to generate a URL without the application context being"
RuntimeError: Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:44:22] "GET / HTTP/1.1" 200 -
Traceback (most recent call last):
  File "C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp\FlaskApplication.py", line 64, in <module>
    favicon_link = url_for('assets', filename='favicon.ico')
  File "C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\lib\site-packages\flask\helpers.py", line 307, in url_for
    "Attempted to generate a URL without the application context being"
RuntimeError: Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.
Traceback (most recent call last):
  File "FlaskApplication.py", line 64, in <module>
    favicon_link = url_for('assets', filename='favicon.ico')
  File "C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\lib\site-packages\flask\helpers.py", line 307, in url_for
    "Attempted to generate a URL without the application context being"
RuntimeError: Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
Traceback (most recent call last):
  File "FlaskApplication.py", line 20, in <module>
    favicon_link = url_for('assets', filename='favicon.ico')
  File "C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\lib\site-packages\flask\helpers.py", line 307, in url_for
    "Attempted to generate a URL without the application context being"
RuntimeError: Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:45:27] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:47:11] "GET / HTTP/1.1" 200 -
Traceback (most recent call last):
  File "C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp\FlaskApplication.py", line 71, in <module>
    favicon_link = url_for('assets', filename='favicon.ico')
  File "C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\lib\site-packages\flask\helpers.py", line 307, in url_for
    "Attempted to generate a URL without the application context being"
RuntimeError: Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.
Traceback (most recent call last):
  File "FlaskApplication.py", line 64, in <module>
    if __name__ == "__main__":
  File "C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\lib\site-packages\flask\helpers.py", line 307, in url_for
    "Attempted to generate a URL without the application context being"
RuntimeError: Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>python FlaskApplication.py
C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp
 * Serving Flask app "FlaskApplication" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [10/Jan/2021 17:49:01] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\farha\\Documents\\GitHub\\MedicAI\\WebsiteFiles\\FlaskApp\\FlaskApplication.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-248-335
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>pip list
Package      Version
------------ -------
click        7.1.2
Flask        1.1.1
itsdangerous 1.1.0
Jinja2       2.11.2
lxml         4.6.2
MarkupSafe   1.1.1
pip          20.2.4
pypng        0.0.20
PyQRCode     1.2.1
python-docx  0.8.10
setuptools   51.0.0
Werkzeug     1.0.1
wheel        0.35.1
WARNING: You are using pip version 20.2.4; however, version 20.3.3 is available.
You should consider upgrading via the 'C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\Scripts\python.exe -m pip install --upgrade pip' command.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>cd ..

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles>cd ..

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI>pip install -r reqs.txt
Requirement already satisfied: python-docx==0.8.10 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from -r reqs.txt (line 1)) (0.8.10)
Requirement already satisfied: Flask==1.1.1 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from -r reqs.txt (line 4)) (1.1.1)
Requirement already satisfied: PyQRCode==1.2.1 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from -r reqs.txt (line 5)) (1.2.1)
Requirement already satisfied: pypng==0.0.20 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from -r reqs.txt (line 6)) (0.0.20)
Collecting gunicorn==20.0.4
  Using cached gunicorn-20.0.4-py2.py3-none-any.whl (77 kB)
Requirement already satisfied: lxml>=2.3.2 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from python-docx==0.8.10->-r reqs.txt (line 1)) (4.6.2)
Requirement already satisfied: click>=5.1 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from Flask==1.1.1->-r reqs.txt (line 4)) (7.1.2)
Requirement already satisfied: Jinja2>=2.10.1 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from Flask==1.1.1->-r reqs.txt (line 4)) (2.11.2)
Requirement already satisfied: itsdangerous>=0.24 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from Flask==1.1.1->-r reqs.txt (line 4)) (1.1.0)
Requirement already satisfied: Werkzeug>=0.15 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from Flask==1.1.1->-r reqs.txt (line 4)) (1.0.1)
Requirement already satisfied: setuptools>=3.0 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from gunicorn==20.0.4->-r reqs.txt (line 7)) (51.0.0)    
Requirement already satisfied: MarkupSafe>=0.23 in c:\users\farha\documents\github\medicai\medicaienv\lib\site-packages (from Jinja2>=2.10.1->Flask==1.1.1->-r reqs.txt (line 4)) (1.1.1)
Installing collected packages: gunicorn
Successfully installed gunicorn-20.0.4
WARNING: You are using pip version 20.2.4; however, version 20.3.3 is available.
You should consider upgrading via the 'C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\Scripts\python.exe -m pip install --upgrade pip' command.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI>pip list
Package      Version
------------ -------
click        7.1.2
Flask        1.1.1
gunicorn     20.0.4
itsdangerous 1.1.0
Jinja2       2.11.2
lxml         4.6.2
MarkupSafe   1.1.1
pip          20.2.4
pypng        0.0.20
PyQRCode     1.2.1
python-docx  0.8.10
setuptools   51.0.0
Werkzeug     1.0.1
wheel        0.35.1
WARNING: You are using pip version 20.2.4; however, version 20.3.3 is available.
You should consider upgrading via the 'C:\Users\farha\Documents\GitHub\MedicAI\MedicAIEnv\Scripts\python.exe -m pip install --upgrade pip' command.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI>cd WebsiteFiles/FlaskApp

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku login
 »   Warning: Our terms of service have changed: https://dashboard.heroku.com/terms-of-service
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/b181d0f0-4691-4ff2-a414-e2a89057b585?requestor=SFMyNTY.g2gDbQAAAA4xODIuNjYuMTM5LjExN24GAGzaR-x2AWIAAVGA.UBE2wY8ix8MUHGE-TDxdJSxpVE9RTjkz-64K62KNt9g
Logging in... done
Logged in as njrfarhandasilva10@gmail.com

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku create medicai-api-heroku
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
Creating ⬢ medicai-api-heroku... done
https://medicai-api-heroku.herokuapp.com/ | https://git.heroku.com/medicai-api-heroku.git

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku create medicai-api-heroku
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
Creating ⬢ medicai-api-heroku... !
 !    Name medicai-api-heroku is already taken

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>abcd
'abcd' is not recognized as an internal or external command,
operable program or batch file.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku create medicalai-api-heroku
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
Creating ⬢ medicalai-api-heroku... done
https://medicalai-api-heroku.herokuapp.com/ | https://git.heroku.com/medicalai-api-heroku.git

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git init
Initialized empty Git repository in C:/Users/farha/Documents/GitHub/MedicAI/WebsiteFiles/FlaskApp/.git/

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku git:remote -a FlaskApp
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
 »   Error: Couldn't find that app.
 »
 »   Error ID: not_found

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku git:remote -a medicai-api-heroku
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
set git remote heroku to https://git.heroku.com/medicai-api-heroku.git

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git remote heroku=https://git.heroku.com/medicai-api-heroku.git
error: Unknown subcommand: heroku=https://git.heroku.com/medicai-api-heroku.git
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku git:remote -a medicai-api-heroku
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
set git remote heroku to https://git.heroku.com/medicai-api-heroku.git

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git remote heroku
error: Unknown subcommand: heroku
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git remote https://git.heroku.com/medicai-api-heroku.git
error: Unknown subcommand: https://git.heroku.com/medicai-api-heroku.git
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git remote heroku https://git.heroku.com/medicai-api-heroku.git
error: Unknown subcommand: heroku
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git remote https://git.heroku.com/medicai-api-heroku.git
error: Unknown subcommand: https://git.heroku.com/medicai-api-heroku.git
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git add .

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git commit -m "My first commit"
[master (root-commit) aaf3ebe] My first commit
 246 files changed, 44420 insertions(+)
 create mode 100644 HerokuSteps.md
 create mode 100644 Procfile
 create mode 100644 app.py
 create mode 100644 assets/css/argon-design-system.css
 create mode 100644 assets/css/argon-design-system.css.map
 create mode 100644 assets/css/argon-design-system.min.css
 create mode 100644 assets/css/font-awesome.css
 create mode 100644 assets/css/nucleo-icons.css
 create mode 100644 assets/css/nucleo-svg.css
 create mode 100644 assets/demo/demo.css
 create mode 100644 assets/demo/demo.js
 create mode 100644 assets/favicon.ico
 create mode 100644 assets/fonts/FontAwesome.otf
 create mode 100644 assets/fonts/fontawesome-webfont.eot
 create mode 100644 assets/fonts/fontawesome-webfont.svg
 create mode 100644 assets/fonts/fontawesome-webfont.ttf
 create mode 100644 assets/fonts/fontawesome-webfont.woff
 create mode 100644 assets/fonts/fontawesome-webfont.woff2
 create mode 100644 assets/fonts/nucleo-icons.eot
 create mode 100644 assets/fonts/nucleo-icons.svg
 create mode 100644 assets/fonts/nucleo-icons.ttf
 create mode 100644 assets/fonts/nucleo-icons.woff
 create mode 100644 assets/fonts/nucleo-icons.woff2
 create mode 100644 assets/img/apple-icon.png
 create mode 100644 assets/img/brand/MedicAIFavicon.png
 create mode 100644 assets/img/brand/MedicAILOGO.png
 create mode 100644 assets/img/brand/MedicAILogo_Blue.png
 create mode 100644 assets/img/brand/MedicAILogo_Transparent.png
 create mode 100644 assets/img/brand/MedicAILogo_TransparentBig.png
 create mode 100644 assets/img/brand/TeamFKlogo.png
 create mode 100644 assets/img/brand/TeamMLXTREME.png
 create mode 100644 assets/img/brand/blue.png
 create mode 100644 assets/img/brand/creativetim-black-slim.png
 create mode 100644 assets/img/brand/creativetim-white-slim.png
 create mode 100644 assets/img/brand/white.png
 create mode 100644 assets/img/docs/computer-docs.jpg
 create mode 100644 assets/img/faces/alejandro-escamilla.jpg
 create mode 100644 assets/img/faces/ali-pazani.jpg
 create mode 100644 assets/img/faces/atikh.jpg
 create mode 100644 assets/img/faces/brooke-cagle.jpg
 create mode 100644 assets/img/faces/christian.jpg
 create mode 100644 assets/img/faces/fezbot.jpg
 create mode 100644 assets/img/faces/michael.jpg
 create mode 100644 assets/img/faces/team-1.jpg
 create mode 100644 assets/img/faces/team-2.jpg
 create mode 100644 assets/img/faces/team-3.jpg
 create mode 100644 assets/img/faces/team-4.jpg
 create mode 100644 assets/img/faces/team-5.jpg
 create mode 100644 assets/img/favicon.ico
 create mode 100644 assets/img/favicon.png
 create mode 100644 assets/img/github.svg
 create mode 100644 assets/img/google.svg
 create mode 100644 assets/img/icons/common/github.svg
 create mode 100644 assets/img/icons/common/google.svg
 create mode 100644 assets/img/icons/flags/AD.png
 create mode 100644 assets/img/icons/flags/AE.png
 create mode 100644 assets/img/icons/flags/AG.png
 create mode 100644 assets/img/icons/flags/AM.png
 create mode 100644 assets/img/icons/flags/AR.png
 create mode 100644 assets/img/icons/flags/AT.png
 create mode 100644 assets/img/icons/flags/AU.png
 create mode 100644 assets/img/icons/flags/BE.png
 create mode 100644 assets/img/icons/flags/BF.png
 create mode 100644 assets/img/icons/flags/BG.png
 create mode 100644 assets/img/icons/flags/BO.png
 create mode 100644 assets/img/icons/flags/BR.png
 create mode 100644 assets/img/icons/flags/CA.png
 create mode 100644 assets/img/icons/flags/CD.png
 create mode 100644 assets/img/icons/flags/CG.png
 create mode 100644 assets/img/icons/flags/CH.png
 create mode 100644 assets/img/icons/flags/CL.png
 create mode 100644 assets/img/icons/flags/CM.png
 create mode 100644 assets/img/icons/flags/CN.png
 create mode 100644 assets/img/icons/flags/CO.png
 create mode 100644 assets/img/icons/flags/CZ.png
 create mode 100644 assets/img/icons/flags/DE.png
 create mode 100644 assets/img/icons/flags/DJ.png
 create mode 100644 assets/img/icons/flags/DK.png
 create mode 100644 assets/img/icons/flags/DZ.png
 create mode 100644 assets/img/icons/flags/EE.png
 create mode 100644 assets/img/icons/flags/EG.png
 create mode 100644 assets/img/icons/flags/ES.png
 create mode 100644 assets/img/icons/flags/FI.png
 create mode 100644 assets/img/icons/flags/FR.png
 create mode 100644 assets/img/icons/flags/GA.png
 create mode 100644 assets/img/icons/flags/GB.png
 create mode 100644 assets/img/icons/flags/GM.png
 create mode 100644 assets/img/icons/flags/GT.png
 create mode 100644 assets/img/icons/flags/HN.png
 create mode 100644 assets/img/icons/flags/HT.png
 create mode 100644 assets/img/icons/flags/HU.png
 create mode 100644 assets/img/icons/flags/ID.png
 create mode 100644 assets/img/icons/flags/IE.png
 create mode 100644 assets/img/icons/flags/IL.png
 create mode 100644 assets/img/icons/flags/IN.png
 create mode 100644 assets/img/icons/flags/IQ.png
 create mode 100644 assets/img/icons/flags/IR.png
 create mode 100644 assets/img/icons/flags/IT.png
 create mode 100644 assets/img/icons/flags/JM.png
 create mode 100644 assets/img/icons/flags/JO.png
 create mode 100644 assets/img/icons/flags/JP.png
 create mode 100644 assets/img/icons/flags/KG.png
 create mode 100644 assets/img/icons/flags/KN.png
 create mode 100644 assets/img/icons/flags/KP.png
 create mode 100644 assets/img/icons/flags/KR.png
 create mode 100644 assets/img/icons/flags/KW.png
 create mode 100644 assets/img/icons/flags/KZ.png
 create mode 100644 assets/img/icons/flags/LA.png
 create mode 100644 assets/img/icons/flags/LB.png
 create mode 100644 assets/img/icons/flags/LC.png
 create mode 100644 assets/img/icons/flags/LS.png
 create mode 100644 assets/img/icons/flags/LU.png
 create mode 100644 assets/img/icons/flags/LV.png
 create mode 100644 assets/img/icons/flags/MG.png
 create mode 100644 assets/img/icons/flags/MK.png
 create mode 100644 assets/img/icons/flags/ML.png
 create mode 100644 assets/img/icons/flags/MM.png
 create mode 100644 assets/img/icons/flags/MT.png
 create mode 100644 assets/img/icons/flags/MX.png
 create mode 100644 assets/img/icons/flags/NA.png
 create mode 100644 assets/img/icons/flags/NE.png
 create mode 100644 assets/img/icons/flags/NG.png
 create mode 100644 assets/img/icons/flags/NI.png
 create mode 100644 assets/img/icons/flags/NL.png
 create mode 100644 assets/img/icons/flags/NO.png
 create mode 100644 assets/img/icons/flags/OM.png
 create mode 100644 assets/img/icons/flags/PA.png
 create mode 100644 assets/img/icons/flags/PE.png
 create mode 100644 assets/img/icons/flags/PG.png
 create mode 100644 assets/img/icons/flags/PK.png
 create mode 100644 assets/img/icons/flags/PL.png
 create mode 100644 assets/img/icons/flags/PT.png
 create mode 100644 assets/img/icons/flags/PY.png
 create mode 100644 assets/img/icons/flags/QA.png
 create mode 100644 assets/img/icons/flags/RO.png
 create mode 100644 assets/img/icons/flags/RU.png
 create mode 100644 assets/img/icons/flags/RW.png
 create mode 100644 assets/img/icons/flags/SA.png
 create mode 100644 assets/img/icons/flags/SE.png
 create mode 100644 assets/img/icons/flags/SG.png
 create mode 100644 assets/img/icons/flags/SL.png
 create mode 100644 assets/img/icons/flags/SN.png
 create mode 100644 assets/img/icons/flags/SO.png
 create mode 100644 assets/img/icons/flags/SV.png
 create mode 100644 assets/img/icons/flags/TD.png
 create mode 100644 assets/img/icons/flags/TJ.png
 create mode 100644 assets/img/icons/flags/TL.png
 create mode 100644 assets/img/icons/flags/TR.png
 create mode 100644 assets/img/icons/flags/TZ.png
 create mode 100644 assets/img/icons/flags/UA.png
 create mode 100644 assets/img/icons/flags/US.png
 create mode 100644 assets/img/icons/flags/VE.png
 create mode 100644 assets/img/icons/flags/VN.png
 create mode 100644 assets/img/icons/flags/YE.png
 create mode 100644 assets/img/ill/1.svg
 create mode 100644 assets/img/ill/ill.png
 create mode 100644 assets/img/logo.png
 create mode 100644 assets/img/nucleo-logo.svg
 create mode 100644 assets/img/pages/mohamed.jpg
 create mode 100644 assets/img/theme/img-1-1200x1000.jpg
 create mode 100644 assets/img/theme/img-2-1200x1000.jpg
 create mode 100644 assets/img/theme/landing.jpg
 create mode 100644 assets/img/theme/profile.jpg
 create mode 100644 assets/js/argon-design-system.js
 create mode 100644 assets/js/argon-design-system.js.map
 create mode 100644 assets/js/argon-design-system.min.js
 create mode 100644 assets/js/core/bootstrap.min.js
 create mode 100644 assets/js/core/jquery.min.js
 create mode 100644 assets/js/core/popper.min.js
 create mode 100644 assets/js/plugins/bootstrap-datepicker.min.js
 create mode 100644 assets/js/plugins/bootstrap-switch.js
 create mode 100644 assets/js/plugins/chartjs.min.js
 create mode 100644 assets/js/plugins/datetimepicker.js
 create mode 100644 assets/js/plugins/jquery.sharrre.min.js
 create mode 100644 assets/js/plugins/moment.min.js
 create mode 100644 assets/js/plugins/nouislider.min.js
 create mode 100644 assets/js/plugins/perfect-scrollbar.jquery.min.js
 create mode 100644 assets/scss/argon-design-system.scss
 create mode 100644 assets/scss/argon-design-system/accordion.scss
 create mode 100644 assets/scss/argon-design-system/alert.scss
 create mode 100644 assets/scss/argon-design-system/avatar.scss
 create mode 100644 assets/scss/argon-design-system/badge.scss
 create mode 100644 assets/scss/argon-design-system/buttons.scss
 create mode 100644 assets/scss/argon-design-system/card.scss
 create mode 100644 assets/scss/argon-design-system/carousel.scss
 create mode 100644 assets/scss/argon-design-system/close.scss
 create mode 100644 assets/scss/argon-design-system/content.scss
 create mode 100644 assets/scss/argon-design-system/custom-forms.scss
 create mode 100644 assets/scss/argon-design-system/docs.scss
 create mode 100644 assets/scss/argon-design-system/docs/clipboard-js.scss
 create mode 100644 assets/scss/argon-design-system/docs/component-examples.scss
 create mode 100644 assets/scss/argon-design-system/docs/content.scss
 create mode 100644 assets/scss/argon-design-system/docs/footer.scss
 create mode 100644 assets/scss/argon-design-system/docs/nav.scss
 create mode 100644 assets/scss/argon-design-system/docs/prism.scss
 create mode 100644 assets/scss/argon-design-system/docs/sidebar.scss
 create mode 100644 assets/scss/argon-design-system/docs/variables.scss
 create mode 100644 assets/scss/argon-design-system/dropdown.scss
 create mode 100644 assets/scss/argon-design-system/footer.scss
 create mode 100644 assets/scss/argon-design-system/forms.scss
 create mode 100644 assets/scss/argon-design-system/functions.scss
 create mode 100644 assets/scss/argon-design-system/global.scss
 create mode 100644 assets/scss/argon-design-system/grid.scss
 create mode 100644 assets/scss/argon-design-system/icons.scss
 create mode 100644 assets/scss/argon-design-system/input-group.scss
 create mode 100644 assets/scss/argon-design-system/kit-free.scss
 create mode 100644 assets/scss/argon-design-system/list-group.scss
 create mode 100644 assets/scss/argon-design-system/mixins.scss
 create mode 100644 assets/scss/argon-design-system/mixins/alert.scss
 create mode 100644 assets/scss/argon-design-system/mixins/background-variant.scss
 create mode 100644 assets/scss/argon-design-system/mixins/badge.scss
 create mode 100644 assets/scss/argon-design-system/mixins/buttons.scss
 create mode 100644 assets/scss/argon-design-system/mixins/forms.scss
 create mode 100644 assets/scss/argon-design-system/mixins/icon.scss
 create mode 100644 assets/scss/argon-design-system/mixins/modals.scss
 create mode 100644 assets/scss/argon-design-system/mixins/popover.scss
 create mode 100644 assets/scss/argon-design-system/modal.scss
 create mode 100644 assets/scss/argon-design-system/nav.scss
 create mode 100644 assets/scss/argon-design-system/navbar.scss
 create mode 100644 assets/scss/argon-design-system/pagination.scss
 create mode 100644 assets/scss/argon-design-system/popover.scss
 create mode 100644 assets/scss/argon-design-system/progress.scss
 create mode 100644 assets/scss/argon-design-system/reboot.scss
 create mode 100644 assets/scss/argon-design-system/section.scss
 create mode 100644 assets/scss/argon-design-system/separator.scss
 create mode 100644 assets/scss/argon-design-system/theme.scss
 create mode 100644 assets/scss/argon-design-system/type.scss
 create mode 100644 assets/scss/argon-design-system/utilities.scss
 create mode 100644 assets/scss/argon-design-system/utilities/backgrounds.scss
 create mode 100644 assets/scss/argon-design-system/utilities/floating.scss
 create mode 100644 assets/scss/argon-design-system/utilities/helper.scss
 create mode 100644 assets/scss/argon-design-system/utilities/position.scss
 create mode 100644 assets/scss/argon-design-system/utilities/shadows.scss
 create mode 100644 assets/scss/argon-design-system/utilities/sizing.scss
 create mode 100644 assets/scss/argon-design-system/utilities/spacing.scss
 create mode 100644 assets/scss/argon-design-system/utilities/text.scss
 create mode 100644 assets/scss/argon-design-system/utilities/transform.scss
 create mode 100644 assets/scss/argon-design-system/variables.scss
 create mode 100644 assets/scss/argon-design-system/vendor/_bootstrap-datepicker.scss
 create mode 100644 assets/scss/argon-design-system/vendor/datetimepicker.scss
 create mode 100644 assets/scss/argon-design-system/vendor/headroom.scss
 create mode 100644 assets/scss/argon-design-system/vendor/nouislider.scss
 create mode 100644 assets/scss/argon-design-system/vendor/scrollbar.scss
 create mode 100644 assets/scss/argon-design-system/vendors.scss
 create mode 100644 favicon.ico
 create mode 100644 templates/homepage.html

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git remote -v
heroku  https://git.heroku.com/medicai-api-heroku.git (fetch)
heroku  https://git.heroku.com/medicai-api-heroku.git (push)

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku git:remote -a medicai-api-heroku
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
set git remote heroku to https://git.heroku.com/medicai-api-heroku.git

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git remote rename heroku heroku-staging

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku master
fatal: 'heroku' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]    
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]       
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku-staging master
Enumerating objects: 268, done.
Counting objects: 100% (268/268), done.
Delta compression using up to 4 threads
Compressing objects: 100% (262/262), done.
Writing objects: 100% (268/268), 3.91 MiB | 341.00 KiB/s, done.
Total 268 (delta 98), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote:  !     No default language could be detected for this app.
remote:                         HINT: This occurs when Heroku cannot detect the buildpack to use for this application automatically.
remote:                         See https://devcenter.heroku.com/articles/buildpacks
remote:
remote:  !     Push failed
remote: Verifying deploy...
remote:
remote: !       Push rejected to medicai-api-heroku.
remote:
To https://git.heroku.com/medicai-api-heroku.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/medicai-api-heroku.git'

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku buildpacks:set heroku/python
 »   Warning: heroku update available from 7.47.2 to 7.47.7.
Buildpack set. Next release on medicai-api-heroku will use heroku/python.
Run git push heroku main to create a new release using this buildpack.

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku main
error: src refspec main does not match any
error: failed to push some refs to 'heroku'

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku-staging master
Enumerating objects: 268, done.
Counting objects: 100% (268/268), done.
Delta compression using up to 4 threads
Compressing objects: 100% (262/262), done.
Writing objects: 100% (268/268), 3.91 MiB | 495.00 KiB/s, done.
Total 268 (delta 98), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote:
remote:  !     Push failed
remote:  !
remote:  ! ## Warning - The same version of this code has already been built: aaf3ebec69ce7371b6254e1eccf8df143b6b9d88
remote:  !
remote:  ! We have detected that you have triggered a build from source code with version aaf3ebec69ce7371b6254e1eccf8df143b6b9d88
remote:  ! at least twice. One common cause of this behavior is attempting to deploy code from a different branch.
remote:  !
remote:  ! If you are developing on a branch and deploying via git you must run:
remote:  !
remote:  !     git push heroku <branchname>:main
remote:  !
remote:  ! This article goes into details on the behavior:
remote:  !   https://devcenter.heroku.com/articles/duplicate-build-version
remote:
remote: Verifying deploy...
remote:
remote: !       Push rejected to medicai-api-heroku.
remote:
To https://git.heroku.com/medicai-api-heroku.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/medicai-api-heroku.git'

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HerokuSteps.md

no changes added to commit (use "git add" and/or "git commit -a")

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git add .

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   HerokuSteps.md


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git commit -m "Changed Somethings"
[master 2b66a29] Changed Somethings
 1 file changed, 552 insertions(+)

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku-staging master
Enumerating objects: 271, done.
Counting objects: 100% (271/271), done.
Delta compression using up to 4 threads
Compressing objects: 100% (265/265), done.
Writing objects: 100% (271/271), 3.92 MiB | 287.00 KiB/s, done.
Total 271 (delta 99), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote:
remote:  !     Push failed
remote: Verifying deploy...
remote:
remote: !       Push rejected to medicai-api-heroku.
remote:
To https://git.heroku.com/medicai-api-heroku.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/medicai-api-heroku.git'

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku-staging master
Enumerating objects: 271, done.
Counting objects: 100% (271/271), done.
Delta compression using up to 4 threads
Compressing objects: 100% (265/265), done.
Writing objects: 100% (271/271), 3.92 MiB | 307.00 KiB/s, done.
Total 271 (delta 99), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote:
remote:  !     Push failed
remote:  !
remote:  ! ## Warning - The same version of this code has already been built: 2b66a293a4fb0cf265e2a4cf6690ab5e70e20346
remote:  !
remote:  ! We have detected that you have triggered a build from source code with version 2b66a293a4fb0cf265e2a4cf6690ab5e70e20346
remote:  ! at least twice. One common cause of this behavior is attempting to deploy code from a different branch.
remote:  !
remote:  ! If you are developing on a branch and deploying via git you must run:
remote:  !
remote:  !     git push heroku <branchname>:main
remote:  !
remote:  ! This article goes into details on the behavior:
remote:  !   https://devcenter.heroku.com/articles/duplicate-build-version
remote:
remote: Verifying deploy...
remote:
remote: !       Push rejected to medicai-api-heroku.
remote:
To https://git.heroku.com/medicai-api-heroku.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/medicai-api-heroku.git'

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git add .

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   requirements.txt


(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku-staging master
Enumerating objects: 271, done.
Counting objects: 100% (271/271), done.
Delta compression using up to 4 threads
Compressing objects: 100% (265/265), done.
Writing objects: 100% (271/271), 3.92 MiB | 304.00 KiB/s, done.
Total 271 (delta 99), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote:
remote:  !     Push failed
remote:  !
remote:  ! ## Warning - The same version of this code has already been built: 2b66a293a4fb0cf265e2a4cf6690ab5e70e20346
remote:  !
remote:  ! We have detected that you have triggered a build from source code with version 2b66a293a4fb0cf265e2a4cf6690ab5e70e20346
remote:  ! at least twice. One common cause of this behavior is attempting to deploy code from a different branch.
remote:  !
remote:  ! If you are developing on a branch and deploying via git you must run:
remote:  !
remote:  !     git push heroku <branchname>:main
remote:  !
remote:  ! This article goes into details on the behavior:
remote:  !   https://devcenter.heroku.com/articles/duplicate-build-version
remote:
remote: Verifying deploy...
remote:
remote: !       Push rejected to medicai-api-heroku.
remote:
To https://git.heroku.com/medicai-api-heroku.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/medicai-api-heroku.git'

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>heroku update
heroku: Updating CLI from 7.47.2 to 7.47.7... done
heroku: Updating CLI... done

(MedicAIEnv) C:\Users\farha\Documents\GitHub\MedicAI\WebsiteFiles\FlaskApp>git push heroku-staging master
Enumerating objects: 271, done.
Counting objects: 100% (271/271), done.
Delta compression using up to 4 threads
Compressing objects: 100% (265/265), done.
Writing objects: 100% (271/271), 3.92 MiB | 242.00 KiB/s, done.
Total 271 (delta 99), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote:
remote:  !     Push failed
remote:  !
remote:  ! ## Warning - The same version of this code has already been built: 2b66a293a4fb0cf265e2a4cf6690ab5e70e20346
remote:  !
remote:  ! We have detected that you have triggered a build from source code with version 2b66a293a4fb0cf265e2a4cf6690ab5e70e20346
remote:  ! at least twice. One common cause of this behavior is attempting to deploy code from a different branch.
remote:  !
remote:  ! If you are developing on a branch and deploying via git you must run:
remote:  !
remote:  !     git push heroku <branchname>:main
remote:  !
remote:  ! This article goes into details on the behavior:
remote:  !   https://devcenter.heroku.com/articles/duplicate-build-version
remote:
remote: Verifying deploy...
remote:
remote: !       Push rejected to medicai-api-heroku.
remote:
To https://git.heroku.com/medicai-api-heroku.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/medicai-api-heroku.git'