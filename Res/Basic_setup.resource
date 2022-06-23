*** Settings ***

Documentation   Test_001: General Script for verifying functionality
#Library         uiautomatorlibrary
Library         String
Library         Dialogs
Library         DateTime
Library         OperatingSystem
Library         ../Lib/Android/localuiautomatorlibrary/Mobile.py
Library         Collections




*** Variables ***
&{browser_Menu}  descriptionContains=More options  resourceId=com.android.chrome:id/menu_button
&{calender_Browser_Menu_NewTab_Button}  text=New tab  resourceId=com.android.chrome:id/menu_item_text
&{calendar_Browser_Url_Search}  text=Search or type web address  resourceId=com.android.chrome:id/search_box_text  packageName=com.android.chrome
&{browserUrlSearch}  text=Search or type web address  resourceId=com.android.chrome:id/url_bar  className=android.widget.EditText
&{calendar_Pause_Song}  text=pause  className=android.widget.Button
&{calendar_Download_Song}  text=show more media controls
&{calendar_Download}  text=download media
${browserUrl10}  https://test-ipv6.com/
${browserUrl11}     https://speed.hetzner.de/
&{url10Id}  textContains=No IPv6 address detected
&{url11Id}  textContains=Your IPv4 address on the public Internet appears to be
${file_size}        100
${upload_file_size}  9
&{download_notification}     textContains=Download complete
&{mobileDataOff}  text=Off  descriptionContains=Mobile data
&{mobileDataOn}  text=On  descriptionContains=Mobile data
&{whatsapp-1}         resourceId=com.whatsapp:id/contact_row_container
&{whatsapp-2}          className=android.widget.ImageButton
&{whatsapp-3}          resourceId=android:id/button1
&{voice-1}             textContains=Phone
&{voice-2}             resourceId=com.android.contacts:id/primary_action_view
&{upload_msg}          textContains=VID-20210701-WA0001.mp4
&{upload_1}            resourceId=com.google.android.apps.docs:id/branded_fab
&{upload_2}            textContains=Upload
&{upload_3}            textContains=9.24MB


*** Keywords ***
Launch browser
     Execute Adb Shell Command  monkey -p com.android.chrome -c android.intent.category.LAUNCHER 1
      ${Result}  Wait For Exists  &{browser_Menu}
      Click  &{browser_Menu}
      Click  &{calender_Browser_Menu_NewTab_Button}
      Click  &{calendar_Browser_Url_Search}

Verify Particular Url Is Opened IPV6
    [Arguments]  &{url_identifier}
    BuiltIn.Sleep  5
    ${web_page}  Wait for Exists  &{url_identifier}
    BuiltIn.Sleep    2
    Log To Console    ${web_page}
    Run Keyword If  ${web_page}  Log To Console  IPV6 not supported
    ...  ELSE  Log To Console  IPV6 supported


Verify Particular Url Is Opened IPV4
    [Arguments]  &{url_identifier}
    BuiltIn.Sleep  5
    ${web_page}  Wait for Exists  &{url_identifier}
    Run Keyword If  ${web_page}  Log To Console  IPV4 supported
    ...  ELSE  Log To Console  IPV4 not supported


Final Speed
     [Arguments]    ${time1}
      ${time2}      Get Cur Time
      Log To Console    ${time2}
      ${rel_time}   Get Rel Time    ${time1}    ${time2}
      ${speed}      Get Speed        ${file_size}      ${rel_time}
      Log To Console    Download speed is
      Log To Console    ${speed}


Final Speed Upload
     [Arguments]    ${time1}
      ${time2}      Get Cur Time
      Log To Console    ${time2}
      ${rel_time}   Get Rel Time    ${time1}    ${time2}
      ${speed}      Get Speed        ${upload_file_size}      ${rel_time}
      Log To Console    Upload speed is
      Log To Console    ${speed}



Send message
       Execute Adb Shell Command  monkey -p com.simplemobiletools.smsmessenger -c android.intent.category.LAUNCHER 1
       Click   resourceId=com.simplemobiletools.smsmessenger:id/conversations_fab
       BuiltIn.Sleep  1
       Set text  6000700023   resourceId=com.simplemobiletools.smsmessenger:id/new_conversation_address
       BuiltIn.Sleep  1
       Click   resourceId=com.simplemobiletools.smsmessenger:id/new_conversation_confirm
       BuiltIn.Sleep  1
       Set text  HiIndranee   resourceId=com.simplemobiletools.smsmessenger:id/thread_type_message
       BuiltIn.Sleep  1
       Click   resourceId=com.simplemobiletools.smsmessenger:id/thread_send_message


Swipe Left In Quick Panel
    Press Home
    Open Notification
    Swipe Left
    Click       className=android.widget.ImageView
    BuiltIn.Sleep  1
    Press Home





Verify Option State
    [Arguments]  ${state}  &{optionLocator}
    ${status}  wait for exists  &{optionLocator}
    run keyword unless  ${status}==${state}  Fail  &{optionLocator} is not in ${state} state+


Enable Mobile Data
      Swipe Left In Quick Panel
       BuiltIn.Sleep  2


Open Whatsapp
         Execute Adb Shell Command  monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1


Make data call
         Click      &{whatsapp-1}
         Click      &{whatsapp-2}



Make voice call
         Click      &{voice-1}
         Click      &{voice-2}


Open Google drive
         Execute Adb Shell Command  monkey -p com.google.android.apps.docs -c android.intent.category.LAUNCHER 1

Open file
         Click      &{upload_1}
         Click      &{upload_2}

upload file
             Click       &{upload_3}

