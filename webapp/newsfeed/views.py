from django.shortcuts import render


posts = [
    {
        'title': 'Global food price index up 3.3% year to year',
        'content': 'September 2019 global Food Price Index remained unchanged from August, but it was 3.3% higher than ' 
                   'the corresponding period in 2018. Maize prices were down month-on-month. The Vegetable Oil Price ' 
                   'Index averaged 135.7 points and the Sugar Price Index averaged 168 points, down nearlt 3.9% from ' 
                   'August. According to the latest outlook for 2019 to 2028, the local production and market demand has ' 
                   'had major impacts on South African sugar production, resulting in a decrease of revenue ' 
                   'of approximately R1.5 billion.',
        'source': 'Farmers Weekly',
        'link_url': 'https://google.com',
        'link_title': 'SA Global food price index up 3.3% year to year from 2019',
        'tags': 'agriculture news localnews farmer_sa agriculture_life agriculture_global',
        'date_posted': 'November 05, 2018'
    },
    {
        'title': 'South Africas minister of agriculture Thoko Didiza refuses',
        'content': 'South Africas minister of agriculture Thoko Didiza has upheld previous refusals to allow general '
                   'release of Bayers triple stacked genetically modified (GM) maize seed technology for production'
                   'in the country.',
        'source': 'Agri-Update',
        'link_url': 'https://yahoo.com',
        'link_title': 'Thoko Didiza refuses local triple-stacked GM maize seed release',
        'tags': 'agriculture news localnews farmer_sa maize agriculture_life agriculture_global',
        'date_posted': 'November 06, 2018'
    },
    {
        'title': 'Agricultural diversification driving economic growth in KZN',
        'content': 'The province is recovering from a severe drought , and indicators point to a normal rainfall for SAs'
                   'summer rainfall areas which bodes well for prodcution. The province has seen a dramatic increase in'
                   'production of macadamia nuts and avos, mainly for export markets.',
        'source': 'Daily Sun',
        'link_url': 'https://bing.com',
        'link_title': 'Agricultural diversification driving economic growth in KZN',
        'tags': 'agriculture news localnews farmer_sa  agriculture_life agriculture_global',
        'date_posted': 'November 07, 2018'
    }
]

def home(request):
    context = {
        'title': 'Newsfeed',
        'posts': posts
    }
    return render(request, 'newsfeed/home.html', context)
