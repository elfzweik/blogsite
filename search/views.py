from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.db.models import Q
from wagtail.core.models import Page
from wagtail.search.models import Query

from blog.models import BlogDetailPage


def search(request):
    search_query = request.GET.get('query', None)
    page_num = request.GET.get('page', 1)
    print(search_query)
    # Search
    if search_query:
        #search_results = BlogDetailPage.objects.live().search(search_query, operator='or')
        search_results = BlogDetailPage.objects.live().filter(
                Q(custom_title_contains = search_query) |
                Q(intro_contains = search_query) | 
                Q(content_contains = search_query) |
                Q(tags_contains = search_query) 
            )
        query = Query.get(search_query)
        print(search_results)
        # Record hit
        query.add_hit()
    else:
        search_results = BlogDetailPage.objects.none()

    # Pagination
    paginator = Paginator(search_results, 12)
    try:
        search_results = paginator.page(page_num)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    page_range = list(range(max(int(page_num)-2, 1), int(page_num))) + \
            list(range(int(page_num), min(int(page_num)+2, paginator.num_pages)+1))
    if page_range[0]-1 > 1:
        page_range.insert(0,'...')
        page_range.insert(0,1)
    elif page_range[0]-1 == 1:
        page_range.insert(0,1)

    if paginator.num_pages - page_range[-1] > 1:
        page_range.append('...')
        page_range.append(paginator.num_pages)
    elif paginator.num_pages - page_range[-1] == 1:
        page_range.append(paginator.num_pages)

    return TemplateResponse(request, 'search/search_result.html', {
        'search_query': search_query,
        'search_results': search_results,
        'page_range': page_range,
    })
