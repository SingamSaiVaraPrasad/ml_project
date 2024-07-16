import sys
from src.logger import logging
def error_name_display(error,error_detail:sys):
    _,_,exe_tb=error_detail.exc_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_msg="Error occured in script [{0}] in the line number [{1}] and err message is [{2}]".format(
        file_name,exe_tb.tb_lineno,str(error)
    )
    return error_msg
class custom_exception(Exception):
        def __init__(self,error_message,error_detail:sys):
              super().__init__(error_message)
              self.error_message=error_name_display(error_message,error_detail=error_detail)
        def __str__(self):
              return self.error_message              
