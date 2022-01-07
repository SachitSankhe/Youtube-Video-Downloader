# pip install --upgrade pytube


# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
    head_label = Label(window, text="YouTube Video Downloader Using Tkinter",
                       padx=15,
                       pady=15,
                       font="Roboto",
                       bg="#B3E81C",
                       fg="black")
    head_label.grid(row=1,
                    column=1,
                    pady=25,
                    padx=10,
                    columnspan=3)

    link_label = Label(window,
                       text="YouTube link :- ",
                       font="Roboto",
                       bg="darkblue",
                       fg="Yellow",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=10,
                    padx=5)

    window.linkText = Entry(window,
                            width=40,
                            textvariable=video_Link,
                            font="Roboto")
    window.linkText.grid(row=2,
                         column=1,
                         pady=5,
                         padx=5,
                         columnspan=2)

    destination_label = Label(window,
                              text="Destination :",
                              bg="darkblue",
                              fg="Yellow",
                              font="Roboto",
                              pady=5,
                              padx=20)
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)

    window.destinationText = Entry(window,
                                   width=27,
                                   textvariable=download_Path,
                                   font="Roboto")
    window.destinationText.grid(row=3,
                                column=1,
                                pady=5,
                                padx=5)

    browse_B = Button(window,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(window,
                        text="Download the Video",
                        command=Download,
                        width=20,
                        bg="#34D831",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Roboto")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)


# Defining Browse() to select a
# destination folder to save the video

def Browse():
    # Presenting user with a pop-up for
    # directory selection. initial dir
    # argument is optional Retrieving the user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)


# Defining the  Download() function to download the video containing the video link
# and also asking where to save the video


def Download():
    Youtube_link = video_Link.get()

    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()

    # getting user-input Youtube Link
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)

    try:
        getVideo = YouTube(Youtube_link)
    except:
        messagebox.showerror("showerror", "The video link field is not correct,try again")

    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the list and filtering the video for 720p resolution
    try:
        videoStream = getVideo.streams.filter(res="720p").first()
    except:
        videoStream = getVideo.streams.first()

    # Downloading the video to destination directory
    videoStream.download(download_Folder)

    # Displaying the message
    messagebox.showinfo("showinfo", "SUCCEESFULLY DOWNLOADED IN\n" + download_Folder)


# Creating object of tk class
window = Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property

window.title("YouTube Video Downloader")
# Add image file
bg = PhotoImage(file="bg.png")

# Show image using label
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

window.config(background="#4db9d5")
window.geometry("720x380")
window.resizable(False, False)

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
window.mainloop()


