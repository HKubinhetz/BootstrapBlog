# BootstrapBlog
Bootstrap Blog for 100 Days of Code!

This is a Blog website built with HTML + CSS (Bootstrap) and Python (Flask and Jinja).

![image](https://user-images.githubusercontent.com/31540553/159622947-5c1d53cd-f943-495d-a6de-43f700881111.png)

Every page is generated through a Flask code. Blog posts come from an API using requests (a separate python file called getposts.py was created for this API interaction alone).

Posts also have their link programatically built, so that there is scabilty in the application. The same code is able to render as much posts as needed.
It is recommended, however, to limit posts per page, or there will be infinite scrolling in the future.

![image](https://user-images.githubusercontent.com/31540553/159623447-6ea4ccdd-9567-4b75-82e4-9dea1b3b6fd6.png)

The last piece of code I made was building functionality for the form! To do so, I used the HTML form structure and the Request module from Flask. Finally, the form information was sent via e-mail through a simple smtplib application.

![Formgif](https://user-images.githubusercontent.com/31540553/160225027-f1342730-148a-4a1d-8bd5-982bf577af9b.gif)

This was a very fun project I had the opportunity to work! Eager for developing the next ones!

Feel free to contact me via any of the channels listed in my bio. Cheers!
