*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
When counter has a nonzero value and it is reset the value becomes zero
   Go To  ${HOME_URL}
   Click Button  Paina
   Click Button  Nollaa
   Page Should Contain  nappia painettu 0 kertaa

When textinput is given new value is updated
   Go To  ${HOME_URL}
   Click Button  Nollaa
   Input Text  aseta  10
   Page Should Contain  nappia painettu 0 kertaa

