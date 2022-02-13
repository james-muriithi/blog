# Epic Blog
Created by James Muriithi on 12-02-2022
## Description
A web application where users you can create and share their opinions and people can read and comment on them.
# Setup / Installation
* clone the repo:

```shell
git clone https://github.com/james-muriithi/blog.git
```

```
cd blog
```
* create virtual environment 

```shell
python3.8 -m venv --without-pip venv
```

* To activate the virtual environment
```shell
source venv/bin/activate
```

* install the packages from requirements.txt
```shell
pip install -r requirements.txt 
```

* setup environment variables
```shell
cp .env.example .env
```
* Execute the shell script and start the server
```shell
chmod a+x start.sh
./start.sh
```
* open the browser and navigate to http://127.0.0.1:5000/ to see the application in action


## Technologies Used
The following languages have been used on this project:

* HTML
* CSS
* JS
* Bootstrap
* Flask
* Python
* Cloudinary (for image upload)

## Live Link
[Click Here](https://epic-blogs.herokuapp.com/)

## Design
[Here is the figma design of the app](https://www.figma.com/file/fxVWP4Fm5LfR1zCksAzZzN/Untitled?node-id=2%3A5)

## Screenshot
![Screenshot](./screenshots/screenshot.png)

## MIT licence

<p>Copyright (c) 2022 Moringa School </p>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

