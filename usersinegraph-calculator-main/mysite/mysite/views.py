import matplotlib
matplotlib.use("Agg")  # Use the backend that does not require an X server
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def generate_sine_graph(start, end, step):
    # Generate x values
    x = np.arange(start, end, step)

    # Generate y values (sine function)
    y = np.sin(x)

    # Create the plot
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sine Graph')

    # Save the plot to a temporary image file
    temp_img_path = os.path.join(settings.MEDIA_ROOT, 'sine_graph.png')
    plt.savefig(temp_img_path)
    plt.close()

    return settings.MEDIA_URL + 'sine_graph.png'

def generate_cosine_graph(start, end, step):
    # Generate x values
    x = np.arange(start, end, step)

    # Generate y values (cosine function)
    y = np.cos(x)

    # Create the plot
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cosine Graph')

    # Save the plot to a temporary image file
    temp_img_path = os.path.join(settings.MEDIA_ROOT, 'cosine_graph.png')
    plt.savefig(temp_img_path)
    plt.close()

    return settings.MEDIA_URL + 'cosine_graph.png'

def generate_tan_graph(start, end, step):
    # Generate x values
    x = np.arange(start, end, step)

    # Generate y values (tangent function)
    y = np.tan(x)

    # Create the plot
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Tangent Graph')

    # Save the plot to a temporary image file
    temp_img_path = os.path.join(settings.MEDIA_ROOT, 'tangent_graph.png')
    plt.savefig(temp_img_path)
    plt.close()

    return settings.MEDIA_URL + 'tangent_graph.png'

def generate_graph(request):
    if request.method == 'POST':
        # Get user input from the form
        start = float(request.POST.get('start'))
        end = float(request.POST.get('end'))
        step = float(request.POST.get('step'))
        graph_type = request.POST.get('graph_type')

        # Generate the appropriate graph based on user selection
        if graph_type == 'sine':
            image_path = generate_sine_graph(start, end, step)
        elif graph_type == 'cosine':
            image_path = generate_cosine_graph(start, end, step)
        elif graph_type == 'tangent':
            image_path = generate_tan_graph(start, end, step)
        else:
            # Default to generating a sine graph if no graph type is selected
            image_path = generate_sine_graph(start, end, step)

        # Prepare the context data to pass to the template
        context = {'graph_generated': True, 'image_path': image_path}
        return render(request, 'graph.html', context)

    return render(request, 'graph.html')


def index(request):
    return render(request, 'index.html')
