from dagster import define_asset_job, ScheduleDefinition
from lab6.assets.dataingest import *
from lab6.assets.modeltrain import *

generate_data_job = define_asset_job(name="generate_data", selection=[create_demo_table, display_table_before, pull_data, ingest_data, display_table_after])
remove_data_job = define_asset_job(name="remove_data", selection=[clear_table])
train_static_model_job = define_asset_job(name="train_static_model", selection=[pull_data, train_static])
train_recurring_model_job = define_asset_job(name="train_recurring_model", selection=[pull_data, train_recurring])
compare_model_job = define_asset_job(name="compare_models_performance", selection=[pull_data, predict_static, predict_recurring, compare_models])


generate_data_job_schedule = ScheduleDefinition(
    job=generate_data_job,
    cron_schedule="* * * * *",  # every minute
)

recurring_model_train_schedule = ScheduleDefinition(
    job=train_recurring_model_job,
    cron_schedule="*/2 * * * *",  # every 2 minutes
)

compare_model_job_schedule = ScheduleDefinition(
    job=compare_model_job,
    cron_schedule="*/2 * * * *",  # every 2 minutes
)