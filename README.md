<h1> Exploring Django Framework : Step-by-step </h1>


> [!TIP]
> Helpful advice: A better way to learn complicated tasks is reading the documentation (if available) and taking notes. I hope this might be useful.
<br>
<h3>Sketching</h3>
<br>
<ol>
    <li>I've learned a few key things to create a Django application. 
See as follows: </li>
    <ul>
        <li>Use the following steps to create a Django project:</li>
        <ol>
            <li>Create a virtual environment:</li>
            <ul>
                <li>python -m venv myworld</li>
                <ol>
                    <li>This will set up a venv and create a folder named "myword" with subfolders and files.</li>
                </ol>
            </ul>
            <li>Activate virtual environment:</li>
            <ul>
                <li>source myworld/bin/activate</li>
            </ul>
            <li>Install django:</li>
            <ul>
                <li>python -m pip install Django</li>
            </ul>
            <li>Create a django project:</li>
            <ul>
                <li>django-admin startproject my_log_app</li>
                <ol>
                    <li>This command create a django application. Django creates a my_log_app folder on my computer with subfolder and files.</li>
                </ol>
            </ul>
            <li>Use the following command to run the project:</li>
            <ul>
                <li>python manager.py runserver</li>
                <ol>
                    <li>Open a new window browser and type the IP address</li>
                </ol>
                <li>Modify your application in with the following steps to reach what you need:</li>
                <ol>
                    <li>Inside the my_log_app there will be the necessary structure to make you application work. </li>
                    <li>Let's start from views.py:</li>
                    <ul>
                        <li>Inside views.py will have to import HttpResponse and declare a function to send Http request:</li>
                        <ol>
                            <li>from django.http import HttpResponse</li>
                            <li>def my_log_app(request): return HttpResponse("Hello world")</li>
                        </ol>
                    </ul>
                </ol>
            </ul>
        </ol>
    </ul>
</ol>
