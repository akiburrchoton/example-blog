from django.shortcuts import render
import requests

# POSTS VIEW ENDPOINT
def posts(request):

    responses = requests.get('https://jsonplaceholder.typicode.com/posts').json


    return render(request, 'blog-listing.html', {'responses': responses})


# POST DETAILS VIEW ENDPOINT
def post_details(request, post_id):
    responses = requests.get('https://jsonplaceholder.typicode.com/posts/'+str(post_id)).json 
    url = 'https://jsonplaceholder.typicode.com/posts/'+ str(post_id) + '/comments'
    comments = requests.get(url).json

    context={
        'responses': responses,
        'comments': comments,
        }
    return render(request, 'blog-post.html', context)