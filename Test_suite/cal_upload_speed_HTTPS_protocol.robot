*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     ../Res/Basic_setup.resource


Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***
TC1

         Open Google drive
         Open file
         ${time1}    Get Cur Time
         upload file
         BuiltIn.Sleep  1
         FOR    ${i}    IN RANGE    10000

                  ${Result}  Wait For Exists   &{upload_msg}
        Exit For Loop If    ${Result}==True

        END

        Log To Console    ${Result}
        Run Keyword If    ${Result}      Final Speed Upload   ${time1}
        Final Speed Upload   ${time1}