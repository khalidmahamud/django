from datetime import date

from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountain",
        "image": "mountains.jpg",
        "author": "Khalid",
        "date": date(2024, 6, 21),
        "title": "Mountain Hiking",
        "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Harum magnam quos consectetur at velit dolorem.",
        "content": 
            """Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae amet, tenetur dolorem soluta possimus eaque aspernatur laboriosam! Ipsam assumenda consequuntur dicta cum magni doloremque vitae quos. Cumque officiis sapiente reiciendis?
            
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Doloribus repellendus deserunt, facilis perferendis ducimus aliquid ipsam atque cupiditate! Autem molestias ducimus a iste temporibus minima quisquam commodi exercitationem. Dolore, quaerat!
            
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nemo sequi, officia modi quod, dolor fuga soluta sunt consequatur facere obcaecati voluptas ratione atque iusto vero voluptate dolores, voluptatibus harum minima.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Khalid",
        "date": date(2024, 5, 10),
        "title": "Programming is Great!",
        "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Harum magnam quos consectetur at velit dolorem.",
        "content":
            """Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae amet, tenetur dolorem soluta possimus eaque aspernatur laboriosam! Ipsam assumenda consequuntur dicta cum magni doloremque vitae quos. Cumque officiis sapiente reiciendis?
            
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Doloribus repellendus deserunt, facilis perferendis ducimus aliquid ipsam atque cupiditate! Autem molestias ducimus a iste temporibus minima quisquam commodi exercitationem. Dolore, quaerat!
            
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nemo sequi, officia modi quod, dolor fuga soluta sunt consequatur facere obcaecati voluptas ratione atque iusto vero voluptate dolores, voluptatibus harum minima.
        """,
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Khalid",
        "date": date(2024, 6, 21),
        "title": "Nature At Its Best",
        "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Harum magnam quos consectetur at velit dolorem.",
        "content": 
            """Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae amet, tenetur dolorem soluta possimus eaque aspernatur laboriosam! Ipsam assumenda consequuntur dicta cum magni doloremque vitae quos. Cumque officiis sapiente reiciendis?
            
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Doloribus repellendus deserunt, facilis perferendis ducimus aliquid ipsam atque cupiditate! Autem molestias ducimus a iste temporibus minima quisquam commodi exercitationem. Dolore, quaerat!
            
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nemo sequi, officia modi quod, dolor fuga soluta sunt consequatur facere obcaecati voluptas ratione atque iusto vero voluptate dolores, voluptatibus harum minima.
        """,
    },
]

def get_date(post):
    return post['date']

# Create your views here.


def home_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/home.html", {
        "posts": latest_posts,
    })


def posts_page(request):
    return render(request, "blog/posts.html", {
        "all_posts": all_posts,
    })


def single_post_page(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/single_post.html", {
        "post": identified_post,
    })
