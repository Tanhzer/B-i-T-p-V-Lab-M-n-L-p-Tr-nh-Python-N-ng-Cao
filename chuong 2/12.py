import http.client
import json

def fetch_posts():
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET", "/posts")

    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read()
        posts = json.loads(data)
        return posts
    else:
        print("Error fetching posts:", response.status)
        return []

def display_posts(posts):
    print(f"Tổng số bài post: {len(posts)}\n")
    print("Danh sách các bài post:")
    for post in posts:
        print(f"User ID: {post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)  # Đường phân cách giữa các bài post

def main():
    posts = fetch_posts()
    display_posts(posts)

if __name__ == "__main__":
    main()
