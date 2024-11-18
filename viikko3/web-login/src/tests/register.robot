*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Input Text  name=username  oikea
    Input Text  name=password  Toimiva123!
    Input Text  name=password_confirmation  Toimiva123!
    Click Button  Register
    Page Should Contain  Welcome

Register With Too Short Username And Valid Password
    Input Text  name=username  ab
    Input Text  name=password  Toimiva123!
    Input Text  name=password_confirmation  Toimiva123!
    Click Button  Register
    Page Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Text  name=username  oikea
    Input Text  name=password  short
    Input Text  name=password_confirmation  short
    Click Button  Register
    Page Should Contain  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Input Text  name=username  oikea
    Input Text  name=password  password
    Input Text  name=password_confirmation  password
    Click Button  Register
    Page Should Contain  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Input Text  name=username  oikea
    Input Text  name=password  Toimiva123!
    Input Text  name=password_confirmation  Toimiva123
    Click Button  Register
    Page Should Contain  Passwords do not match

Register With Username That Is Already In Use
    Create User  oikea  Toimiva123!
    Go To  ${REGISTER_URL}
    Input Text  name=username  oikea
    Input Text  name=password  Toimiva123!
    Input Text  name=password_confirmation  Toimiva123!
    Click Button  Register
    Page Should Contain  already taken

Login After Successful Registration
    Input Text  name=username  uusi_kayttaja
    Input Text  name=password  Toimiva123!
    Input Text  name=password_confirmation  Toimiva123!
    Click Button  Register
    Page Should Contain  Welcome

    Go To  ${HOME_URL}/ohtu
    Click Button  Logout

    Page Should Contain  Ohtu Application main page
    Set Username  uusi_kayttaja
    Set Password  Toimiva123!
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Input Text  name=username  uusi_kayttaja
    Input Text  name=password  lyhyt
    Input Text  name=password_confirmation  lyhyt
    Click Button  Register
    Page Should Contain  Password must be at least 8 characters long

    Go To  ${LOGIN_URL}
    Input Text  name=username  uusi_kayttaja
    Input Text  name=password  lyhyt
    Click Button  name=submit
    Page Should Contain  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  existinguser  Valid123!
    Go To  ${REGISTER_URL}
