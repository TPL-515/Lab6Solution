from dagster import Definitions, load_assets_from_modules
from lab6.assets import dataingest
from lab6.assets import modeltrain
from lab6.jobs import *

assets = load_assets_from_modules([dataingest, modeltrain])

defs = Definitions(
    assets=assets,
    jobs = [generate_data_job, remove_data_job, train_static_model_job, train_recurring_model_job, compare_model_job],
    schedules = [generate_data_job_schedule, recurring_model_train_schedule, compare_model_job_schedule]
)