*** Settings ***
Library      ${EXECDIR}/Lib/Android/localuiautomatorlibrary/Mobile.py
Resource     /home/indranee/Mobile application/Res/Basic_setup.resource


Documentation   Test_001: General Script for verifying functionality

*** Test Cases ***
TC1


         Enable Mobile Data
         Send message
