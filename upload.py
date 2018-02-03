from ftplib import FTP

def upload(location):
	""" Uploads file backup.zip at location. """
	
	ftp = FTP('server.address.com')
	ftp_user='ftp username'
	ftp_passwd='ftp password'
	upload_directory = 'server\\destination\\directory'
	
	ftp.login(user=ftp_user, passwd=ftp_passwd)
	ftp.cwd(upload_directory)
		
	ftp.storbinary('STOR ' + 'backup.zip', open('backup.zip', 'rb'))