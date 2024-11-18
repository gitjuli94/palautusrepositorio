*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Counter setting with text input value works
    Go To  ${HOME_URL}
    Input Text  name=arvo  10
    Click Button  aseta
    Page Should Contain  nappia painettu 10 kertaa

