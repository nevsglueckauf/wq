# Container-Klasse für Web-Content
#
# AUTHOR Sven Schrodt
# SINCE 2025-11-05

# 3rd party libs
import datetime

class Namer:

    @staticmethod
    def fn_now(ext:str ='.csv') -> str:
        """ Generiert temp. File name mit aktuellen Datumsstempel

        """ 
        s = Namer.now()
        return 'uploads/' + s[:16].replace(' ', '_').replace(':', '').replace('-', '') + ext

    def now() -> str:
        return str(datetime.datetime.now())

