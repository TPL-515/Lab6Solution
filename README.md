# Lab 6

For this lab we will be creating scheduled runs for our jobs and manipulating their run intervals.

## Getting Started

First clone the lab locally and install the dependencies like so:

```bash
git clone git@github.com:TPL-515/Lab6.git
cd Lab6/
pip install -e ".[dev]"
```

This should install all of the required dependencies for the lab.

## Running the Lab

In order to run the lab just run the following command:

```bash
dagster dev
```

From here you should be able to navigate to the UI hosted at: http://localhost:3000

## Lab Tasks

For this lab you will be asked to perform the following tasks

1) Look within the UI and notice that the "generate_data" and "remove_data" jobs have been added.

2) Look through the modeling/randomforest code and make sure you understand the methods that currently exist.

3) Write an asset called "train_static" that trains a model on the first 10 rows within the database

4) Write an asset called "predict_static" that makes predictions on the whole database using the model from train_static

5) Write an asset called "train_recurring" that trains a model on the whole database

6) Write an asset called "predict_recurring" that uses the model from train to make predictions on the data.

7) Write a job called "train_static_model_job" that trains the static model

8) Write a job called "train_recurring_model_job" that trains the recurring model.

9) Write a job called "compare_model_job" that compares the accuracy of the two models and logs it to the meta data.

10) Write a job schedule for the train_recurring_model_job that goes every 2 minutes

11) Write a job schedule for the compare_model_job that goes every 2 minutes.

12) After everything is configured materialize everything one by one starting with the generate_data, then the train_static and the train_recurring and ending with the compare_models

13) Turn on the schedule and notice how the metrics change over time.
