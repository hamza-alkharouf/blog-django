from django.shortcuts import render


posts = [
    {
        'title' :'التدوينى الاولى',
        'content' :'نص التدوينة الاولى كنص تجريبي',
        'post_date':'10-4-2019',
        'author':'hamza alkh'
    },
    {
        'title' :'التدوينى الثانية',
        'content' :'نص التدوينة الثانية كنص تجريبي',
        'post_date':'8-1-2020',
        'author':'sami assaf'
    },
    {
        'title' :'التدوينى الثالثة',
        'content' :'نص التدوينة الثالثة كنص تجريبي',
        'post_date':'25-3-2020',
        'author':'ali ahmad'
    },
    {
        'title' :'التدوينى الرابعة',
        'content' :'نص التدوينة الرابعة كنص تجريبي',
        'post_date':'2-12-2022',
        'author':'rami alkh'
    },
]

def home(request):
    context ={
        'title' : 'الصفحة الرئيسية',
        'posts' : posts
    }
    return render(request, 'blog/index.html', context)

def about(request):
        context ={
        'title' : 'من انا',
    }
        return render(request, 'blog/about.html', context)
