import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y,%H_%M_%S')}.log"  #making a new log file with this format of name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) #checks if the given path exists i.e directory, if not create one 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #final logpath is made till the file 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s], %(lineno)d, %(name)s, %(levelname)s, %(message)s ",
    level=logging.INFO,   #only logs with level higher than INFO will be logged
)

