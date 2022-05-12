#!/usr/bin/env python3

# Include imports for making HTTP calls with requests, and parsing json files with json.
import requests
import json


# Read in user json file as string and parse to python dictionary
users = json.loads(open('users.json', 'r').read())

# Print first user details
print(json.dumps(users[0]))

# Read in todos json file as string and parse to python dictionary
todos = json.loads(open('todos.json', 'r').read())

# Print first of todos
print(json.dumps(todos[0]))

# Get posts via API
posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Extract the json body of the posts_response object - as a note, if this is not a structured json object,
# this operation will throw an exception
posts = posts_response.json()

# Print first comment
print(json.dumps(posts[0]))

# Get post comments via API
comments_response = requests.get('https://jsonplaceholder.typicode.com/comments')

# Extract the json body of the comments_response object - as a note, if this is not a structured json object,
# this operation will throw an exception
comments = comments_response.json()

# Print first comment
print(json.dumps(comments[0]))


# Task 1
#
# Get the city of the user with an ID of 7
# Note, we will be breaking out each step here, although many could be combined into smaller operations
#


# Create empty city variable to capture details with global scope, an empty string is fine, python will update
# it to a dictionary when it gets re-assigned
city = ''

# Loop through the posts, creating a temporary p variable to represent each post
for user in users:
    print(user)
    # Check to see if the p variables ID is equal to the ID from the comment
    if user['id'] == 7:
        city = user['address']['city']
        # No need to continue looping here so we will break out of it
        break
print(city)

# Task 2
#
# Get the post details for the first comment
# Note, we will be breaking out each step here, although many could be combined into smaller operations
#

# Create a variable for the first comment in the list
comment = comments[0]

# Create a variable for the postId element of the comment
first_comment_post_id = comment['postId']

# Create empty post details variable to capture details with global scope, an empty string is fine, python will update
# it to a dictionary when it gets re-assigned
post_details = ''

# Loop through the posts, creating a temporary p variable to represent each post
for p in posts:
    # Check to see if the p variables ID is equal to the ID from the comment
    if p['id'] == first_comment_post_id:
        post_details = p
        # No need to continue looping here so we will break out of it
        break

print(post_details)


# Task 3
#
# Modify the email address of the first comment to the forth user in your list
# Note, we will be breaking out each step here, although many could be combined into smaller operations
#

user_to_update = users[3]
user_to_update_email = user_to_update['email']
comments[0]['email'] = user_to_update_email

print(comments[0])

