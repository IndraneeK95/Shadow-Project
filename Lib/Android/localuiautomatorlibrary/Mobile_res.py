# -*- coding: utf-8 -*-
from robot.api import logger
from uiautomator import Device
import subprocess
import os
import time
import datetime
from robot.libraries.BuiltIn import BuiltIn

import random
import string


class TestHelper:
    def __init__(self, adb):
        self.adb = adb

    def __convert_to_unicode_by_text(self, text):
        """
        Transfer input string to UTF-8 format
        """
        # Remove the unicode tag. example: transfer u'abc' to string abc
        return repr(text)[2:-1]

    def send_set_text_cmd(self, text):
        """
        Setting the input string to MyIME
        1. adb shell "am broadcast -a myIME.intent.action.pass.string -e input abc"
        2. adb shell input keyevent KEYCODE_UNKNOWN
        """
        self.adb.shell_cmd(
            '\"am broadcast -a myIME.intent.action.pass.string -e input \\\"\"%s\"\\\"\"' % TestHelper.__convert_to_unicode_by_text(
                self, text))
        self.adb.shell_cmd('input keyevent KEYCODE_UNKNOWN')


class ADB:
    def __init__(self, android_serial=None):
        self.buf = []
        self.buf.append('adb ')
        self.prefix_cmd = ''.join(self.buf)
        if android_serial is not None:
            self.buf.append('-s %s ' % android_serial)
            self.prefix_cmd = ''.join(self.buf)

    def cmd(self, cmd):
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    def shell_cmd(self, cmd):
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append('shell ')
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()


