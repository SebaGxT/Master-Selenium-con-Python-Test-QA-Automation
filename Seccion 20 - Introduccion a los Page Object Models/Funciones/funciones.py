import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE

class Funciones_Globales():

    def __init__(self,driver):
        self.driver = driver
    
    def driverCh():
        ops = webdriver.ChromeOptions()
        ops.add_argument('--start-maximized')
        driver=webdriver.Chrome(chrome_options=ops)
        return driver

    def saludos(self):
        print('Bienvenido a Page Object Model')
    
    def Tiempo(self,tiempo):
        t = time.sleep(tiempo)
        return t

    def navegar(self,url):
        self.driver.get(url)
        print(f'Pagina abierta: {url}')
    
    def navegar2(self,url,tiempo):
        self.driver.get(url)
        print(f'Pagina abierta: {url}')
        Funciones_Globales.Tiempo(self,tiempo)

    def texto_Xpath(self,xpath,text,tiempo):
        val = self.driver.find_element(By.XPATH,xpath)
        val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val.clear()
        val.send_keys(text)
        print(f'Escribiendo en el campo {xpath} el texto: {text}')
        Funciones_Globales.Tiempo(self,tiempo)
    
    def texto_ID(self,Id,text,tiempo):
        val = self.driver.find_element(By.ID,Id)
        val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val.clear()
        val.send_keys(text)
        print(f'Escribiendo en el campo {Id} el texto: {text}')
        Funciones_Globales.Tiempo(self,tiempo)

    def texto_Xpath_Valida(self,xpath,text,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val.clear()
            val.send_keys(text)
            print(f'Escribiendo en el campo {xpath} el texto: {text}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
    
    def texto_ID_Valida(self,Id,text,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val.clear()
            val.send_keys(text)
            print(f'Escribiendo en el campo {Id} el texto: {text}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)
    
    def Click_Xpath_Valida(self,xpath,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val.click()
            print(f'Se da click en el elemento {xpath}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
    
    def Click_ID_Valida(self,Id,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val.click()
            print(f'Se da click en el elemento {Id}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)
    
    def Select_Lista_Xpath_Valida(self,xpath,op,sel,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val = Select(val)
            try:
                op = str.lower(op)
                if op == "text":
                    val.select_by_visible_text(sel)
                    print(f'Opcion de la lista {xpath} seleccionada por texto: {sel}')
                elif op == "value":
                    val.select_by_value(sel)
                    print(f'Opcion de la lista {xpath} seleccionada por valor: {sel}')
                elif op == "index":
                    val.select_by_index(sel)
                    print(f'Opcion de la lista {xpath} seleccionada por indice: {sel}')
                else:
                    print(f'El valor {op} ingresado no corresponde a una accion valida. Debe ingresar como parametro /"text/" - /"value/" - /"index/"')
            except TOE as toe:
                print(toe.msg)
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
        
    def Select_Lista_Id_Valida(self,Id,op,sel,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val = Select(val)
            try:
                op = str.lower(op)
                if op == "text":
                    val.select_by_visible_text(sel)
                    print(f'Opcion de la lista {Id} seleccionada por texto: {sel}')
                elif op == "value":
                    val.select_by_value(sel)
                    print(f'Opcion de la lista {Id} seleccionada por valor: {sel}')
                elif op == "index":
                    val.select_by_index(sel)
                    print(f'Opcion de la lista {Id} seleccionada por indice: {sel}')
                else:
                    print(f'El valor {op} ingresado no corresponde a una accion valida. Debe ingresar como parametro /"text/" - /"value/" - /"index/"')
            except TOE as toe:
                print(toe.msg)
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)

    def Upload_File_Xpath_Valida(self,xpath,url,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val.send_keys(url)
            print(f'Se cargo el archivo {url} en el elemento {xpath}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
    
    def Upload_File_Id_Valida(self,Id,url,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val.send_keys(url)
            print(f'Se cargo el archivo {url} en el elemento {Id}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)

    def CheckBox_RadioButton_Xpath_Valida(self,xpath,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val.click()
            print(f'Se selecciono el elemento {xpath}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
    
    def CheckBox_RadioButton_Id_Valida(self,Id,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val.click()
            print(f'Se selecciono el elemento {Id}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)

    def CheckBoxMul_RadioButton_Xpath_Valida(self,xpath,cantI,cantF,tiempo):
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
                                xpath2 = str(xpath + "[" + str(n) + "]")
                                Funciones_Globales.CheckBox_RadioButton_Xpath_Valida(self,xpath2,tiempo)
                        except TOE as toe:
                            print(toe.msg)
                            print('No se enconto el elemento' + xpath)
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
    
    def texto_Mixto(self,tipo,selector,text,tiempo):
        if tipo == 'xpath':
            tipo = By.XPATH
        elif tipo == 'id':
            tipo = By.ID
        val = self.driver.find_element(tipo,selector)
        val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val.clear()
        val.send_keys(text)
        print(f'Escribiendo en el campo {selector} el texto: {text}')
        Funciones_Globales.Tiempo(self,tiempo)

    def texto_Mixto_Valida(self,tipo,selector,text,tiempo):
        if tipo == 'xpath':
            tipo = By.XPATH
        elif tipo == 'id':
            tipo = By.ID
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((tipo,selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(tipo,selector)
            val.clear()
            val.send_keys(text)
            print(f'Escribiendo en el campo {selector} el texto: {text}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + selector)

    def Click_Mixto_Valida(self,tipo,selector,tiempo):
        if tipo == 'xpath':
            tipo = By.XPATH
        elif tipo == 'id':
            tipo = By.ID
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((tipo,selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(tipo,selector)
            val.click()
            print(f'Se da click en el elemento {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + selector)
    
    def Select_Lista_Mixto_Valida(self,tipo,selector,op,sel,tiempo):
        if tipo == 'xpath':
            tipo = By.XPATH
        elif tipo == 'id':
            tipo = By.ID
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((tipo,selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(tipo,selector)
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
            print('No se enconto el elemento' + selector)
        
    def Upload_File_Mixto_Valida(self,tipo,selector,url,tiempo):
        if tipo == 'xpath':
            tipo = By.XPATH
        elif tipo == 'id':
            tipo = By.ID
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((tipo,selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(tipo,selector)
            val.send_keys(url)
            print(f'Se cargo el archivo {url} en el elemento {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + selector)

    def CheckBox_RadioButton_Mixto_Valida(self,tipo,selector,tiempo):
        if tipo == 'xpath':
            tipo = By.XPATH
        elif tipo == 'id':
            tipo = By.ID
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((tipo,selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(tipo,selector)
            val.click()
            print(f'Se selecciono el elemento {selector}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + selector)
    
    def CheckBoxMul_RadioButton_Mixto_Valida(self,tipo,selector,cantI,cantF,tiempo):
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
                                Funciones_Globales.CheckBox_RadioButton_Mixto_Valida(self,tipo,selector2,tiempo)
                        except TOE as toe:
                            print(toe.msg)
                            print('No se enconto el elemento' + selector)
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