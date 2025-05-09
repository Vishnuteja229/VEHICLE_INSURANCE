import sys
import logging

def error_messsage_detail(error:Exception,error_detail:sys)->str:
    _,_,exc_tb =error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_messsage=f"Error occured in pyhton script [{file_name}] at line number[{line_number}: {str(error)}]"
    
    logging.error(error_messsage)
    return error_messsage

class MyException(Exception):
    def __init__(self,error_message: str,error_detail: sys):
        super().__init__(error_message)
        self.error_message=error_messsage_detail(error_message,error_detail)
        
    def __str__(self)-> str:
        return self.error_message     
    