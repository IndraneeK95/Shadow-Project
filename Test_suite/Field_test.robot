*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     ../Res/Basic_setup.resource


Documentation   Test_001: General Script for verifying functionality

*** Comments ***

Sending a text message
     Send message


4G LTE Attach and Communication IPV6
        Launch browser
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV6  &{url10Id}

*** Comments *** *********
 4G LTE Attach and Communication IPV4
        Launch browser
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV4  &{url11Id}

*** Test Cases ***
Calculate download speed via HTTP protocol in 4G network

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

*** Comments ***
Sending a message when data is on

         Enable Mobile Data
         Send message