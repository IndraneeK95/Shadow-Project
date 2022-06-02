*** Settings ***

Documentation   Test_001: General Script for verifying functionality
#Library         uiautomatorlibrary
Library         String
Library         Dialogs
Library         DateTime
Library         OperatingSystem
Library         Mobile_res.py
Library         Mobile.py
Library         Collections
#Library        SeleniumLibrary
Library         AppiumLibrary




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
&{url11Id}  textContains=Your IPv4 address on the public Internet appears to be 117.99.214.89
${file_size}        100
&{download_notification}     textContains=Download complete

*** Keywords ***
Verify Particular Url Is Opened IPV6
    [Arguments]  &{url_identifier}
    BuiltIn.Sleep  5
    ${web_page}  Wait for Exists  &{url_identifier}
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
     
*** Comments ***
TC1:Sending a text message

       # Set Serial    HEBENZEE8TORV4W8
       # Turn On Screen
        #Turn Off Screen
        #Press Home
        #Press Menu
        ${list}      Execute Adb Command     devices
        Log To Console      ${list[0]}
        Log To Console      ${list[1]}
       #
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

       # Open Notification

#TC2
       # Turn On Screen
        #Execute Adb Shell Command  monkey -p com.android.chrome -c android.intent.category.LAUNCHER 1
        #BuiltIn.Sleep  2
        ##Click   className=android.widget.EditText
        #Set text   Cache optimization papers    resourceId=com.android.chrome:id/url_bar
        #Click   className=android.view.ViewGroup
         #Turn Off Screen
         #Click   resourceId=com.android.chrome:id/search_box_text
         #Set text     https://www.researchgate.net/publication/317194195_A_Comparative_Study_of_Cache_Optimization_Techniques_and_Cache_Mapping_Techniques  resourceId=com.android.chrome:id/url_bar
         #Press Enter
        # Turn Off Screen
        # Turn On Screen 
          #Click Element   xpath=//span[@class='nova-legacy-c-button__label gtm-download-citation-btn']

#TC3
 #      Execute Adb Shell Command  monkey -p com.android.vending -c android.intent.category.LAUNCHER 1
  #     BuiltIn.Sleep  5
   #    Click    resourceId=com.android.vending:id/mini_blurb
    #   Click    className=android.widget.Button

     #  ${download_speed}     Cal Speed
      # Log To Console    Download speed is
       #Log To Console    ${download_speed}

#TC4

      # Execute Adb Shell Command  monkey -p de.twofingersapps.fileupload -c android.intent.category.LAUNCHER 1
       #BuiltIn.Sleep  5
       #Click    resourceId=de.twofingersapps.fileupload:id/main_fab
       #Click    resourceId=com.google.android.documentsui:id/item_root
       #${upload_speed}      Cal Upload Speed
       #${new}   Convert    ${upload_speed}
       #Log To Console    The upload speed is
       #Log To Console    ${new}

#TC5
        #Execute Adb Shell Command  monkey -p com.android.chrome -c android.intent.category.LAUNCHER 1
        #${status}    Get Text Of Respective Object      text=Airplane mode      resourceId=android:id/switch_widget       position=right
        #run keyword if    '${status}'=="OFF"    Click    text=Airplane mode
        #BuiltIn.Sleep    3
        #Click   resourceID=android:id/switch_widget
        #Builtin.Sleep  2
        #${Result}  Wait For Exists  &{browser_Menu}
        #Click  &{browser_Menu}
        #Click  &{calender_Browser_Menu_NewTab_Button}
        #Click  &{calendar_Browser_Url_Search}
        #Set Text  Laag ja gale  &{browserUrlSearch}
        #Press Enter
        #BuiltIn.Sleep  5
        #Click   text=play  className=android.widget.Button
       # Click  &{calendar_Pause_Song}
        #Click  &{calendar_Download_Song}
        #Click  &{calendar_Download}
       #Click  &{calendar_Pause_Song}
       # Open Notification
        #Get Text Of Respective Object
        #Swipe By Coordinates    540    1340   940    1340

*** Test Cases *** ***
TC2:4G LTE Attach and Communication IPV6
      Execute Adb Shell Command  monkey -p com.android.chrome -c android.intent.category.LAUNCHER 1
      ${Result}  Wait For Exists  &{browser_Menu}
      Click  &{browser_Menu}
      Click  &{calender_Browser_Menu_NewTab_Button}
      Click  &{calendar_Browser_Url_Search}
      Set Text  ${browserUrl10}    &{browserUrlSearch}
      Press Enter
      BuiltIn.Sleep  5
      Verify Particular Url Is Opened IPV6  &{url10Id}


*** Comments *** ***
TC3:4G LTE Attach and Communication IPV4
        Execute Adb Shell Command  monkey -p com.android.chrome -c android.intent.category.LAUNCHER 1
        ${Result}  Wait For Exists  &{browser_Menu}
        Click  &{browser_Menu}
        Click  &{calender_Browser_Menu_NewTab_Button}
        Click  &{calendar_Browser_Url_Search}
        Set Text  ${browserUrl10}    &{browserUrlSearch}
        Press Enter
        BuiltIn.Sleep  5
        Verify Particular Url Is Opened IPV4  &{url11Id}

*** Comments *** *** ***
TC4:Calculate download speed via HTTP protocol in 4G network

        Execute Adb Shell Command  monkey -p com.android.chrome -c android.intent.category.LAUNCHER 1
        ${Result}  Wait For Exists  &{browser_Menu}
        Click  &{browser_Menu}
        Click  &{calender_Browser_Menu_NewTab_Button}
        Click  &{calendar_Browser_Url_Search}
        Set Text  ${browserUrl11}    &{browserUrlSearch}
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










