*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     ../Res/Basic_setup.resource


Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***
TC1

        Open Whatsapp
        Make data call
        Press Home
        Make voice call