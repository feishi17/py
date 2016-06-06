import sys, getopt, smtplib
def main():
    """
       Send an email via qianyang.code@gmail.com.
       EXAMPLE: python email_qian.py -s <Subject> -c <Context>
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:c:h")
        #, ["Subject", "Context", "help"])
    except getopt.GetoptError:
        usage()

    if len(opts)<1:
        print 'Warning: No input.'
        usage()

    Subject = "No Subject"
    Context = "No context"
    for o, a in opts:
        if o == "-s":
            Subject = a
        if o == "-c":
        	Context = a
       	if o == '-h':
       		usage()

    from_email = "example_from@gmail.com"
    password = 'pwd'
    to_email  = "example_to@example2.com"
    msg = "\r\n".join([
	  "From: " + from_email,
	  "To: " + to_email,
	  "Subject: "+Subject,
	  "",
	  Context
	  ])
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg)
    server.quit()
    print "Email sent successfully!"

def usage():
    print "\n\tUSAGE: python email_qian.py -s <Subject> -c <Context>"
    sys.exit(1)

if __name__ == "__main__":
    main()
