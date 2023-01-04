from Funciones_Globales.funciones import Funciones_Globales as FG


def setup_function(function):
    global dri
    global Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    Fun.insertar_texto('xpath',"//input[@id='Email']","admin@yourstore.com")
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin")
    Fun.Click_elemento('xpath',"//button[@type='submit']")

def teardown_function(function):
    dri.quit()

def test_catalogo_computer():
    Fun.Click_elemento('xpath',"(//p[contains(.,'Catalog')])[1]")
    Fun.Click_elemento('xpath',"(//p[contains(.,'Products')])[1]")
    Fun.insertar_texto('xpath',"//input[@id='SearchProductName']",'Computer')
    Fun.Click_elemento('xpath',"//button[@id='search-products']")
    Fun.Tiempo(3)

def test_catalogo_agregarprod():
    Fun.Click_elemento('xpath',"(//p[contains(.,'Catalog')])[1]")
    Fun.Click_elemento('xpath',"(//p[contains(.,'Products')])[1]")
    Fun.Click_elemento("xpath","//a[@href='/Admin/Product/Create']")
    if Fun.validar_elemento_visible("xpath","//div[@class='card-title'][contains(.,'Product info')]"):
        Fun.insertar_texto("xpath","//input[@id='Name']","memory ram")
        Fun.insertar_texto("xpath","//textarea[@id='ShortDescription']","Hyper5x Fury")
        dri.switch_to.frame(0)
        Fun.insertar_texto("id",'tinymce',"CCL 18 latency 4y 15 32 GB")
        dri.switch_to.default_content()
        Fun.insertar_texto("xpath","//input[@id='Sku']","352GB")
        Fun.click_AC("xpath","(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[1]")
        Fun.click_AC("xpath","(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
        Fun.click_AC("xpath","//li[@tabindex='-1'][contains(.,'HP')]")
        Fun.click_AC("xpath","(//div[contains(.,'Enter tags ...')])[9]")
        Fun.insertar_texto("xpath","//input[@maxlength='50']","Memory Ra66m")
        Fun.insertar_texto("xpath","//input[@id='Gtin']","12h3456")
        Fun.insertar_texto("xpath","//input[@id='ManufacturerPartNumber']","678u90")
        Fun.CheckBox_RadioButton("xpath","//input[@id='ShowOnHomepage']")
        Fun.insertar_texto("xpath","//input[contains(@id,'AvailableStartDateTimeUtc')]","11/20/2022")
        Fun.insertar_texto("xpath","//input[contains(@id,'AvailableEndDateTimeUtc')]","12/31/2022")
        Fun.insertar_texto("xpath","//textarea[contains(@id,'AdminComment')]","No Comments")
        Fun.CheckBox_RadioButton("xpath","//input[@id='AvailableForPreOrder']")
        Fun.insertar_texto("xpath","//input[@id='PreOrderAvailabilityStartDateTimeUtc']","11/5/2022")
        Fun.Select_Lista("id","TaxCategoryId","value","2")
        if Fun.validar_elemento_visible("xpath","//input[@id='IsShipEnabled']"):
            print("Elemento visible")
        else:
            Fun.click_AC("xpath","(//i[contains(@class,'fa toggle-icon fa-plus')])[1]")
        Fun.CheckBox_RadioButton("xpath","//input[@id='IsShipEnabled']")
        if Fun.validar_elemento_visible("xpath","//input[@id='SeName']"):
            print("Elemento visible")
        else:
            Fun.click_AC("xpath","(//button[@class='btn btn-tool'])[12]")
        Fun.insertar_texto("xpath","//input[@id='SeName']","Google12")
        Fun.insertar_texto("xpath","//input[@id='MetaTitle']","Memory Ram")
        Fun.insertar_texto("xpath","//input[@id='MetaKeywords']","Ram, access memory, memory, pc, components, hardware")
        Fun.insertar_texto("xpath","//textarea[@id='MetaDescription']","pc components hardware")
        Fun.click_AC("xpath","//a[@id='backTop']")
        Fun.Tiempo(5)
        Fun.click_AC("xpath","(//button[@type='submit'][contains(.,'Save')])[1]")
        if Fun.validar_elemento_visible("xpath","//div[contains(@class,'alert alert-success alert-dismissable')]"):
            print("Elemento agregado con exito")