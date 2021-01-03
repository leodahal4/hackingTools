## ADB Commands

Information obtained from: http://adbshell.com/​

### Connection

> adb devices

This indicates to the device that it has to start and adb server in port 5555:

> adb tcpip 5555

Connect to that IP and that Port:

> adb connect <IP>:<PORT>

### Packet Manager
#### Install/Uninstall

> adb install [option] <path>

> adb install test.apk

> adb install -l test.apk forward lock application

> adb install -r test.apk replace existing application

> adb install -t test.apk allow test packages

> adb install -s test.apk install application on sdcard

> adb install -d test.apk allow version code downgrade

> adb install -p test.apk partial application install

adb uninstall [options] <PACKAGE>

> adb uninstall com.test.app

> adb uninstall -k com.test.app Keep the data and cache directories around after package removal.

### Packages

Prints all packages, optionally only those whose package name contains the text in <FILTER>.
__adb shell pm list packages [options] <FILTER-STR>__

> adb shell pm list packages <FILTER-STR>

> adb shell pm list packages -f <FILTER-STR> #See their associated file.

> adb shell pm list packages -d <FILTER-STR> #Filter to only show disabled packages.

> adb shell pm list packages -e <FILTER-STR> #Filter to only show enabled packages.

> adb shell pm list packages -s <FILTER-STR> #Filter to only show system packages.

> adb shell pm list packages -3 <FILTER-STR> #Filter to only show third party packages.

> adb shell pm list packages -i <FILTER-STR> #See the installer for the packages.

> adb shell pm list packages -u <FILTER-STR> #Also include uninstalled packages.

> adb shell pm list packages --user <USER_ID> <FILTER-STR> #The user space to query.

### adb shell pm path <PACKAGE>

Print the path to the APK of the given .

> adb shell pm path com.android.phone

__adb shell pm clear <PACKAGE>__

Delete all data associated with a package.

> adb shell pm clear com.test.abc

### File Manager

__adb pull <remote> [local]__

Download a specified file from an emulator/device to your computer.

> adb pull /sdcard/demo.mp4 ./

__adb push <local> <remote>__

Upload a specified file from your computer to an emulator/device.

> adb push test.apk /sdcard

__Screencapture/Screenrecord__

__adb shell screencap <filename>__

Taking a screenshot of a device display.

> adb shell screencap /sdcard/screen.png

__adb shell screenrecord [options] <filename>__

Recording the display of devices running Android 4.4 (API level 19) and higher.

> adb shell screenrecord /sdcard/demo.mp4

> adb shell screenrecord --size <WIDTHxHEIGHT>

> adb shell screenrecord --bit-rate <RATE>

> adb shell screenrecord --time-limit <TIME> #Sets the maximum recording time, in seconds. The default and maximum value is 180 (3 minutes).

> adb shell screenrecord --rotate # Rotates 90 degrees

> adb shell screenrecord --verbose

(press Ctrl-C to stop recording)

__You can download the files (images and videos) using adb pull__

### Shell

__adb shell__

Get a shell inside the device

> adb shell

__adb shell <CMD>__

Execute a command inside the device

> adb shell ls

### Processes

If you want to get the PID of the process of your application you can execute:

> adb shell ps

And search for your application

Or you can do

> adb shell pidof com.your.application

And it will print the PID of the application

### System

> adb root

Restarts the adbd daemon with root permissions. Then, you have to conenct again to the ADB server and you will be root (if available)

> adb sideload <update.zip>

flashing/restoring Android update.zip packages.

### Logs
#### Logcat

To filter the messages of only one application, get the PID of the application and use grep (linux/macos) or findstr (windows) to filter the output of logcat:

> adb logcat | grep 4526

> adb logcat | findstr 4526

adb logcat [option] [filter-specs]

> adb logcat

Notes: press Ctrl-C to stop monitor

> adb logcat *:V lowest priority, filter to only show Verbose level

> adb logcat *:D filter to only show Debug level

> adb logcat *:I filter to only show Info level

> adb logcat *:W filter to only show Warning level

> adb logcat *:E filter to only show Error level

> adb logcat *:F filter to only show Fatal level

> adb logcat *:S Silent, highest priority, on which nothing is ever printed

__adb logcat -b <Buffer>__

> adb logcat -b radio View the buffer that contains radio/telephony related messages.

> adb logcat -b event View the buffer containing events-related messages.

> adb logcat -b main default

> adb logcat -c Clears the entire log and exits.

> adb logcat -d Dumps the log to the screen and exits.

> adb logcat -f test.logs Writes log message output to test.logs .

> adb logcat -g Prints the size of the specified log buffer and exits.

> adb logcat -n <count> Sets the maximum number of rotated logs to <count>. 

### dumpsys

dumps system data
__adb shell dumpsys [options]__

> adb shell dumpsys

> adb shell dumpsys meminfo

> adb shell dumpsys battery

Notes: A mobile device with Developer Options enabled running Android 5.0 or higher.

> adb shell dumpsys batterystats collects battery data from your device

Notes: Battery Historian converts that data into an HTML visualization. STEP 1 adb shell dumpsys batterystats > batterystats.txt STEP 2 python historian.py batterystats.txt > batterystats.html

> adb shell dumpsys batterystats --reset erases old collection data

adb shell dumpsys activity

### Backup

Backup an android device from adb.

> adb backup [-apk] [-shared] [-system] [-all] -f file.backup

> # -apk -- Include APK from Third partie's applications

> # -shared -- Include removable storage

> # -system -- Include system Applciations

> # -all -- Include all the applications
