Main Idea:
- You create an account, then choose someone from the list to start a dialogue. 
- You are able to see the chat history and whether the user is on-line.
- You are able to send pics and gifs. They are stored.
- So it is kind of a replica of WhatsApp or Telegram app but with fewer features.

Technologies I`m going to use:
* I will use Django and DRF (if there is any point in it, not sure).
* Postgres will store most of the info, but I need to research if it is a suitable solution if there are more than 2 chats.
* Maybe I`ll use Redis to store the client sessions parameters, but not sure.
* I would like to launch the app using Docker and nginx.
* Frontend ??? (Oh god, not ExtJs again...) Maybe I`ll give Vue or Node.js a try.
* To be continued...

TODO:
* Create Djngo app, make db schema (User, Chat, etc.).
* Make an authentication form.
* Create basic layout for the main page.
* Make tests.
* To be continued...
