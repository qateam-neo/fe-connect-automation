# from tkinter import messagebox
from functools import wraps
import logging
from helpers.alert_helper import AlertHelper
import sys

from utils.driver import get_driver

logger = logging.getLogger(__name__)

# NOTE The purpose of this decorator is to handle any exceptions that may occur during the execution of the decorated method and to present an alert to the user if necessary.
def handle_exceptions(func):
    # NOTE The wraps decorator is used to preserve the metadata of the original function, such as its name and documentation, in the decorated function.
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exception:
            # Todo: Present a popup or report or link it to testrail
            # NOTE args[0].__class__.__name__ is used to get the name of the class that caused the exception. 
            class_name = args[0].__class__.__name__
            # NOTE sys._getframe(1).f_code.co_name is used to get the name of the method that caused the exception
            calling_func_name = sys._getframe(1).f_code.co_name
            logger.error(f"Exception occurred in {class_name}.{calling_func_name}: {exception}", exc_info=True)       
            alert_helper = AlertHelper(get_driver())
            alert_text = alert_helper.switch_to_alert()
            if alert_text is not None:
                alert_helper.show_alert(alert_text)
            
            
    return wrapper
