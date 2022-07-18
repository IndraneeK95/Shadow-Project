*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
<<<<<<< HEAD
Resource     /home/indranee/Mobile application/Res/Basic_setup.resource

=======
Resource     ../Res/Basic_setup.resource
>>>>>>> origin/master


Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***
TC1

        Launch browser
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV4  &{url11Id}