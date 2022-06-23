*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     ../Res/Basic_setup.resource


Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***
TC1

        Launch browser
        Set Text       https://speed.hetzner.de/    &{browserUrlSearch}
        Press Enter
        ${time1}    Get Cur Time
        BuiltIn.Sleep  1
        Click   textContains=100MB.bin
        BuiltIn.Sleep  2
        FOR    ${i}    IN RANGE    10000
                  Open Notification
                  ${Result}  Wait For Exists   &{download_notification}
        Exit For Loop If    ${Result}==True

        END

        Log To Console    ${Result}
        Run Keyword If    ${Result}      Final Speed    ${time1}
        Final Speed    ${time1}