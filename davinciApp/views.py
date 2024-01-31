
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, BlogSection
from .functions import generateBlogTopicIdeas, generateBlogSectionTitles, generateBlogSectionDetails
# Create your views here.

def home(request):
    return render (request, 'blog-topic.html')


def blogTopic(request):
    context = {}

    if request.method == "POST":
        blogIdea = request.POST['blogIdea']
        request.session['blogIdea'] = blogIdea

        keywords = request.POST['keywords']
        request.session['keywords'] = keywords

        audience = request.POST['audience']
        request.session['audience'] = audience

        blogTopics = generateBlogTopicIdeas(blogIdea, audience, keywords)
        if blogTopics:
            request.session['blogTopics'] = blogTopics
            return redirect('blog-sections')
        else:
            messages.error(request, 'OOPs, we could not generate blog ideas for you, retry')
            return redirect('blog-topic')

    return render(request, 'blog-topicc.html', context)



def blogSections(request):
    if 'blogTopics' in request.session:
        pass
    else:
        messages.error(request, "Start by creating blog ideas")
        return redirect('blog-topic')

    context = {}
    context['blogTopics'] = request.session['blogTopics']
    return render(request, 'blog-sections.html', context)



def saveBlogTopic(request, blogTopic):
    if "blogIdea" in request.session and "keywords" in request.session and "audience" in request.session and 'blogTopics' in request.session:
        blog = Blog.objects.create(
            title=blogTopic,
            blogIdea=request.session['blogIdea'],
            keywords=request.session['keywords'],
            audience=request.session['audience'],
        )
        blog.save()

        blogTopics = request.session['blogTopics']
        blogTopics.remove(blogTopic)
        request.session['blogTopics'] = blogTopics

        return redirect('blog-sections')
    else:
        return redirect('blog-topic')


def useBlogTopic(request, blogTopic):
    context = {}

    if "blogIdea" in request.session and "keywords" in request.session and "audience" in request.session:

        blog = Blog.objects.create(
            title=blogTopic,
            blogIdea=request.session['blogIdea'],
            keywords=request.session['keywords'],
            audience=request.session['audience'],
        )
        blog.save()

        blogSections = generateBlogSectionTitles(blogTopic, request.session['audience'], request.session['keywords'])

    else:
        return redirect('blog-topic')

    if len(blogSections) > 0:
        request.session['blogSections'] = blogSections
        context['blogSections'] = blogSections
    else:
        messages.error(request, "Oopsie doosie, we could not generate any blog for you. Please try again")
        return redirect('blog-topic')

    if request.method == 'POST':
        for val in request.POST:
            if not 'csrfmiddlewaretoken' in val:
                section = generateBlogSectionDetails(blogTopic, val, request.session['audience'], request.session['keywords'])

                blogSec = BlogSection.objects.create(
                    title=val,
                    body=section,
                    blog=blog,
                )
                blogSec.save()
        return redirect('view-generated-blog', slug=blog.slug)

    return render(request, 'select-blog-sections.html', context)




def generatedBlog(request):
    context = {}

    # Retrieve the generated blog topics from the user's session
    blogTopics = request.session.get('blogTopics', [])

    if not blogTopics:
        # Handle the case where there are no generated blog topics
        context['error_message'] = "No blog topics have been generated. Please generate blog topics first."
    else:
        # Generate full blog content based on the topics
        blogContent = []

        # Define a function to generate content using GPT-3
        def generate_blog_content(topic):
            prompt = f"Write a blog post about {topic}"
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=500,  # Adjust the length as needed
                temperature=0.7,  # Adjust creativity (higher values make it more creative)
                stop=None  # You can add custom stop words to end the text
            )
            return response.choices[0].text

        for topic in blogTopics:
            content = generate_blog_content(topic)
            blogContent.append(content)

        context['blogContent'] = blogContent

    return render(request, 'generated-blog.html', context)