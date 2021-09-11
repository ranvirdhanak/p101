from os import access
import dropbox
class TransferData:
    def __init__(self,upload_files):
        self.upload_files = upload_files

    def upload_file(self,file_from,file_to):
        """upload a file to dropbox using API v2"""
        dbx = dropbox.Dropbox(self.upload_files)

        with open(file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A4Hqf_ftKgaz8kt52Cq2Xac6hsBZbp1UX5XLKZ7HU_Z_z-Myy4TFoc83xDMTnno9yRa1UbNxZqecqTiVCKltbYrt90tp0xoOE-oUjLMTcLuEr49jr58ae4I2cxoblzLst-rCmIRhVwM'
    transferData = TransferData('upload_files')
    
    file_from = 'uploadFiles.py'
    file_to = '/uploadFiles.py'

    transferData.upload_file(file_from,file_to)

if __name__== '__main__':
    main()
    