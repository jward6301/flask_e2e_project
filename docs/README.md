# flask_e2e_project
HHA 504 Final Assignment

## Web service:
* My web service provides datasets from NYC regarding pregancy morbidity and mortality
* All info was downloaded from https://catalog.data.gov/dataset
* Once the webiste is opened, you are brought to the index page. Then there are 4 tabs, about, morbidity, mortality and additional info. About explains what the website is. The morbidity and mortality tabs reflect the data from csv files that were downlaoded from https://catalog.data.gov/dataset. Additional infor provides information about Pregnancy Risk Assessment Monitoring System (PRAMS).


## Technologies Used:
- Github (Version Control)
- Flask (Python; Frotend & Backend)
- MySQL (Database via Azure)
- SQLAlchemy (ORM)
- .ENV (Environment Variables)
- Tailwind (Frontend Styling)
- API Service (Flask Backend)
- Sentry.io (Debugging & Logging)
- Docker (Containerization)
- Azure (Deployment)

## Steps to run your web service if someone wanted to either run locally or deploy to the cloud
1. How could they run it without Docker locally?
    - First clone the repo and paste it into your terminal using ` git clone https://github.com/jward6301/flask_e2e_project.git`
    - In the `app` folder, add a `.env` file and copy the format of my .env in the .env template section below. Fill it in with your information
    - Install any dependencies that aren't already installed. Depedning on the device or terminal it may be different, but if using Google cloud shell, use `pip install`
    - Once everyhing is installed and the .env file is updated, redirect to ~/flask_e2e_project/app$ in the terminal
    - Type `python app.py` into the terminal. Click on the following link that will generate in your terminal `http://127.0.0.1:5001`. 
2. How could they run it with Docker locally?
    - First clone the repo and paste it into your terminal using ` git clone https://github.com/jward6301/flask_e2e_project.git`, if this wasn't done already. Also follow the next two steps under running without Docker.
    - In the `app` folder, ensure there are `Dockerfile` and `docker-compose.yml` files.
    - In the terminal, redirect to ~/flask_e2e_project/app$ 
    - In the terminal, type `docker-compose build` to build the images.
    - Next, type `docker-compose up` to run them.
    - Then, type in `docker run -p 5001:5001 <name of image>`
        - If intereseted in changing the ports, ensure they are changed in the `docker-compose.yml` as well.
    - Type type `docker-compose ps` in the terminal to view a list of all images.
    - To view the docker image, click Web Preview and change the port to the port entered in previous commands. Click change and preview and your image will de displayed. 
3. How could they deploy it to the cloud?
    - If the following steps were already followed, please skip them:
         - First clone the repo and paste it into your terminal using ` git clone https://github.com/jward6301/flask_e2e_project.git`
         - In the `app` folder, add a `.env` file and copy the format of my .env in the .env template section below. Fill it in with your information
         - Install any dependencies that aren't already installed. Depedning on the device or terminal it may be different, but if using Google cloud shell, use `pip install`
         - In the terminal, redirect to ~/flask_e2e_project/app$ 
    - Type in `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash` to install Azure CLI
    - To log into Azure via authentification code, type `az login --use-device-code`. Follow the instructions that will appear
    - You will have to create a resource group. Type `az group create --name <create a resource group name> -- location eastus` into the terminal.
    - If you run into any issues, you can view my steps from a previous assignment here: https://github.com/jward6301/azure_flask_deployment or you can view instructions via the microsoft website here: https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app-for-app-service?tabs=web-app-flask
    - Now, you have to deploy the app. Type in the following command `az webapp --resource-group <groupname> --name <app-name> --runtime <PYTHON : 3.9 > --sku <B1>`. For example, one of my commands was `az webapp up --name Jessica-504-flask1 --runtime PYTHON:3.9 --sku B1`.
    - You can now view the webside through the link provided in the output from the command or to view mine, click on the following link: https://jessflaskappe2e.azurewebsites.net/. 


## Deployed API app: 
* https://jessicaflaske2e.azurewebsites.net/api/hello

## .env Template:

``````
DB_HOST=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
DB_PORT=
DB_CHARSET=
alembic.ini 
 - sqlalchemy.url was changed to reflect my url based off of mysql+mysqlconnector:
``````

## Sentry.io
- I was unsure how to add the logs of sentry.io to my cloud shell but I have attached screenshots of some of the logs here: https://github.com/jward6301/flask_e2e_project/tree/main/docs/Screenshots/Sentry.io
- My error test from the app.py is also in this file. (There is no logs folder due to this, it is all in the docs folder). 


