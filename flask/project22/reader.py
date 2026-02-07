from imapclient import IMAPClient
import pyzmail
import ssl

HOST = "imap.gmail.com"
PORT = 993
USERNAME = "shubham1singh23@gmail.com"
PASSWORD = "nvutubnhfawyocpj"   # App password

def read_latest():
    # SSL fix for Python 3.13 (DEV ONLY)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    server = IMAPClient(
        HOST,
        port=PORT,
        ssl=True,
        ssl_context=ssl_context
    )

    server.login(USERNAME, PASSWORD)
    server.select_folder("INBOX")

    messages = server.search()
    if not messages:
        server.logout()
        return None, None

    last_uid = messages[-1]
    raw = server.fetch([last_uid], ["BODY[]"])

    msg = pyzmail.PyzMessage.factory(
        raw[last_uid][b"BODY[]"]
    )

    subject = msg.get_subject()
    body = ""

    if msg.text_part:
        body = msg.text_part.get_payload().decode(
            msg.text_part.charset
        )

    server.logout()
    return subject, body
