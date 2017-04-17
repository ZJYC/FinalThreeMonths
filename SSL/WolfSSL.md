
# Application Note #

## As for client,The usage is as following ##

###brief
The ssl socket derived from a normal socket,So the main mind is ,create a normal socket,then connect it to remote socket,then bind it with the ssl socket.Finally using ssl's api to send or recv data.
###details:

####0 prvInitialiseWolfSSL()

just initialize the SSL module

####1 wolfSSL_CTX_new()
example:

	xWolfSSL_ClientContext = wolfSSL_CTX_new( wolfTLSv1_2_client_method() );

create a ssl context

####2 wolfSSL_CTX_load_verify_locations

example:

	lReturned = wolfSSL_CTX_load_verify_locations( xWolfSSL_ClientContext, "ca-cert.pem", 0 );

just load a certification to identify yourself

####3 Create a socket and connect it

example:

    xClientSocket = socket( AF_INET, SOCK_STREAM, 0 );

	connect( xClientSocket, ( SOCKADDR * ) &xConnection, sizeof( xConnection ) )

####4 Create a SSL object

example:

    xWolfSSL_Object = wolfSSL_new( xWolfSSL_ClientContext );

####5 Associate the SSL object with created socket

example:

    lReturned = wolfSSL_set_fd( xWolfSSL_Object, xClientSocket );

####6 Use wolfSSL_write and wolfSSL_read to operate data transfer

example:

    lReturned = wolfSSL_write( xWolfSSL_Object, cString, strlen( cString ) + 1 );

####7 Stop SSL connect and clear the source

example:

			wolfSSL_free( xWolfSSL_Object );
			closesocket( xClientSocket );

## As for sercer,The usage is as following ##

####0 prvInitialiseWolfSSL();

####1 Create server socket

	xListeningSocket = prvOpenServerSocket();

####2 accpet the client connect

	xConnectedSocket = accept( xListeningSocket, ( struct sockaddr * ) &xClient, &xClientAddressLength );

####3 create ssl object

	xWolfSSL_Object = wolfSSL_new( xWolfSSL_ServerContext );

####4 bind to socket

	xReturned = wolfSSL_set_fd( xWolfSSL_Object, xConnectedSocket );

####5 like client read or write

	lBytes = wolfSSL_read( xWolfSSL_Object, cReceivedString, sizeof( cReceivedString ) );

####6 close and clear

	closesocket( xConnectedSocket );
	wolfSSL_free( xWolfSSL_Object );

# **That's all,Now is 2017--04--17--11--17--03,and I am ZJYC** #

















