COVID 19 ESTMATOR API

GETTING STARTED

INSTALL PYTHON  3.7

Follow the instructions to install the latest version of python for your platform in the (https://www.python.org/downloads/)

VIRTUAL ENVIRONMENT

We recommend working within a virtual environment whenever using python for projects. This keeps your dependencies for each project seperate and organised. Instructions for setting up a virtual environment for your platform can be found in the (https://docs.python.org/3/library/venv.html)
 
DEPENDENCIES

Install django ==>
django is a lightweight backend framework .Which is required to handle requests and responses.

install json==> 
This converts any data into a json format.

install dicttoxml ==>
This converts your json file or any other data into a xml format.

ENDPOINTS

Post category 

for json format ==> (127.0.0.1/v1/on-covid-19/json) 

for xml format ==> (127.0.0.1/v1/on-covid-19/xml) 

Accepts a get request

To get the logs ==> (127.0.0.1/v1/on-covid-19/log) 

So basically what the repo does is that when you get it all setup you use site such as postman to access the endpoints. Some of the endpoint in there is (127.0.0.1/v1/on-covid-19/json) which accepts a post request of a particular data format which is in the json format so here is a preview of the format you would input.

{
region: {
name: "Africa",
avgAge: 19.7,
avgDailyIncomeInUSD: 5,
avgDailyIncomePopulation: 0.71
},
periodType: "days",
timeToElapse: 58,
reportedCases: 674,
population: 66622705,
totalHospitalBeds: 1380614
}

When you input this kind of data in . It does a set of calculation and gives you the result of your calculations for the (IMPACT AND SEVERE-IMPACT-CASES) of the covid-19 cases.

Another endpoint is (127.0.0.1/v1/on-covid-19/xml) which practically does the same calculations with the right data and returns your output in xml format.
then all of these post is recorded in another endpoint called the (127.0.0.1/v1/on-covid-19/log) which stores all the requests sent.

   