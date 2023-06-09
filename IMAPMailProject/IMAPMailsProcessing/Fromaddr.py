import imaplib
import email

class FromaddrSearch():
    def __init__(self, userid, passwd):
        self.userid = userid
        self.passwd = passwd
    ################ IMAP SSL ##############################
    def FromProcess(self):
        with imaplib.IMAP4_SSL(host="imap.gmail.com", port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
            print("Connection Object : {}".format(imap_ssl))
            records = []
            ############### Login to Mailbox ######################
            print("Logging into mailbox...")
            resp_code, response = imap_ssl.login(self.userid,self.passwd)

            print("Response Code : {}".format(resp_code))
            print("Response      : {}\n".format(response[0].decode()))

            ############### Set Mailbox #############
            resp_code, mail_count = imap_ssl.select(mailbox="Inbox", readonly=True)

            ############### Retrieve Mail IDs for given Directory #############   
            resp_code, mails = imap_ssl.search(None, 'All')
            print("Mail IDs : {}\n".format(mails[0].decode().split()))

            ############### Display Few Messages for given Directory #############
            for mail_id in mails[0].decode().split():
                print("================== Start of Mail [{}] ====================".format(mail_id))
                resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)') ## Fetch mail data.
                message = email.message_from_bytes(mail_data[0][1]) ## Construct Message from mail data

                #print("From       : {}".format(message.get("From")))
                #print("To         : {}".format(message.get("To")))
                #print("Bcc        : {}".format(message.get("Bcc")))
                #print("Date       : {}".format(message.get("Date")))
                #print("Subject    : {}".format(message.get("Subject")))

                #print("Body : ")
                #for part in message.walk():
                    #if part.get_content_type() == "text/plain":
                        #body_lines = part.as_string().split("\n")
                        
                        #print("\n".join(body_lines[:12])) ### Print first 12 lines of message
                records.append({"fromaddress":message.get("From")})
                
            
                #print("================== End of Mail [{}] ====================\n".format(mail_id))

            ############# Close Selected Mailbox #######################
            print("\nClosing selected mailbox....")
            imap_ssl.close()
        return records

