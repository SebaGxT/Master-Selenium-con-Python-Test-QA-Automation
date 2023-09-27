Feature: Nuestro Quinto Demo

Background: 
    Given Abriendo el navegador

Scenario Outline: Corriendo nuestro Quinto Test
    When Cargando el nombre del "<nombre>"
    Then Cargando su "<email>"
    Then Cargando la "<direccion>"
    Examples:
    | nombre | email | direccion |
    | nombre1 | email1@gmail.com | direccion1 |
    | nombre2 | email2@gmail.com | direccion2 |
    | nombre3 | email3@gmail.com | direccion3 |
    | nombre4 | email4@gmail.com | direccion4 |
    | nombre5 | email5@gmail.com | direccion5 |