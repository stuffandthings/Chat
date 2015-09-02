# Chat
Simple chat server and client implemented in Python.

The client has 2 components:
- Client View
- Client Interface

The client view is just simply a... well... view to see all messages from the chat server.

The interface is what the user interacts with and all messages typed into the interface are sent to the server.

As you can probably imagine, there's a redundant connection here; there's a connection for the interface and a connection for the view. This is just a simplification due to a time crunch. Dealing with stdin and stdout along with formatting in the command line wasn't something I knew how to do. The two components can be unified with a simple GUI thrown on top. This is why the MVC (Model-View-Controller) pattern is great.

### Usage:
- Run the server first: python server.py <host> <port>
- Then the view: python client_view.py <host> <port>
- Finally, the interface: python client_interface.py <username> <host> <port>
