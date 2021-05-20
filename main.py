from FMWJob import FMWJob
import sys

sys.path.append('../FMEServerLib')
from FileLogger.Logger import AppLogger
import os
import json

APP_CONFIG = "app.json"
SECRET_CONFIG = "secret.json"
JOB_CONFIG = "job.json"

with open(APP_CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
log = AppLogger(os.path.join(app_config["log_dir"], "log.txt"), True, True)
try:
    job = FMWJob(APP_CONFIG, SECRET_CONFIG, JOB_CONFIG)
    job.execute()
except Exception as e:
    log.write_line(e)
