*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle1233
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least three letters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kale12
    Output Should Contain  Password must contain at least 8 letters and numbers

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kkaallee
    Output Should Contain  Password must contain at least 8 letters and numbers

*** Keywords ***
Input New
    Input New Command
