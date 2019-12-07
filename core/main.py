# @Author  : GentleCP
# @Email   : 574881148@qq.com
# @File    : main.py
# @Item    : PyCharm
# @Time    : 2019/11/28/028 14:00
# @WebSite : https://www.gentlecp.com

import logging
import time

from core.source import Downloader,BackToMain,GradeObserver
from core.wifi import WifiLoginer,WifiError
import settings

WELCOME_MESSAGE = """
*********************************************************************************
**      #   #   ###     #       ###    #  #   ###  #     ###    ###  ####      **
**      #   #  #       # #     #       #  #  #     #     #  #  #     #   #     **
**      #   #  #      #   #    ####    ####  ###   #     ###   ###   ####      **
**      #   #  #     #######      #    #  #  #     #     #     #     #  #      **
**       ###    ### ##     ##  ###     #  #   ###  ##### #      ###  #   #     **
**                            copyright@GentleCP                               **
**                            website:https://www.gentlecp.com                 **
**                            1:course sources download                        **
**                            2:wifi login                                     **
**                            3:wifi logout                                    **
**                            4:view grades                                    **
**                            5:exit                                           **
*********************************************************************************
"""


class Init:
    """
    用于检查一切配置信息是否合理正确
    """

    def __init__(self,
                 welcome_msg,
                 wifi_loginer=None,
                 downloader=None,
                 observer=None
                 ):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s:[%(message)s]')
        self._logger = logging.getLogger("Init")
        self._welcome_msg = welcome_msg
        self._wifi_loginer = wifi_loginer
        self._downloader = downloader
        self._observer = observer

    def _show_welcome(self):
        print(self._welcome_msg)

    def _cmd(self):
        while True:
            time.sleep(0.1)
            option = input("输入你的操作：")
            if not (option.isdigit() and 1<=int(option)<=4) :
                self._logger.warning("非法操作，请重新输入")
            else:
                option = int(option)
                if option == 1:
                    try:
                        self._downloader.run()
                    except BackToMain:
                        pass

                elif option == 2:
                    try:
                        self._wifi_loginer.login()
                    except WifiError:
                        pass

                elif option == 3:
                    try:
                        self._wifi_loginer.logout()
                    except WifiError:
                        pass
                elif option == 4:
                    self._observer.run()
                elif option == 5:
                    print("欢迎使用，下次再会~")
                    exit(1)


    def run(self):
        self._show_welcome()
        self._cmd()


def main():
    wifi_loginer = WifiLoginer(accounts_path=settings.ACCOUNTS_PATH)
    downloader = Downloader(user_info=settings.USER_INFO,
                            urls=settings.URLS,
                            source_dir=settings.SOURCE_DIR)
    observer = GradeObserver(user_info=settings.USER_INFO,urls=settings.URLS)
    init = Init(WELCOME_MESSAGE, wifi_loginer, downloader,observer)
    init.run()


if __name__ == "__main__":
    main()