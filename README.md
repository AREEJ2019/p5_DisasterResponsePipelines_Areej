# p5_DisasterResponsePipelines_Areej
# Project: Disaster_Response_Pipelines

The idea of the project is to classify disaster response pipline messages by using machine learning.

## Table of Contents

<ul>
<li><a href="#Installation">Installation</a></li>
<li><a href="#Instructions">Instructions</a></li>
<li><a href="#File Description">File Description</a></li>
<li><a href="#Results">Results</a></li>
<li><a href="#Licensing, Authors, and Acknowledgements">Licensing, Authors, and Acknowledgements</a></li>
</ul>


<a id='Installation'></a>
# Installation
The code should run with no issues
<a id='Instructions'></a>

# Instructions
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
inter to cd app in directory
    `python run.py`

3. Go to http://0.0.0.0:3001/

4. open new terminal
       env|grep WORK
       https://WORKSPACEID-3001.WORKSPACEDOMAIN
       https://view6914b2f4-3001.udacity-student-workspaces.com/
       

  

<a id='File Description'></a>
# File Description

These are the following files I used to complete this analysis:
- Data folder that contains
  - process_data.py: reads in the data, cleans and stores it in a SQL database. 
  - disaster_messages.csv: csv disaster_messages(dataset)
  - disaster_categories.csv disaster_categories (dataset)
  - DisasterResponse.db: created database from transformed and cleaned data in process_data.py .
- Models folder that contains:
  - classifier.pkl:To run ML pipeline that trains classifier and saves the trained model to classifier.pkl
  - train_classifier.py: includes the code to load data, transform and run a machine learning model .
- app folder that contains:
  - run.py: Flask app and the user interface used to predict results and display them.
   templates: folder containing the html templates


