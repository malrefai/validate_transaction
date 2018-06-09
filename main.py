#############################################################################
#                                                                           #
#   main.py                                                                 #
#                                                                           #
#       Created on  :   Oct 24, 2016                                        #
#       Author      :   Mohammad F. Alrefai                                 #
#                                                                           #
#                                                                           #
#############################################################################

from datetime import datetime, timedelta

from markets.UAE.Dubai.Dubai import Dubai
from markets.UAE.Abudhabi.Abudhabi import Abudhabi


def main():
    """

    :return:
    """
    args = dict()
    # args['browser'] = 'googleChrome'
    args['user'] = 'mohd.alrefai@hotmail.com'
    args['password'] = 'bombom85'
    args['wait'] = 25
    args['print'] = True
    args['duration'] = 10
    args['database'] = 'sqlite'
    timeNow = datetime.utcnow()
    # args['first_day'] = timeNow.replace(hour=0, minute=0, second=0, microsecond=0)
    # args['last_day'] = timeNow.replace(hour=0, minute=0, second=0, microsecond=0)
    # args['start_time'] = timeNow.replace(hour=8, minute=45, second=0, microsecond=0)
    # args['end_time'] = timeNow.replace(hour=10, minute=0, second=0, microsecond=0)
    args['end_time'] = timeNow + timedelta(minutes=2)

    dubai = Dubai(args)
    dubai.start()

    # abudhabi = Abudhabi(args)
    # abudhabi.start()

    print('Good Bye !!!')

main()
