html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale="1.0">
<title>Horizontal Navigation Menu</title>
<style>
.navbar ul{
	list-style-type: none;
    padding: 0;
    margin: 0;
    overflow: hidden;
    background-color: grey;
}

.navbar ul li {
    float: left;
}

.navbar ul li a {
	display: block;
    color: blue;
    text-align: center;
    padding: 14px 20px;
    text-decoration: none;
}

.navbar ul li a:hover{
	background-color: #ccc;
 	color: red;
}

</style>
</head>
<body>
<nav class="navbar">
<ul>
<li><a href="#home">Home</a></li>
<li><a href="#about">About</a></li>
<li><a href="contact">Contact</a></li>
</ul>
"""

with open('nav_menu.html', 'w') as file: 
    file.write(html_content)
    
print('Html and Css for navigation menu generated in "nav_menu.html"')