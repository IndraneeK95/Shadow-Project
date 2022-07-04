*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     ../Res/Basic_setup.resource


Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***
TC1

        Enable Mobile Data
        Make voice call


TC2

        Launch browser
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV4  &{url11Id}


TC3

        Launch browser
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV6  &{url10Id}


