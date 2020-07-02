import sys

os = "windows"
try:
	from ctypes import wintypes, windll, create_unicode_buffer
except:
	os = "linux"

# copied from SO
def getActiveTitle():
	if os == "windows":
		hWnd = windll.user32.GetForegroundWindow()
		length = windll.user32.GetWindowTextLengthW(hWnd)
		buf = create_unicode_buffer(length + 1)
		windll.user32.GetWindowTextW(hWnd, buf, length + 1)
		return buf.value if buf.value else None
	else:
		


while True:
	print(getActiveTitle())
	break