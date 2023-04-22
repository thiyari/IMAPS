import imaplib
import email

class DeleteSearch():
    def __init__(self, userid, passwd, fromaddr):
        self.userid = userid
        self.passwd = passwd
        self.fromaddr = fromaddr

    ################ IMAP SSL ##############################
    def DeleteProcess(self):
    ################ IMAP SSL ##############################
        with imaplib.IMAP4_SSL(host="imap.gmail.com", port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
            print("Connection Object : {}".format(imap_ssl))

            ############### Login to Mailbox ######################
            print("Logging into mailbox...")
            resp_code, response = imap_ssl.login(self.userid,self.passwd)

            print("Response Code : {}".format(resp_code))
            print("Response      : {}\n".format(response[0].decode()))

            ############### Set Mailbox #############
            resp_code, mail_count = imap_ssl.select(mailbox="INBOX", readonly=False)
            
            ############### Search and delete mails in a given Directory #############   
            resp_code, mails = imap_ssl.search(None, '(FROM "'+ self.fromaddr +'")')
            mail_ids = mails[0].decode().split()
            print("Total Mail IDs : {}\n".format(len(mail_ids)))

            print("Deleting Mails...")
            #for mail_id in mail_ids[:2]:
            for mail_id in mail_ids:
                resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)') ## Fetch mail data.
                message = email.message_from_bytes(mail_data[0][1]) ## Construct Message from mail data
                print("Mail ID : {}, Date : {}, Subject : {}".format(mail_id, message.get("Date"), message.get("Subject")))
                resp_code, response = imap_ssl.store(mail_id, '+FLAGS', '\\Deleted')
                print("Response Code : {}".format(resp_code))
                print("Response      : {}\n".format(response[0].decode()))

            resp_code, response = imap_ssl.expunge()
            print("Response Code : {}".format(resp_code))
            print("Response      : {}\n".format(response[0].decode()))
            
            ############# Close Selected Mailbox #######################
            print("\nClosing selected mailbox....")
            imap_ssl.close()

