import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
        
    def uploadingFiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from,"rb") as file:
            dbx.files_upload(file.read(),file_to,mode=WriteMode("overwrite"))
        

def main():
    access_token = "enter your access token"
    transfer_data = TransferData(access_token)
    file_from = input("Enter the file Path : ")
    file_to = "abc.txt"        
    if transfer_data.uploadingFiles(file_from,file_to):
    
        print("File/Files has been moved!")
    else:
        print("Didn't get uploaded due to a problem")
    
if __name__ == '__main__':
    main()