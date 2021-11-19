*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username must be at least three letters

Register With Valid Username And Too Short Password
    Set Username  kallee
    Set Password  kallee
    Set Password Confirmation  kalle
    Click Button  Register
    Register Should Fail With Message  Password must contain at least 8 letters and numbers

egister With Nonmatching Password And Password Confirmation
    Set Username  kallee
    Set Password  kalle1233
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click Button  Register
    Register Should Succeed
    Go To Main Page
    Front Page Should Be Open
    Click Link  Login
    Set Username  pekka
    Set Password  pekka123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  p
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click Button  Register
    Register Should Fail With Message  Username must be at least three letters
    Go To Main Page
    Front Page Should Be Open
    Click Link  Login
    Set Username  p
    Set Password  pekka123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