class Mobile():

    def __init__(self):
        self.set_serial(None)

    def set_serial(self, android_serial):
        """
        Specify given *android_serial* device to perform test.

        You do not have to specify the device when there is only one device connects to the computer.

        When you need to use multiple devices, do not use this keyword to switch between devices in test execution.

        Using different library name when importing this library according to http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.8.5.

        | Setting | Value  | Value     | Value   |
        | Library | Mobile | WITH NAME | Mobile1 |
        | Library | Mobile | WITH NAME | Mobile2 |

        And set the serial to each library.

        | Test Case        | Action             | Argument           |
        | Multiple Devices | Mobile1.Set Serial | device_1's serial  |
        |                  | Mobile2.Set Serial | device_2's serial  |

        """
        self.adb = ADB(android_serial)
        self.device = Device(android_serial)
        self.test_helper = TestHelper(self.adb)

    def get_device_info(self):
        """
        Retrieve the device info.

        The keyword will return a dictionary.

        You can log the information by using the log dictionary keyword in build in Collections library(http://robotframework.googlecode.com/hg/doc/libraries/Collections.html?r=2.8.4).

        Example:
        | ${device_info} | Get Device Info |
        | Log Dictionary | ${device_info}  |

        =>

        Dictionary size is 9 and it contains following items:\n
        currentPackageName: com.android.keyguard\n
        displayHeight: 1776\n
        displayRotation: 0\n
        displaySizeDpX: 360\n
        displaySizeDpY: 640\n
        displayWidth: 1080\n
        naturalOrientation: True\n
        productName: hammerhead\n
        sdkInt: 19\n

        Or get specific information of the device by giving the key.

        | ${device_info}  | Get Device Info |   |                |
        | ${product_name} | Get From Dictionary | ${device_info} | productName |

        =>

        ${product_name} = hammerhead

        """
        return self.device.info

    # Key Event Actions of the device
    """
    Turn on/off screen
    """

    def turn_on_screen(self):
        """
        Turn on the screen.
        """
        self.device.screen.on()

    def turn_off_screen(self):
        """
        Turn off the screen.
        """
        self.device.screen.off()

    """
    Press hard/soft key
    """

    def press_key(self, *keys):
        """
        Press *key* keycode.

        You can find all keycode in http://developer.android.com/reference/android/view/KeyEvent.html

        """
        # not tested
        self.device.press(*keys)

    def press_home(self):
        """
        Press home key.
        """
        self.device.press.home()

    def press_back(self):
        """
        Press back key.
        """
        self.device.press.back()

    def press_left(self):
        """
        Press left key.
        """
        self.device.pres.left()

    def press_right(self):
        """
        Press right key.
        """
        self.device.press.right()

    def press_up(self):
        """
        Press up key.
        """
        self.device.press.up()

    def press_down(self):
        """
        Press down key.
        """
        self.device.press.down()

    def press_center(self):
        """
        Press center key.
        """
        self.device.press.center()

    def press_menu(self):
        """
        Press menu key.
        """
        self.device.press.menu()

    def press_search(self):
        """
        Press search key.
        """
        self.device.press.search()

    def press_enter(self):
        """
        Press enter key.
        """
        self.device.press.enter()

    def press_delete(self):
        """
        Press delete key.
        """
        self.device.press.delete()

    def press_recent(self):
        """
        Press recent key.
        """
        self.device.press.recent()

    def press_volume_up(self):
        """
        Press volume up key.
        """
        self.device.press.volume_up()

    def press_volume_down(self):
        """
        Press volume down key.
        """
        self.device.press.volume_down()

    def press_camera(self):
        """
        Press camera key.
        """
        self.device.press.camera()

    def press_power(self):
        """
        Press power key.
        """
        self.device.press.power()

    # Gesture interaction of the device

    def click_at_coordinates(self, x, y):
        """
        Click at (x,y) coordinates.
        """
        self.device.click(int(x), int(y))

    def swipe_by_coordinates(self, sx, sy, ex, ey, steps=10):
        """
        Swipe from (sx, sy) to (ex, ey) with *steps* .

        Example:
        | Swipe By Coordinates | 540 | 1340 | 940 | 1340 |     | # Swipe from (540, 1340) to (940, 100) with default steps 10 |
        | Swipe By Coordinates | 540 | 1340 | 940 | 1340 | 100 | # Swipe from (540, 1340) to (940, 100) with steps 100        |
        """
        self.device.swipe(sx, sy, ex, ey, steps)

    # Swipe from the center of the ui object to its edge

    def swipe_left(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to left.

        Example:

        | Swipe Left | description=Home screen 3 |                           | # swipe the UI object left              |
        | Swipe Left | 5                         | description=Home screen 3 | # swipe the UI object left with steps=5 |

        See `introduction` for details about Identified UI object.
        """
        self.device(**selectors).swipe.left(steps=steps)

    def swipe_right(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to right

        See `Swipe Left` for more details.
        """
        self.device(**selectors).swipe.right(steps=steps)

    def swipe_top(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to top

        See `Swipe Left` for more details.
        """
        self.device(**selectors).swipe.up(steps=steps)

    def swipe_bottom(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to bottom

        See `Swipe Left` for more details.
        """
        self.device(**selectors).swipe.down(steps=steps)

    def object_swipe_left(self, obj, steps=10):
        """
        Swipe the *obj* from center to left

        Example:

        | ${object}         | Get Object | description=Home screen 3 | # Get the UI object                     |
        | Object Swipe Left | ${object}  |                           | # Swipe the UI object left              |
        | Object Swipe Left | ${object}  | 5                         | # Swipe the UI object left with steps=5 |
        | Object Swipe Left | ${object}  | steps=5                   | # Swipe the UI object left with steps=5 |

        See `introduction` for details about identified UI object.
        """
        obj.swipe.left(steps=steps)

    def object_swipe_right(self, obj, steps=10):
        """
        Swipe the *obj* from center to right

        See `Object Swipe Left` for more details.
        """
        obj.swipe.right(steps=steps)

    def object_swipe_top(self, obj, steps=10):
        """
        Swipe the *obj* from center to top

        See `Object Swipe Left` for more details.
        """
        obj.swipe.up(steps=steps)

    def object_swipe_bottom(self, obj, steps=10):
        """
        Swipe the *obj* from center to bottom

        See `Object Swipe Left` for more details.
        """
        obj.swipe.down(steps=steps)

    def drag_by_coordinates(self, sx, sy, ex, ey, steps=10):
        """
        Drag from (sx, sy) to (ex, ey) with steps

        See `Swipe By Coordinates` also.
        """
        self.device.drag(sx, sy, ex, ey, steps)

    # Wait until the specific ui object appears or gone

    # wait until the ui object appears
    def wait_for_exists(self, timeout=0, *args, **selectors):
        """
        Wait for the object which has *selectors* within the given timeout.

        Return true if the object *appear* in the given timeout. Else return false.
        """
        return self.device(**selectors).wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_gone(self, timeout=0, *args, **selectors):
        """
        Wait for the object which has *selectors* within the given timeout.

        Return true if the object *disappear* in the given timeout. Else return false.
        """
        return self.device(**selectors).wait.gone(timeout=timeout)

    def wait_for_object_exists(self, obj, timeout=0):
        """
        Wait for the object: obj within the given timeout.

        Return true if the object *appear* in the given timeout. Else return false.
        """
        return obj.wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_object_gone(self, obj, timeout=0):
        """
        Wait for the object: obj within the given timeout.

        Return true if the object *disappear* in the given timeout. Else return false.
        """
        return obj.wait.gone(timeout=timeout)

    # Perform fling on the specific ui object(scrollable)
    def fling_forward_horizontally(self, *args, **selectors):
        """
        Perform fling forward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.horiz.forward()

    def fling_backward_horizontally(self, *args, **selectors):
        """
        Perform fling backward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.horiz.backward()

    def fling_forward_vertically(self, *args, **selectors):
        """
        Perform fling forward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.vert.forward()

    def fling_backward_vertically(self, *args, **selectors):
        """
        Perform fling backward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.vert.backward()

    # Perform scroll on the specific ui object(scrollable)

    # horizontal
    def scroll_to_beginning_horizontally(self, steps=10, *args, **selectors):
        """
        Scroll the object which has *selectors* attributes to *beginning* horizontally.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.toBeginning(steps=steps)

    def scroll_to_end_horizontally(self, steps=10, *args, **selectors):
        """
        Scroll the object which has *selectors* attributes to *end* horizontally.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.toEnd(steps=steps)

    def scroll_forward_horizontally(self, steps=10, *args, **selectors):
        """
        Perform scroll forward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.forward(steps=steps)

    def scroll_backward_horizontally(self, steps=10, *args, **selectors):
        """
        Perform scroll backward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.backward(steps=steps)

    def scroll_to_horizontally(self, obj, *args, **selectors):
        """
        Scroll(horizontally) on the object: obj to specific UI object which has *selectors* attributes appears.

        Return true if the UI object, else return false.

        See `Scroll To Vertically` for more details.
        """
        return obj.scroll.horiz.to(**selectors)

    # vertical
    def scroll_to_beginning_vertically(self, steps=10, *args, **selectors):
        """
        Scroll the object which has *selectors* attributes to *beginning* vertically.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.vert.toBeginning(steps=steps)

    def scroll_to_end_vertically(self, steps=10, *args, **selectors):
        """
        Scroll the object which has *selectors* attributes to *end* vertically.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.vert.toEnd(steps=steps)

    def scroll_forward_vertically(self, steps=10, *args, **selectors):
        """
        Perform scroll forward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        Example:
        | ${can_be_scroll} | Scroll Forward Vertically | className=android.widget.ListView       |                                   | # Scroll forward the UI object with class name |
        | ${can_be_scroll} | Scroll Forward Vertically | 100                                     | className=android.widget.ListView | # Scroll with steps |
        """
        return self.device(**selectors).scroll.vert.forward(steps=steps)

    def scroll_backward_vertically(self, steps=10, *args, **selectors):
        """
        Perform scroll backward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.vert.backward(steps=steps)

    def scroll_to_vertically(self, obj, *args, **selectors):
        """
        Scroll(vertically) on the object: obj to specific UI object which has *selectors* attributes appears.

        Return true if the UI object, else return false.

        Example:

        | ${list}        | Get Object           | className=android.widget.ListView |              | # Get the list object     |
        | ${is_web_view} | Scroll To Vertically | ${list}                           | text=WebView | # Scroll to text:WebView. |
        """
        return obj.scroll.vert.to(**selectors)

    # Screen Actions of the device

    def get_screen_orientation(self):
        """
        Get the screen orientation.

        Possible result: natural, left, right, upsidedown

        See for more details: https://github.com/xiaocong/uiautomator#screen-actions-of-the-device
        """
        return self.device.orientation

    def set_screen_orientation(self, orientation):
        """
        Set the screen orientation.

        Input *orientation* : natural or n, left or l, right or r, upsidedown (support android version above 4.3)

        The keyword will unfreeze the screen rotation first.

        See for more details: https://github.com/xiaocong/uiautomator#screen-actions-of-the-device

        Example:

        | Set Screen Orientation | n       | # Set orientation to natural |
        | Set Screen Orientation | natural | # Do the same thing          |
        """
        self.device.orientation = orientation

    def freeze_screen_rotation(self):
        """
        Freeze the screen auto rotation
        """
        self.device.freeze_rotation()

    def unfreeze_screen_rotation(self):
        """
        Un-Freeze the screen auto rotation
        """
        self.device.freeze_rotation(False)

    def screenshot(self, scale=None, quality=None):
        """
        Take a screenshot of device and log in the report with timestamp, scale for screenshot size and quality for screenshot quality
        default scale=1.0 quality=100
        """
        output_dir = BuiltIn().get_variable_value('${OUTPUTDIR}')
        test_name = str(BuiltIn().get_variable_value('${TEST_NAME}')).split(':')[0]
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y_%H_%M_%S')
        screenshot_timestamp = st + '_Screenshot'
        if not os.path.exists(output_dir + '//' + test_name):
            os.makedirs(output_dir + '//' + test_name)
        screenshot_report_dir = '%s%s%s%s%s.png' % (output_dir, os.sep, test_name, os.sep, screenshot_timestamp)
        self.device.screenshot(screenshot_report_dir, scale, quality)
        logger.info('\n<a href="%s">%s</a><br><img src="%s">' % (
        screenshot_report_dir, screenshot_timestamp, screenshot_report_dir), html=True)

    def capture_device_logs(self):

        report_path = BuiltIn().get_variable_value('${OUTPUTDIR}')
        test_name = str(BuiltIn().get_variable_value('${TEST_NAME}')).split(':')[0]
        test_device = str(BuiltIn().get_variable_value('${TEST_DEVICE}'))

        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y_%H_%M_%S')
        logcat_timestamp = timestamp + '_Logcat'
        radio_timestamp = timestamp + '_Radio_Log'

        if not os.path.exists(report_path + '//' + test_name):
            os.makedirs(report_path + '//' + test_name)

        logcat_report_dir = '%s%s%s%s%s.txt' % (report_path, os.sep, test_name, os.sep, logcat_timestamp)
        radio_report_dir = '%s%s%s%s%s.txt' % (report_path, os.sep, test_name, os.sep, radio_timestamp)

        logcat_cmd = 'adb -s %s logcat -d -v time > %s' % (test_device, logcat_report_dir)
        radio_cmd = 'adb -s %s logcat -d -v time -b radio > %s' % (test_device, radio_report_dir)
        os.system(str(logcat_cmd))
        os.system(str(radio_cmd))
        logger.info('\n<a href="%s">%s</a><br><src="%s">' % (logcat_report_dir, logcat_timestamp, logcat_report_dir),
                    html=True)
        logger.info('\n<a href="%s">%s</a><br><src="%s">' % (radio_report_dir, radio_timestamp, radio_report_dir),
                    html=True)

    # Watcher
    def __unicode_to_dict(self, a_unicode):
        a_dict = dict()
        dict_item_count = a_unicode.count('=')
        for count in range(dict_item_count):
            equal_sign_position = a_unicode.find('=')
            comma_position = a_unicode.find(',')
            a_key = a_unicode[0:equal_sign_position]
            if comma_position == -1:
                a_value = a_unicode[equal_sign_position + 1:]
            else:
                a_value = a_unicode[equal_sign_position + 1:comma_position]
                a_unicode = a_unicode[comma_position + 1:]
            a_dict[a_key] = a_value
        return a_dict

    def register_click_watcher(self, watcher_name, selectors, *condition_list):
        """
        The watcher click on the object which has the *selectors* when conditions match.
        """
        watcher = self.device.watcher(watcher_name)
        for condition in condition_list:
            watcher.when(**self.__unicode_to_dict(condition))
        watcher.click(**self.__unicode_to_dict(selectors))
        self.device.watchers.run()

    def register_press_watcher(self, watcher_name, press_keys, *condition_list):
        """
        The watcher perform *press_keys* action sequentially when conditions match.
        """

        def unicode_to_list(a_unicode):
            a_list = list()
            comma_count = a_unicode.count(',')
            for count in range(comma_count + 1):
                comma_position = a_unicode.find(',')
                if comma_position == -1:
                    a_list.append(str(a_unicode))
                else:
                    a_list.append(a_unicode[0:comma_position])
                    a_unicode = a_unicode[comma_position + 1:]
            return a_list

        watcher = self.device.watcher(watcher_name)
        for condition in condition_list:
            watcher.when(**self.__unicode_to_dict(condition))
        watcher.press(*unicode_to_list(press_keys))
        self.device.watchers.run()

    def remove_watchers(self, watcher_name=None):
        """
        Remove watcher with *watcher_name* or remove all watchers.
        """
        if watcher_name == None:
            self.device.watchers.remove()
        else:
            self.device.watchers.remove(watcher_name)

    def list_all_watchers(self):
        """
        Return the watcher list.
        """
        return self.device.watchers

    # Selector

    def get_object(self, *args, **selectors):
        """
        Get the UI object with selectors *selectors*

        See `introduction` for details about identified UI object.

        Example:
        | ${main_layer} | Get Object | className=android.widget.FrameLayout | index=0 | # Get main layer which class name is FrameLayout |
        """
        return self.device(*args, **selectors)

    def get_child(self, object, *args, **selectors):
        """
        Get the child or grandchild UI object from the *object* with *selectors*
        Example:
        | ${root_layout}   | Get Object | className=android.widget.FrameLayout |
        | ${child_layout}  | Get Child  | ${root_layout}                       | className=LinearLayout |
        """
        return object.child(*args, **selectors)

    def get_sibling(self, object, *args, **selectors):
        """
        Get the sibling or child of sibling UI object from the *object* with *selectors*
        Example:
        | ${root_layout}     | Get Object   | className=android.widget.FrameLayout |
        | ${sibling_layout}  | Get Sibling  | ${root_layout}                       | className=LinearLayout |
        """
        return object.sibling(*args, **selectors)

    def get_count(self, *args, **selectors):
        """
        Return the count of UI object with *selectors*

        Example:

        | ${count}              | Get Count           | text=Accessibility    | # Get the count of UI object text=Accessibility |
        | ${accessibility_text} | Get Object          | text=Accessibility    | # These two keywords combination                |
        | ${count}              | Get Count Of Object | ${accessibility_text} | # do the same thing.                            |

        """
        obj = self.get_object(**selectors)
        return self.get_count_of_object(obj)

    #     def get_count_of_object(self, obj):
    #         """
    #         Return the count of given UI object
    #
    #         See `Get Count` for more details.
    #         """
    #         return len(obj)

    def get_info_of_object(self, obj, selector=None):
        """
        return info dictionary of the *obj*
        The info example:
        {
         u'contentDescription': u'',
         u'checked': False,
         u'scrollable': True,
         u'text': u'',
         u'packageName': u'com.android.launcher',
         u'selected': False,
         u'enabled': True,
         u'bounds':
                   {
                    u'top': 231,
                    u'left': 0,
                    u'right': 1080,
                    u'bottom': 1776
                   },
         u'className': u'android.view.View',
         u'focusable': False,
         u'focused': False,
         u'clickable': False,
         u'checkable': False,
         u'chileCount': 1,
         u'longClickable': False,
         u'visibleBounds':
                          {
                           u'top': 231,
                           u'left': 0,
                           u'right': 1080,
                           u'bottom': 1776
                          }
        }
        """
        if selector:
            return obj.info.get(selector)
        else:
            return obj.info

    def click(self, *args, **selectors):
        """
        Click on the UI object with *selectors*

        | Click | text=Accessibility | className=android.widget.Button | # Click the object with class name and text |
        """
        self.device(**selectors).click()

    def click_on_object(self, object):
        """
        Click on the UI object which is gained by `Get Object`.

        Example:
        | ${button_ok}    | text=OK      | className=android.widget.Button |
        | Click on Object | ${button_ok} |
        """
        return object.click()

    def long_click(self, *args, **selectors):
        """
        Long click on the UI object with *selectors*

        See `Click` for more details.
        """
        self.device(**selectors).long_click()

    def call(self, obj, method, *args, **selectors):
        """
        This keyword can use object method from original python uiautomator

        See more details from https://github.com/xiaocong/uiautomator

        Example:

        | ${accessibility_text} | Get Object            | text=Accessibility | # Get the UI object                        |
        | Call                  | ${accessibility_text} | click              | # Call the method of the UI object 'click' |
        """
        func = getattr(obj, method)
        return func(**selectors)

    def set_text(self, input_text, *args, **selectors):
        """
        Set *input_text* to the UI object with *selectors*
        """
        self.device(**selectors).set_text(input_text)

    def set_object_text(self, input_text, object):
        """
        Set *input_text* the *object* which could be selected by *Get Object* or *Get Child*
        """
        object.set_text(input_text)

    # Other feature

    def clear_text(self, *args, **selectors):
        """
        Clear text of the UI object  with *selectors*
        """
        while True:
            target = self.device(**selectors)
            text = target.info['text']
            target.clear_text()
            remain_text = target.info['text']
            if text == '' or remain_text == text:
                break

    def open_notification(self):
        """
        Open notification

        Built in support for Android 4.3 (API level 18)

        Using swipe action as a workaround for API level lower than 18

        """
        sdk_version = self.device.info['sdkInt']
        if sdk_version < 18:
            height = self.device.info['displayHeight']
            self.device.swipe(1, 1, 1, height - 1, 1)
        else:
            self.device.open.notification()

    def open_quick_settings(self):
        """
        Open quick settings

        Work for Android 4.3 above (API level 18)

        """
        self.device.open.quick_settings()

    def sleep(self, time):
        """
        Sleep(no action) for *time* (in millisecond)
        """
        target = 'wait for %s' % str(time)
        self.device(text=target).wait.exists(timeout=time)

    def install(self, apk_path):
        """
        Install apk to the device.

        Example:

        | Install | ${CURDIR}${/}com.hmh.api_4.0.apk | # Given the absolute path to the apk file |
        """
        self.adb.cmd('install "%s"' % apk_path)

    def uninstall(self, package_name):
        """
        Uninstall the APP with *package_name*
        """
        self.adb.cmd('uninstall %s' % package_name)

    def execute_adb_command(self, cmd):
        """
        Execute adb *cmd*
        """
        return self.adb.cmd(cmd)

    def execute_adb_shell_command(self, cmd):
        """
        Execute adb shell *cmd*
        """
        return self.adb.shell_cmd(cmd)

    def type(self, input_text):
        """
        [IME]

        Type *text* at current focused UI object
        """
        self.test_helper.send_set_text_cmd(input_text)

    def start_test_agent(self):
        """
        [Test Agent]

        Start Test Agent Service
        """
        cmd = 'am start edu.ntut.csie.sslab1321.testagent/edu.ntut.csie.sslab1321.testagent.DummyActivity'
        self.adb.shell_cmd(cmd)

    def stop_test_agent(self):
        """
        [Test Agent]

        Stop Test Agent Service
        """
        cmd = 'am broadcast -a testagent -e action STOP_TESTAGENT'
        self.adb.shell_cmd(cmd)

    def connect_to_wifi(self, ssid, password=None):
        """
        [Test Agent]

        Connect to *ssid* with *password*
        """
        cmd = 'am broadcast -a testagent -e action CONNECT_TO_WIFI -e ssid %s -e password %s' % (ssid, password)
        self.adb.shell_cmd(cmd)

    def clear_connected_wifi(self):
        """
        [Test Agent]

        Clear all existed Wi-Fi connection
        """
        cmd = 'am broadcast -a testagent -e action CLEAR_CONNECTED_WIFIS'
        self.adb.shell_cmd(cmd)

    def scroll_for_vertical_screen_object(self, *args, **selectors):

        if self.wait_for_exists(timeout=5000, **selectors):
            return True
        else:
            search = self.device().scroll.to(**selectors)
            if not search:
                self.device(scrollable=True).scroll.vert.backward(steps=2, action='backward')
                search = self.device().scroll.to(**selectors)
                return search
            else:
                return True

    def get_object_text(self, **selectors):

        return self.device(**selectors).text

    def get_object_description(self, **selectors):

        return self.device(**selectors).description

    def get_object_classname(self, **selectors):

        return self.device(**selectors).className

    def get_object_packagename(self, **selectors):

        return self.device(**selectors).packageName

    def drag_object_to_a_coordinate(self, x, y, steps=10, **selectors):

        self.device(**selectors).drag.to(x, y, steps=steps)

    def drag_object_to_certain_position(self, width_percentage, height_percentage, steps=10, **selectors):

        x, y = float(self.get_display_screen_width()), float(self.get_display_screen_height())
        width_percentage, height_percentage = float(width_percentage), float(height_percentage)
        x = (width_percentage / 100) * x
        y = (height_percentage / 100) * y

        self.device(**selectors).drag.to(x, y, steps=steps)

    def drag_from_a_point_to_another(self, startX_percentage, startY_percentage, endX_percentage, endY_percentage,
                                     steps=10):

        x, y = float(self.get_display_screen_width()), float(self.get_display_screen_height())
        startX_percentage, startY_percentage = float(startX_percentage), float(startY_percentage)
        endX_percentage, endY_percentage = float(endX_percentage), float(endY_percentage)
        startX = (startX_percentage / 100) * x
        startY = (startY_percentage / 100) * y
        endX = (endX_percentage / 100) * x
        endY = (endY_percentage / 100) * y

        self.drag_by_coordinates(startX, startY, endX, endY, steps)

    def click_on_coordinates(self, width_percentage, height_percentage):

        x, y = float(self.get_display_screen_width()), float(self.get_display_screen_height())
        width_percentage, height_percentage = float(width_percentage), float(height_percentage)
        x = (width_percentage / 100) * x
        y = (height_percentage / 100) * y

        self.device.click(int(x), int(y))

    def adb_get_device_os_version(self):

        cmd = str('getprop ro.build.version.release')
        devices_os_version = self.execute_adb_shell_command(cmd)
        devices_os_version = devices_os_version[0].decode('UTF-8').strip()

        if devices_os_version.count('.') > 1:
            index = devices_os_version.rfind('.')
            devices_os_version = devices_os_version[:index]

        return float(devices_os_version)

    def launch_app_using_ui(self, app_name=None):

        app_exist = False
        os_version = ''
        os_version = self.adb_get_device_os_version()

        if app_name is None:
            raise Exception("Application to Launch is not specified.")

        if os_version in [8.0, 8.1]:

            self.press_home()

            if self.wait_for_exists(timeout=5000, descriptionContains='Apps'):
                self.device(descriptionContains='Apps').click()
            elif self.wait_for_exists(timeout=5000, descriptionContains='App'):
                self.device(descriptionContains='App').click()
            else:
                raise Exception("Device is not in Home Screen")

            if self.wait_for_exists(timeout=5000, text=str(app_name)):
                self.click(text=str(app_name))
                app_exist = True
            else:
                self.set_text(str(app_name), resourceId='com.android.launcher3:id/search_box_input')
                if self.wait_for_exists(timeout=5000, text=str(app_name), description=str(app_name)):
                    self.click(text=str(app_name), description=str(app_name))
                    app_exist = True

            if not app_exist:
                raise AssertionError("%s application not found." % app_name)

    def close_app_using_ui(self, app_name=None):

        if app_name is None:
            raise Exception("Application to Close is not specified.")

        self.press_recent()

        if self.wait_for_exists(timeout=5000, textContains=str(app_name)):
            self.device(textContains=str(app_name)).fling.horiz.forward()
            self.sleep(2000)
            self.press_home()
            return True
        else:
            self.press_home()
            print("All Apps have been cleared")
            return False

    # def close_all_apps_using_ui(self):
    #
    #     self.press_recent()
    #
    #     if self.wait_for_exists(timeout=5000, className='android.widget.ScrollView', packageName='com.android.systemui'):
    #         self.fling_backward_vertically(className='android.widget.ScrollView')
    #         self.sleep(2000)
    #         if self.wait_for_exists(timeout=5000, text='CLEAR ALL', resourceId='com.android.systemui:id/button'):
    #             self.click(text='CLEAR ALL', resourceId='com.android.systemui:id/button')
    #             self.sleep(1000)
    #             return True
    #         else:
    #             while True:
    #                 self.click(resourceId='com.android.systemui:id/dismiss_task')
    #                 if not self.wait_for_exists(timeout=3000, className='android.widget.ScrollView', packageName='com.android.systemui'):
    #                     print("All Apps have been cleared")
    #                     return True
    #     else:
    #         self.press_home()
    #         print ("Recent App list is empty")
    #         return False

    def close_all_apps_using_ui(self):

        self.press_recent()

        if self.wait_for_exists(timeout=5000, className='android.view.View', packageName='com.android.launcher3',
                                resourceId='com.android.launcher3:id/snapshot'):
            while True:
                self.fling_forward_vertically(className='android.view.View', packageName='com.android.launcher3',
                                              resourceId='com.android.launcher3:id/snapshot')
                self.sleep(2000)
                if not self.wait_for_exists(className='android.view.View', packageName='com.android.launcher3',
                                            resourceId='com.android.launcher3:id/snapshot'):
                    print("All Apps have been cleared")
                    return True
        else:
            self.press_home()
            print("Recent App list is empty")
            return False

    def scroll_to_text(self, **selectors):
        click_bounds = None
        count = 0
        first = ""
        second = ""
        device = self.device
        val = None
        # scrolling app list
        try:
            while True:

                # last_icon_index = device(selectors[u'resourceId']).count
                # check whether it's the last icon by checking the alphabet
                list_of_icons = [x.info for x in device(**selectors)]
                first = list_of_icons[-1][u'text']

                # check if it reaches to the desired app name
                try:
                    val = [ind for ind, x in enumerate(list_of_icons) if str(x[u'text']) == str(selectors[u'text'])][-1]
                except:
                    pass

                if val is not None:
                    break

                # exit when reached at the end of apps list
                if second == first:
                    break

                second = first

                # swipe down
                self.device().scroll(steps=10)

        except:
            pass

    def pinch_screen_in(self, zoom_in_percentage, steps, **selectors):
        """
        Pinches from the edge to centre on the UI object with *selectors*

        | pinch_screen_in | 100 | 5 | packagename=com.android.camera2 |
        """
        self.device(**selectors).pinch.In(percent=zoom_in_percentage, steps=steps)

    def pinch_screen_out(self, zoom_out_percentage, steps, **selectors):
        """
        Pinches from centre to edge on the UI object with *selectors*

        | pinch_screen_in | 30 | 10 | packagename=com.android.camera2 |
        """
        self.device(**selectors).pinch.Out(percent=zoom_out_percentage, steps=steps)

    def get_respective_object(self, **kwargs):
        """
        Get UI object based on respective position of another object

        Example:
        | &{bt_selector} | text=Bluetooth |
        | &{switch_selector} | className=android.widget.Switch |
        | ${obj} | get_respective_object | selector_1=&{bt_selector} | selector_2=&{switch_selector} | position=right |
        """
        selector_1_obj = selector_2_obj = position = ""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'selector_1':
                    selector_1_obj = value
                if key == 'selector_2':
                    selector_2_obj = value
                if key == 'position':
                    position = value

        if selector_1_obj == selector_2_obj == position == "":
            raise AssertionError("Wrong keyword input error %s" % str(kwargs))

        view_obj = None

        try:
            if position == 'left':
                view_obj = self.device(**selector_1_obj).left(**selector_2_obj)
            if position == 'right':
                view_obj = self.device(**selector_1_obj).right(**selector_2_obj)
            if position == 'top':
                view_obj = self.device(**selector_1_obj).up(**selector_2_obj)
            if position == 'bottom':
                view_obj = self.device(**selector_1_obj).down(**selector_2_obj)
        except:
            raise AssertionError("UI object identification failed. %s" % str(kwargs))

        if view_obj is None:
            raise AssertionError("UI object identification failed. %s" % str(kwargs))

        return view_obj

    def get_info_of_respective_object(self, **kwargs):
        """
        Get UI object Information based on respective position of another object

        Example:
        | &{bt_selector} | text=Bluetooth |
        | &{switch_selector} | className=android.widget.Switch |
        | ${obj} | get_info_of_respective_object | selector_1=&{bt_selector} | selector_2=&{switch_selector} | position=right |
        """

        view_obj = self.get_respective_object(**kwargs)

        return view_obj.info

    def get_text_of_respective_object(self, **kwargs):
        """
        Get UI object Text based on respective position of another object

        Example:
        | &{bt_selector} | text=Bluetooth |
        | &{switch_selector} | className=android.widget.Switch |
        | ${obj} | get_text_of_respective_object | selector_1=&{bt_selector} | selector_2=&{switch_selector} | position=right |
        """

        view_obj = self.get_respective_object(**kwargs)

        return view_obj.info['text']

    def set_image_path(self, imagepath):

        self.image_path = imagepath

    def locate_image(self, image_location):

        image_location = self.image_path + '\\' + image_location
        return self.device.find(image_location)

    def click_on_image(self, image_location=None, timeout=0):

        stop_iteration = False
        timeout = float(timeout)
        funtion_start_time = time.time()
        image_location = self.image_path + '\\' + image_location
        while not stop_iteration:
            if self.device.find(image_location):
                return self.device.click_image(image_location)

            iteration_time = time.time()
            funtion_running_time = iteration_time - funtion_start_time
            if funtion_running_time > timeout:
                stop_iteration = True

        return self.device.click_image(image_location)

    def get_display_screen_width(self):

        self.turn_on_screen()
        device_info = self.get_device_info()
        return device_info['displayWidth']

    def get_display_screen_height(self):

        self.turn_on_screen()
        device_info = self.get_device_info()
        return device_info['displayHeight']

    def multiple_window_using_ui(self, width_percentage, height_percentage, steps=200, **app_name):

        self.press_recent()
        self.sleep(1000)
        self.drag_object_to_certain_position(width_percentage, height_percentage, steps, **app_name)
        self.sleep(1000)
        self.press_recent()

    def end_multiple_window_using_ui(self, steps=10):

        x, y = self.get_display_screen_width(), self.get_display_screen_height()
        sx, sy = x / 2, y / 2
        ex, ey = x / 2, y

        self.drag_by_coordinates(sx, sy, ex, ey, steps)

    def close_all_chrome_tabs_by_coordinates(self, steps=10):

        self.click(descriptionContains='open tab')

        while True:
            if self.wait_for_exists(timeout=1000, descriptionContains='0 open tabs'):
                break
            x, y = self.get_display_screen_width(), self.get_display_screen_height()
            sx, sy = x / 2, y / 2
            ex, ey = x, y / 2
            self.drag_by_coordinates(sx, sy, ex, ey, steps)

    def split_phone_number(self, phone_number, digits_to_spite_from_last):
        """
        The primary function is to extract last digits from Phone Number
        :param phone_number:
        :param digits_to_spite_from_last: No of digits needed from of a Phone number
        :return:
        """
        phone_number = str(phone_number)
        digits_to_spite_from_last = '-' + str(digits_to_spite_from_last)
        digits_to_spite_from_last = int(digits_to_spite_from_last)

        return str(phone_number[digits_to_spite_from_last:])

    def generate_random_length_text(self, char_length, char_type='TEXT'):
        """
        :param char_length: character length for which text needs to be generated.
        :param char_type: character type which needs to generate
        :return: random genarated text
        """
        if char_type == 'TEXT':
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(int(char_length)))
        elif char_type == 'ONLY_SPECIALS':
            special_char = ['!', '@', '#', '$', '%', '&', '*', ' ']
            return ''.join(random.choice(special_char) for _ in range(int(char_length)))
        elif char_type == 'TEXT_WITH_SPECIALS':
            special_char = '!@#$%&*'
            return ''.join(
                random.choice(string.ascii_uppercase + string.digits + special_char) for _ in range(int(char_length)))

    def adb_get_call_status(self, device_serial_number):
        """
        Returns :
        0 = idle state
        1 = Ringing state
        2 = Active Call state
        """
        cmd = '"dumpsys telephony.registry | grep mCallState"'
        self.set_serial(device_serial_number)
        output = self.execute_adb_shell_command(cmd)
        output = list(output)[0].decode('UTF-8')
        output = str(output).split('=')[1]
        output = output.split()[0]
        return int(output)

    def adb_end_ongoing_call(self, device_serial_number):
        cmd = 'input keyevent KEYCODE_ENDCALL'
        call_status = self.adb_get_call_status(device_serial_number)
        if call_status != 0:
            self.execute_adb_shell_command(cmd)


##class Relay():
    ##def __init__(self):
        ##self.ser = None

    ##def openPort(self, portname):
        ##try:
            ##if 'COM7' in portname and len(portname) == 4:
               ## self.ser = serial.Serial(0)
                ##self.ser.baudrate = 9600
                ##self.ser.bytesize = serial.EIGHTBITS
                ##self.ser.stopbits = serial.STOPBITS_ONE
                ##self.ser.timeout = 0
                ##self.ser.xonxoff = False  # disable software flow control
                ##self.ser.rtscts = False  # disable hardware (RTS/CTS) flow control
                ##self.ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
                ##self.ser.writeTimeout = 2  # timeout for write
            ##else:
                ##self.ser = serial.Serial(str(portname))
                ## g.write("AT+CSQ")
                ## print(g.readline())
                ##self.ser.port = str(portname)
                ##self.ser.baudrate = 19200
                ##self.ser.bytesize = serial.SEVENBITS
                ##self.ser.stopbits = serial.STOPBITS_TWO
            ##self.ser.parity = serial.PARITY_NONE
        ##except Exception:
    #  print "[ERROR] - Opening serial port: "
