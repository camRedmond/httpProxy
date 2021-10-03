Creators:
	redm7920 - Cameron Redmond
	oged9220 - Olorunfemi Ogedengbe


How To Run

	1) Navigate to the installation of program in command window / terminal

	2) Have python 3.5+ installed on machine

	3) type 'python proxy.py {port number}'
		where 'port number' is the port you wish to access proxy on
		
	4) open prefered browser and navigate to 'localhost:{port number}/{web page}'
		where port number is same as proxy port number,
		and web page is the url of the page requested (ex. 'example.com')
		
		* If connection is slow, and terminal does not connect right away, ctrl+c (ctrl on windows)
			will try to close the connection but force an update. The program is still fully functional from
			here or you can try again and hope it does not lag.
		
		** Persistent HTTP, so multiple requests may be made on different local client browsers
			using multiprocessing
		
	5) Web browser will update with requested site information within local client browser.
		Terminal output is neatly formatted and printed to display processes during execution.
		
		**NOTE: some web pages take some time to load. (a few minutes for some)
				In this state the terminal is also loading processes,
				and can be updated by sending another request in another window

	6) Upon errors a custom error page has been made for most common errors. The design choice in
		this stage was simplicity. Having a simple fluent error the user can understand and readjust the request.
		*The program in this state will continue to run and more requests can be made*
		
	7) The program keeps track of all cached webpages through a file system within the application,
		checking if it can open the file and therefore already in the cache or it creates the file
		and includes all cache information to be read again.
		*Cache can be made in one execution then read from another execution later*
	
*Troubleshooting*
	there is a common error where the program seems to freeze and appear like it is not working. a quick fix is to send another request to update the processes
	or to (ctrl + c on windows) to manually refresh when hung. If problem persists, restart code
	
	clearing the browser cache is also a good idea if you are running the program a lot


