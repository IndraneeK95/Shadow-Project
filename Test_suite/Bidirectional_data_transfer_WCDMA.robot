*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     /home/indranee/Mobile application/Res/Basic_setup.resource



Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***
TC1

         Open Whatsapp
         Send Media
         BuiltIn.Sleep  1
         FOR    ${i}    IN RANGE    10000

                 ${Result}  Wait For Exists   &{msg_re}
         Exit For Loop If    ${Result}==True

         END

         Log To Console    ${Result}