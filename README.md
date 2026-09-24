# Android Device & Sanitization Suite

A lightweight command-line tool designed to streamline Android hardware triage, pull system specifications over ADB, export inventory intake reports, and execute controlled sanitization.

## Overview
* **`phone_triage.py`**: Safe, non-destructive diagnostic intake tool. Queries ADB properties, parses device hardware specs, and logs them to a CSV spreadsheet.
* **`wipe_device.py`**: Independent sanitization utility requiring manual serial verification before issuing factory recovery triggers.

## Prerequisites
* Python 3.8+
* Android Debug Bridge (`adb`) installed and added to system PATH
* Target device with **USB Debugging** enabled