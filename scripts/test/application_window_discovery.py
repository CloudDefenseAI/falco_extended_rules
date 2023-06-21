import subprocess

# Get the window ID of the currently active window
active_window_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()

# Get information about the active window
active_window_info = subprocess.check_output(['xwininfo', '-id', active_window_id]).decode().strip()

# Get a list of all open windows
window_list = subprocess.check_output(['wmctrl', '-l']).decode().strip().split('\n')

# Get information about each open window
for window in window_list:
    window_id = window.split()[0]
    window_info = subprocess.check_output(['xwininfo', '-id', window_id]).decode().strip()
    print(window_info)

# Get a list of all open applications
app_list = subprocess.check_output(['xlsclients']).decode().strip().split('\n')

# Get information about each open application
for app in app_list:
    app_id = app.split()[0]
    app_info = subprocess.check_output(['xprop', '-id', app_id]).decode().strip()
    print(app_info)

# Monitor events in the X server
xev_process = subprocess.Popen(['xev'], stdout=subprocess.PIPE)
for line in iter(xev_process.stdout.readline, ''):
    print(line.decode())