Server -> Proxy Receiving Messages
	*None of the sites provided work, example.com recently*
	*Thru 'whynohttps.com' I have found suitable http sites to test, url's will be included

	~~ ukbsc.info ~~
		~Client -> Proxy -> Server
			GET /ukbsc.info HTTP/1.1
			Host: localhost:1234
			User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
			Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
			Accept-Language: en-US,en;q=0.5
			Accept-Encoding: gzip, deflate
			Connection: keep-alive
			Cookie: has_js=1
			Upgrade-Insecure-Requests: 1
			DNT: 1
			Sec-GPC: 1
		
		~Server -> Proxy -> Client
			'HTTP/1.1 200 OK\r\n'
			'Date: Wed, 10 Feb 2021 23:47:42 GMT\r\n'
			'Server: Apache\r\n'
			'X-Content-Type-Options: nosniff\r\n'
			'X-Powered-By: PHP/7.2.27\r\n'
			'X-Drupal-Cache: MISS\r\n'
			'Expires: Sun, 19 Nov 1978 05:00:00 GMT\r\n'
			'Cache-Control: public, max-age=10800\r\n'
			'X-Content-Type-Options: nosniff\r\n'
			'Content-Language: en\r\n'
			'X-Frame-Options: SAMEORIGIN\r\n'
			'X-Generator: Drupal 7 (http://drupal.org)\r\n'
			'Last-Modified: Wed, 10 Feb 2021 23:47:42 GMT\r\n'
			'Vary: Cookie,Accept-Encoding\r\n'
			'Content-Type: text/html; charset=utf-8\r\n'
			'X-Varnish: 231474156 229999437\r\n'
			'Age: 849\r\n'
			'Via: 1.1 varnish-v4\r\n'
			'ETag: W/"1613000862-1"\r\n'
			'grace: none\r\n'
			'Transfer-Encoding: chunked\r\n'



	~~ weevil.info ~~
		~Client -> Proxy -> Server
			GET /weevil.info HTTP/1.1
			Host: localhost:1234
			User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
			Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
			Accept-Language: en-US,en;q=0.5
			Accept-Encoding: gzip, deflate
			Connection: keep-alive
			Cookie: has_js=1
			Upgrade-Insecure-Requests: 1
			DNT: 1
			Sec-GPC: 1
			
		~Server -> Proxy -> Client
			'HTTP/1.1 200 OK\r\n'
			'Date: Wed, 10 Feb 2021 23:20:25 GMT\r\n'
			'Server: Apache\r\n'
			'X-Content-Type-Options: nosniff\r\n'
			'X-Powered-By: PHP/7.2.27\r\n'
			'X-Drupal-Cache: MISS\r\n'
			'Expires: Sun, 19 Nov 1978 05:00:00 GMT\r\n'
			'Cache-Control: public, max-age=10800\r\n'
			'X-Content-Type-Options: nosniff\r\n'
			'Content-Language: en\r\n'
			'X-Frame-Options: SAMEORIGIN\r\n'
			'X-Generator: Drupal 7 (http://drupal.org)\r\n'
			'Last-Modified: Wed, 10 Feb 2021 23:20:25 GMT\r\n'
			'Vary: Cookie,Accept-Encoding\r\n'
			'Content-Type: text/html; charset=utf-8\r\n'
			'X-Varnish: 231343193 227934585\r\n'
			'Age: 2664\r\n'
			'Via: 1.1 varnish-v4\r\n'
			'ETag: W/"1612999225-1"\r\n'
			'grace: none\r\n'
			'Transfer-Encoding: chunked\r\n'



	~~ xanga.com ~~
		~Client -> Proxy -> Server
			GET /xanga.com HTTP/1.1
			Host: localhost:1234
			User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
			Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
			Accept-Language: en-US,en;q=0.5
			Accept-Encoding: gzip, deflate
			Connection: keep-alive
			Cookie: has_js=1
			Upgrade-Insecure-Requests: 1
			DNT: 1
			Sec-GPC: 1
			
		~Server -> Proxy -> Client
			'HTTP/1.1 200 OK\r\n'
			'Date: Thu, 11 Feb 2021 00:01:09 GMT\r\n'
			'Content-Type: text/html; charset=utf-8\r\n'
			'Content-Length: 20300\r\n'
			'Last-Modified: Wed, 10 Feb 2021 20:12:28 GMT\r\n'
			'Connection: keep-alive\r\n'
			'Keep-Alive: timeout=15\r\n'
			'Vary: Accept-Encoding\r\n'
			'ETag: "60243e2c-4f4c"\r\n'
			'X-Frame-Options: SAMEORIGIN\r\n'
			'Accept-Ranges: bytes\r\n'
			'\r\n'
			'<!DOCTYPE html>\n'
			'\n'
			'<!-- hooks for IE foolishness \n'
			'see: http://paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->\n'
			'\n'
			'<!-- hooks for IE foolishness -->\n'
			'\n'
			'<!--[if lt IE 7]><html lang="en" class="ie ie6"><![endif]-->\n'
			'<!--[if IE 7]><html lang="en" class="ie ie7"><![endif]-->\n'
			
			
			
	~~ e-m-b.org ~~
		~Client -> Proxy -> Server
			GET /e-m-b.org HTTP/1.1
			Host: localhost:1234
			User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
			Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
			Accept-Language: en-US,en;q=0.5
			Accept-Encoding: gzip, deflate
			Connection: keep-alive
			Cookie: has_js=1
			Upgrade-Insecure-Requests: 1
			DNT: 1
			Sec-GPC: 1
			
		~Server -> Proxy -> Client
			'HTTP/1.1 200 OK\r\n'
			'Date: Wed, 10 Feb 2021 23:46:46 GMT\r\n'
			'Server: Apache\r\n'
			'X-Content-Type-Options: nosniff\r\n'
			'X-Powered-By: PHP/7.2.27\r\n'
			'X-Drupal-Cache: MISS\r\n'
			'Expires: Sun, 19 Nov 1978 05:00:00 GMT\r\n'
			'Cache-Control: public, max-age=10800\r\n'
			'X-Content-Type-Options: nosniff\r\n'
			'Content-Language: en\r\n'
			'X-Frame-Options: SAMEORIGIN\r\n'
			'X-Generator: Drupal 7 (http://drupal.org)\r\n'
			'Last-Modified: Wed, 10 Feb 2021 23:46:46 GMT\r\n'
			'Vary: Cookie,Accept-Encoding\r\n'
			'Content-Type: text/html; charset=utf-8\r\n'
			'X-Varnish: 224202019 230949971\r\n'
			'Age: 1199\r\n'
			'Via: 1.1 varnish-v4\r\n'
			'ETag: W/"1613000806-1"\r\n'
			'grace: none\r\n'
			'Transfer-Encoding: chunked\r\n'
			


	~~ go.com ~~ (moved to disney.com, error 302)
		~Client -> Proxy -> Server
			GET /go.com HTTP/1.1
			Host: localhost:1234
			User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
			Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
			Accept-Language: en-US,en;q=0.5
			Accept-Encoding: gzip, deflate
			Connection: keep-alive
			Cookie: has_js=1
			Upgrade-Insecure-Requests: 1
			DNT: 1
			Sec-GPC: 1
			
		~Server -> Proxy -> Client
			'HTTP/1.1 302 Found\r\n'
			'Date: Thu, 11 Feb 2021 02:20:21 GMT\r\n'
			'Server: Apache/2.4.46 (Unix)\r\n'
			'Location: https://www.disney.com/\r\n'
			'Content-Length: 207\r\n'
			'Content-Type: text/html; charset=iso-8859-1\r\n'
			'\r\n'
			'<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n'
			'<html><head>\n'
			'<title>302 Found</title>\n'
			'</head><body>\n'
			'<h1>Found</h1>\n'
			'<p>The document has moved <a href="https://www.disney.com/">here</a>.</p>\n'
			'</body></html>\n'



list of pages:
example.com
e-m-b.org
weevil.info
ukbsc.info
zootaxa.info
xanga.com
apache.org
go.com
