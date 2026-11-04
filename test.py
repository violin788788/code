import sys
sys.path.insert(0, r"A:\\Users\\-\\code")
from utils import *
from pathlib import Path

import webview
class API:
    def hello(self):
        print("Hello from Python!")
html="<html><body><h1>Face Swapper</h1><button onclick=\"pywebview.api.hello()\">Click me</button></body></html>"
api=API()
webview.create_window("Face Swapper",html=html,js_api=api,width=800,height=600)
webview.start(gui="mshtml")
