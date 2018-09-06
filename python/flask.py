#file structure for css
/app
    - app_runner.py
    /services
        - app.py 
    /templates
        - mainpage.html
    /static
        /styles
            - mainpage.css
            
<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/mainpage.css') }}">

##
