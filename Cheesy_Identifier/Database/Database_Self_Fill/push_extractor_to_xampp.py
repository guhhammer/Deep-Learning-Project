import shutil
import os

class preparator():
    def __init__(self, folder_name="Extractor_algorithm",
                 _source_ = ("\\".join(os.path.abspath(os.getcwd()).split("\\")[:-1])),
                 _dest_ = "C:\\xampp\\htdocs"):
        self.source = _source_+"\\"+folder_name
        self.dest = _dest_+"\\"+folder_name+"_Cheesy_Identifier"

    def copyDirectory(self):
        try:
            shutil.copytree(self.source, self.dest)
        # Directories are the same
        except shutil.Error as e:
            print('Directory not copied. Error: %s' % e)
        # Any error saying that the directory doesn't exist
        except OSError as e:
            print('Directory not copied. Error: %s' % e)

    def make(self):
        if os.path.isdir(self.dest):
            shutil.rmtree(self.dest)
        self.copyDirectory()
