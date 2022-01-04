import os

def remove_files_in_folder(files_path: str, *ext: str):
    """Method used to delete all the files with a given extensions
       inside a given folder and subfolders
       Args:
           files_path (str): folder where are all the files we want to delete (included subfolders)

           *ext: List of extensions to be deleted. Example: 'jpg', 'jpeg'

    """
    for folderName, subfolders, filenames in os.walk(files_path, topdown=True):

        for filename in filenames:
            if filename.endswith(ext):
                os.remove(folderName+'\\'+filename)


remove_files_in_folder('D:/OneDrive/alexca73myCode/Upwork2 - Transform png to jpg', 'jpg', 'jpeg')
