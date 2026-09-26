[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (used for Android application ID)
package.domain = org.example

# (str) Main entry point
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg,jpeg,atlas,ttf,otf,json

# (list) Application requirements
requirements = python3,kivy

# (str) Application version
version = 0.1

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) Android API target
android.api = 35

# (str) Minimum Android API
android.minapi = 24

# (str) Android NDK version
android.ndk = 28c

# (str) Android architecture(s)
android.archs = arm64-v8a

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True

# (list) Android permissions (add only those your app needs)
# android.permissions = INTERNET

# (str) Presplash image (optional; uncomment and set a path)
# presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon (optional; uncomment and set a path)
# icon.filename = %(source.dir)s/assets/icon.png

# (list) Python files and resources are included from source.dir.
# Keep main.py and this buildozer.spec in the same project folder.

[buildozer]

# (int) Log level: 2 = informational, 1 = debug
log_level = 2

# (int) Display warnings
warn_on_root = 1
