# Gaze Task
The purpose of the gaze task app is to alternate between two images for N iterations, over a user-specified timescale, with support for eye-gaze contingency.

# Dependencies
- [PyGaze!] (http://www.pygaze.org/downloads)
- ArgparseUi

### Installation of dependencies
I will be operating under the assumption that the installation will be on a windows computer. If you're using Linux or OS X, I'll assume you know how to install dependencies using the terminal.

1. Download and unzip WinPython PyGaze to any location.
2. Navigate to the python directory and then the Scripts directory within. E.g. if WinPython-PyGaze-0.4 is located in the Downloads directory, navigate to `C:\Users\<username>\Downloads\WinPython-PyGaze-0.4\python-2.7.3\Scripts`.
3. From within Python2.7.3\Scripts, open a cmd shell by typing `cmd` into the explorer bar.
4. In the cmd shell, type `easy_install.exe argparseui`. Assuming you're connected to the internet, this will perform the download and installation of ArgparseUi to the WinPython's python.

# Installation of the Gaze Task
1. Download the Gaze Task repository as a zip file.
2. Navigate to the python directory and then the Scripts directory within your WinPython PyGaze directory. E.g. If your WinPython PyGaze directory is in your downloads directory, navigate to `C:\Users\<username>\Downloads\WinPython-PyGaze-0.4\python-2.7.3\Scripts`
3. From within the Python2.7.3\Scripts, open a cmd shell by typing `cmd` in the windows explorer bar.
4. In the cmd shell, type `easy_install.exe` and then drag and drop the gaze_task.zip file into the cmd shell and press enter to install the Gaze Task.
5. The install script will create an executable for the `run_script.py` which executes the gaze task: `run_gaze_task.exe`. The executable will be located in the same directory as dependency installer easy_install: `Python2.7.3\Scripts`. If you don't want to execute `run_gaze_task.exe` from a cmd shell each time, I recommend you create a shortcut by right clicking on `run_gaze_task.exe` and clicking on 'Create Shortcut' and then dragging the shortcut to wherever you want.

# Running the Gaze Task
The Gaze Task can be executed by either launching `run_gaze_task.exe` from a cmd shell or by double clicking on the shortcut that you created during installation. Once executed, the Gaze Task menu will pop up (*NOTE: on first execution, it may take a few seconds to load.*). Here you will input the parameters for your task.

After inputting all the parameters for your gaze task, click 'Save Settings' to save your settings. Or, if you have created task settings and saved them previously, click 'Load Settings'. An example settings file has been included in the repository. Once the settings look appropriate, go ahead and click 'OK' to launch the task.

NOTE: once you click 'OK', the task will start immediately.

# Task Parameters
- `n_iters`: This is the number of image switches that the task will perform. Image switches are contingent upon gaze unless in testing mode (more on testing below).
- `timing`: The amount of time that a single image is displayed in milliseconds. *Note: there is an appropriately 10ms overhead associated with the switching of the images.*
- `displaynumber`: The monitor (if in a multi-display environment) to show the gaze task. 0 is the 'main monitor' and all subsequent numbers are reserved for external monitors. I would recommend launching the task on the main monitor and then displaying the task on the external monitor.
- `resolution`: The resolution of the display which will be displaying the task, in pixels. E.g. a monitor 1920 pixels wide and 1080 pixels tall would be entered as `1920 1080`.
- `testing`: If you wish to run the task without the gaze contingency.
- `Image 1`: The full path to the first image in to be displayed by the gaze task. E.g. `C:\Users\skyler.grammer\Downloads\test_images\CPD.1point4.checkerboard2.28.jpg`.
- `Image 2`: The full path to the second image in to be displayed by the gaze task.

# Keeping Up-To-Date
To keep up-to-date, just perform the steps outlined in Installation of the Gaze Task again. The installation will overwrite the previously-installed code base and the executable.

# Contribution or Questions
Contact **skylergrammer@gmail.com** for permission to contribute or if you have questions/comments/grievences regarding installation or execution of the task.
