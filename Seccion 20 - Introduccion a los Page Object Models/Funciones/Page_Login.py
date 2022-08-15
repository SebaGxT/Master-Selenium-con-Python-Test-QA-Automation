import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE
from Funciones.funciones import Funciones_Globales as FG

class Page_Login():

    def __init__(self,driver):
        self.driver = driver
    
    def Login_Master(self,url,XN,name,XC,clave,XB,t):
        Fun = FG(self.driver)
        Fun.navegar2(url,t)
        Fun.texto_Xpath_Valida(XN,name,t)
        Fun.texto_Xpath_Valida(XC,clave,t)
        Fun.Click_Xpath_Valida(XB,t)
