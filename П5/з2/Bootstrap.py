import config
from MainApp import MainApp


class Bootstrap():

    @staticmethod
    def initEnviroment():
        config.mainApp = MainApp()


    @staticmethod
    def run():
        config.mainApp.mainloop()