Treehouse Python techdegree

Project 6

Jonathan Grenz

Forward:
As part of your job, you’ve been asked to build a website that displays information about various minerals (AKA rocks). The home page of the site contains a list of all of the minerals in a database. Clicking on a mineral’s name opens a page that displays information about the mineral.

A web designer has already designed the pages. You only need to write the code to created the pages as they’ve been designed. Use the included HTML/CSS files to see how to structure and style the pages. You don’t need to alter global.css - just use it as is.

Instruction:

Write a script to that constructs a mineral model instance for each mineral in minerals.json and saves them to a SQLite database.

Create a layout template for the app.
The layout template should contain the title of the site. You can name the site anything you want.

Create a template and view to show the names of all the minerals.
This view should display the name of each mineral in the database. Each name in the list is a link to the detail view of the mineral. See index.html and list-preview.png

Create a mineral details template and view.
The detail view should display the details of the selected mineral.

The details template should contain the mineral’s name, image, and image caption. Other details that are available about the mineral should be displayed below the image caption. See detail.html and detail-preview.png.

Use a template filter to display the name of each attribute in title case.
Write unit tests to test that each view is displaying the correct information.
Make the templates match the style used in the example files.
Look at the example HTML files and global.css to determine which id and class attributes to use on the elements in the pages you generate.

Extra Credit
To get an "exceeds" rating, complete all of the steps below:

 4 steps
To get an "exceeds" rating, you can expand on the project in the following ways:

Display the most common or important details at the top of the details list. You can decide on what order to display them in. The other miscellaneous details can be in any order.
Add a link that goes to a random mineral details page.
In addition to those provided, additional styles are added and used.
