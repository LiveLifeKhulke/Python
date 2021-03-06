import inspect
import logging
# # #
# import logging
# #
# import pytest
# # #
# # #
# @pytest.mark.usefixtures("setup")
# # #
# class BaseClass:
#     def getlogger(self):
#         loggername = inspect.stack()[1][3]
#         logger = logging.getLogger(loggername)
#         filehandler = logging.FileHandler('logging.log')
#         formatter= logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
#         filehandler.setFormatter(formatter)
#         logger.addHandler(filehandler)
#         logger.setLevel(logging.DEBUG)
#         return logger
import pytest

#
@pytest.mark.usefixtures("setup")
#
class BaseClass:
    def getlogger(self):
        loggername=inspect.stack()[1][3]
        logger=logging.getLogger(loggername)
        filehandler=logging.FileHandler('logging1.log')
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
