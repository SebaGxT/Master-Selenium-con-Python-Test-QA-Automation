import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver import ActionChains as AC
from selenium.common.exceptions import TimeoutException as TOE


class Funciones_Globales():

    def __init__(self,driver):
        self.driver = driver
    
    def driverCh():
        ops = webdriver.ChromeOptions()
        ops.add_argument('--start-maximized')
        driver=webdriver.Chrome(chrome_options=ops)
        return driver
    
    def driverCh2():
        driver=webdriver.Chrome()
        driver.maximize_window()
        return driver
    
    def driverChexe(url):
        ops = webdriver.ChromeOptions()
        ops.add_argument('--start-maximized')
        driver=webdriver.Chrome(chrome_options=ops,executable_path=url)
        return driver
    
    def driverChexe2(url):
        driver=webdriver.Chrome(executable_path=url)
        driver.maximize_window()
        return driver
    
    def driverFi():
        driver=webdriver.Firefox()
        driver.maximize_window()
        return driver
    
    def driverFiexe(url):
        driver=webdriver.Firefox(executable_path=url)
        driver.maximize_window()
        return driver
    
    def Tiempo(self,tiempo=.2):
        t = time.sleep(tiempo)
        return t

    def navegar(self,url,tiempo=.2):
        self.driver.get(url)
        print(f'Pagina abierta: {url}')
        Funciones_Globales.Tiempo(self,tiempo)
    
    def definir_tipo(tipo):
        tipo = str.lower(tipo)
        if tipo == 'xpath':
            tipo = By.XPATH
        elif tipo == 'id':
            tipo = By.ID
        elif tipo == 'css' :
            tipo = By.CSS_SELECTOR
        elif tipo == 'tag':
            tipo = By.TAG_NAME
        elif tipo == 'class':
            tipo = By.CLASS_NAME
        elif tipo == 'name':
            tipo == By.NAME
        elif tipo == 'link':
            tipo = By.LINK_TEXT
        elif tipo == 'partial':
            tipo == By.PARTIAL_LINK_TEXT
        return tipo
    
    def validar_elemento(self,tipo,selector):
        val = WW(self.driver,5).until(EC.visibility_of_element_located((tipo,selector)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val = self.driver.find_element(tipo,selector)
        return val
    
    def validar_elemento_visible(self,tipo,selector,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            print(f'Se encontro el elemento {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
            val = True
        except TOE as toe:
            print(toe.msg)
            print(f'No se enconto el elemento: {selector}')
            val = False
        finally:
            return val
    
    def insertar_texto(self,tipo,selector,text,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            val.clear()
            val.send_keys(text)
            print(f'Escribiendo en el campo {selector} el texto: {text}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se enconto el elemento: {selector}')
    
    def insertar_texto_mul(self,dic,text,tiempo=.2): #REVISAR - debo ver la forma de agregar selectores y textos a uno o mas arrays para insertar a varios campos
        dic.tipo = Funciones_Globales.definir_tipo(dic.tipo)
        for i in dic:
            try:
                val = Funciones_Globales.validar_elemento(self,dic.tipo,dic.selector)
                val.clear()
                val.send_keys(text)
                print(f'Escribiendo en el campo {dic.selector} el texto: {text}')
                Funciones_Globales.Tiempo(self,tiempo)
            except TOE as toe:
                print(toe.msg)
                print(f'No se encontro el elemento: {dic.selector}')


    def Click_elemento(self,tipo,selector,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            val.click()
            print(f'Se da click en el elemento {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se enconto el elemento: {selector}')
    
    def Select_Lista(self,tipo,selector,op,sel,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            val = Select(val)
            try:
                op = str.lower(op)
                if op == "text":
                    val.select_by_visible_text(sel)
                    print(f'Opcion de la lista {selector} seleccionada por texto: {sel}')
                elif op == "value":
                    val.select_by_value(sel)
                    print(f'Opcion de la lista {selector} seleccionada por valor: {sel}')
                elif op == "index":
                    val.select_by_index(sel)
                    print(f'Opcion de la lista {selector} seleccionada por indice: {sel}')
                else:
                    print(f'El valor {op} ingresado no corresponde a una accion valida. Debe ingresar como parametro /"text/" - /"value/" - /"index/"')
            except TOE as toe:
                print(toe.msg)
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se encontro el elemento: {selector}')
        
    def Upload_File(self,tipo,selector,url,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            val.send_keys(url)
            print(f'Se cargo el archivo {url} en el elemento {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se encontro el elemento: {selector}')

    def CheckBox_RadioButton(self,tipo,selector,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            val.click()
            print(f'Se selecciono el elemento {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se encontro el elemento: {selector}')
    
    def CheckBoxMul_RadioButton(self,tipo,selector,cantI,cantF,tiempo=.2):
        try:
            if type(cantI) == str and type(cantF) == str:
                print('No se puede realizar el proceso debe ingresar al menos un parametro en inicio o fin')
            else:
                I = True
                F = True
                if type(cantI) == str:
                    if str.isnumeric(cantI):
                        cantF = int(cantI) + 1
                    else:
                        print(f'No es posible convertir {cantI} a int')
                        I = False
                if type(cantF) == str:
                    if str.isnumeric(cantF):
                        cantF = int(cantF) + 1
                    else:
                        print(f'No es posible convertir {cantF} a int')
                        F = False
                if I == True and F == True:
                    if cantI <= cantF:
                        try:
                            for n in range(cantI,cantF):
                                selector2 = str(selector + "[" + str(n) + "]")
                                Funciones_Globales.CheckBox_RadioButton(self,tipo,selector2,tiempo)
                        except TOE as toe:
                            print(toe.msg)
                            print(f'No se encontro el elemento: {selector}')
                    else:
                        print('No se puede realizar el proceso ya que cantF es menor a cantI')
                else:
                    if I == False:
                        print(f'El parametro {cantI} debe ser numerico')
                    if F == False:
                        print(f'El parametro {cantF} debe ser numerico')
        except TOE as toe:
            print(toe.msg)
            print('hubo un error')
    
    def doble_click_AC(self,tipo,selector,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            act = AC(self.driver)
            act.double_click(val).perform()
            print(f'Doble click en el elemento: {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se enconto el elemento: {selector}')
    
    def click_derecho_AC(self,tipo,selector,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            act = AC(self.driver)
            act.context_click(val).perform()
            print(f'Click derecho en el elemento: {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se enconto el elemento: {selector}')
    
    def click_AC(self,tipo,selector,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selector)
            act = AC(self.driver)
            act.click(val).perform()
            print(f'Click en el elemento: {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se enconto el elemento: {selector}')
    
    def DragDrop_AC(self,tipo,selectordrag,selectordrop,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,selectordrag)
            val2 = Funciones_Globales.validar_elemento(self,tipo,selectordrop)
            act = AC(self.driver)
            act.drag_and_drop(val,val2).perform()
            print(f'Se obtuvo el elemento {selectordrag} y se arrastro al campo: {selectordrop}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se encontro uno o varios de los elementos ')
    
    def DragDropXY_AC(self,tipo,selectordrag,x,y,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento_visible(self,tipo,selectordrag)
            if val:
                val = Funciones_Globales.validar_elemento(self,tipo,selectordrag)
            else:
                self.driver.switch_to.frame(0)
                val = Funciones_Globales.validar_elemento(self,tipo,selectordrag)
            act = AC(self.driver)
            act.drag_and_drop_by_offset(val,x,y).perform()
            print(f'Se obtuvo el elemento {selectordrag} y se arrastro a las coordenadas: {x} - {y}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se encontro el elemento: {selectordrag} ')
    
    def ClickXY_AC(self,x,y,tiempo=.2):
        try:
            act = AC(self.driver)
            act.move_by_offset(x,y).click().perform()
            print(f'Se clickeo en las coordenadas: {x} - {y}') 
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se pudo dar click en las coordenadas: {x} {y}')
    
    def Click_derechoXY_AC(self,x,y,tiempo=.2):
        try:
            act = AC(self.driver)
            act.move_by_offset(x,y).context_click().perform()
            print(f'Se dio click derecho en las coordenadas: {x} - {y}') 
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se pudo dar click derecho en las coordenadas: {x} {y}')
    
    def Doble_clickXY_AC(self,x,y,tiempo=.2):
        try:
            act = AC(self.driver)
            act.move_by_offset(x,y).context_click().perform()
            print(f'Se dio doble click en las coordenadas: {x} - {y}') 
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se pudo dar doble click en las coordenadas: {x} {y}')
    
    def copiar_pegar(self,tipo,copy,paste,tiempo=.2):
        tipo = Funciones_Globales.definir_tipo(tipo)
        try:
            val = Funciones_Globales.validar_elemento(self,tipo,copy)
            act = AC(self.driver)
            act.move_to_element(val).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
            print(f'Texto {val} copiado de elemento: {copy}')
            val = Funciones_Globales.validar_elemento(self,tipo,paste)
            act.move_to_element(val).click().key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            print(f'Texto {val} pegado en elemento: {paste}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print(f'No se encontro un elemento ')
    