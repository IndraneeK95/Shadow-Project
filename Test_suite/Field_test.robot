*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     ../Res/Basic_setup.resource


Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***

TC1

     Send message


TC2
#4G LTE Attach and communication IPV6
        Launch browser
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV6  &{url10Id}

TC3
#4G LTE Attach and Communication IPV4
        Launch browser
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV4  &{url11Id}

TC4
#Calculate download speed via HTTP protocol in 4G network

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

TC5
#Sending a message when data is on

         Enable Mobile Data
         Send message


TC6
#Simultaneous data and voice call

        Open Whatsapp
        Make data call
        Press Home
        Make voice call

TC7

        #Open Notification
        Swipe Left


TC8
#Calculate upload speed

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

TC9
#make call while data is on

        Enable Mobile Data
        Make voice call
