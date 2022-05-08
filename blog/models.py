from django.shortcuts import render
from audioop import reverse
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ckeditor.fields import RichTextField

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtailmarkdown.blocks import MarkdownBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailcodeblock.blocks import CodeBlock
from streams.blocks import CardBlock
from visitor_record.utils import count_visits

# Create your models here.
class BlogListingPage(Page):
    template = "blog/blog_listing_page.html"

    custom_title = RichTextField(
        max_length = 100,
        blank = False,
        null = False,
        help_text= 'Overwirtes the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context (self, request, *args, **kwargs):
        context=super().get_context(request, *args, **kwargs)
        blogpages = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        latest_blogs= blogpages[:5]
        paginator = Paginator(blogpages, 12)
        page_num = request.GET.get('page', 1)
        try:
            blogpage = paginator.get_page(page_num)
        except PageNotAnInteger:
            blogpage = paginator.get_page(1)
            page_num=1
        except EmptyPage:
            blogpage = paginator.get_page(paginator.num_pages)
            page_num = paginator.num_pages
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

        data = count_visits(request, self)
        context['client_ip'] = data['client_ip']
        context['total_hits'] = data['total_hits']
        context['total_visitors'] =data['total_vistors']
        context['cookie'] = data['cookie']
        context['posts'] = blogpage
        context['page_range'] = page_range
        context['latest_posts'] = latest_blogs

        return context

    def serve(self, request):
        context = self.get_context(request)
        template = self.get_template(request)
        
        response = render(request, template, context)
        response.set_cookie(context['cookie'], 'true', max_age=300)
        return response

    class Meta:
        verbose_name = "博客"

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogDetailPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogTagIndexPage(Page):
    template = "blog/blog_tag_listing_page.html"

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogDetailPage.objects.filter(tags__name=tag)
        paginator = Paginator(blogpages, 12)
        page_num = request.GET.get('page', 1)
        try:
            blogpage = paginator.get_page(page_num)
        except PageNotAnInteger:
            blogpage = paginator.get_page(1)
            page_num=1
        except EmptyPage:
            blogpage = paginator.get_page(paginator.num_pages)
            page_num = paginator.num_pages
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


        # Update template context
        data = count_visits(request, self)

        context = super().get_context(request)
        context['posts'] = blogpages
        context['page_range']=page_range

        context['total_hits'] = data['total_hits']
        context['total_visitors'] =data['total_vistors']
        context['cookie'] = data['cookie']
        return context

    def serve(self, request):
        context = self.get_context(request)
        template = self.get_template(request)
        
        response = render(request, template, context)
        response.set_cookie(context['cookie'], 'true', max_age=300)
        return response

class BlogDetailPage(Page):
    template = "blog/blog_detail_page.html"
    
    def get_context(self, request):

        authorname=self.author.get_fullname_or_username()
        data = count_visits(request, self)

        context = super().get_context(request)
        context['total_hits'] = data['total_hits']
        context['total_visitors'] =data['total_vistors']
        context['cookie'] = data['cookie']
        context['author']=authorname
        return context
    
    def serve(self, request):
        context = self.get_context(request)
        template = self.get_template(request)
        
        response = render(request, template, context)
        response.set_cookie(context['cookie'], 'true', max_age=300)
        return response
        

    custom_title = models.CharField('Title', max_length=60, help_text='文章标题')
    #author = models.CharField("Author", max_length=255, default="Wang Zhenxuan")
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    create_date = models.DateField("Create date", auto_now_add= True)
    update_date = models.DateField("Update date", auto_now=True)
    intro = models.CharField('Introduction', max_length=500, help_text='文章简介')
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    
    #categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    content = StreamField(
        [
            ('heading', blocks.CharBlock(form_classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('blockquote', blocks.BlockQuoteBlock(label='Block Quote')),
            ('documentchooser', DocumentChooserBlock(label='Document Chooser')),
            ('url', blocks.URLBlock(label='URL')),
            ('embed', EmbedBlock(label='Embed')),
            #('snippetchooser', SnippetChooserBlock(label='Snippet Chooser')),
            ('rawhtml', blocks.RawHTMLBlock(label='Raw HTML')),
            ('table', TableBlock(label='Table')),
            ('markdown', MarkdownBlock(label='Markdown')),
            ('code', CodeBlock(label='Code')),
            ('imagedeck', CardBlock(label='Imagedeck')), 
            
        ],
        null=True,
        blank=True,
    )
    
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def prev(self):
        try:
            previous=self.get_next_sibling()
            return(previous)
        except self.DoesNotExist:
            return(None)

    def next(self):
        try:
            return(self.get_prev_sibling())
        except self.DoesNotExist:
            return(None) 
    
    def get_url(self):
        return self.url
        
    def get_user(self):
        return self.author

    def get_email(self):
        return self.author.email
    

    search_fields = Page.search_fields + [
        index.SearchField('custom_title'),
        index.SearchField('intro'),
        index.SearchField('content'),
        index.SearchField('create_date'),
    ]

    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label="Gallery images"),
        MultiFieldPanel([
            FieldPanel('custom_title'),
            FieldPanel('intro'),
            FieldPanel('author'),
            #FieldPanel('create_date'),
            #FieldPanel('update_date'),
            FieldPanel('tags'),
            #FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        
        # FieldPanel('body'),
        StreamFieldPanel('content'),
        
    ]

    class Meta:
        ordering = ['-create_date']

    
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogDetailPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', blank=False, on_delete=models.CASCADE, related_name='+'
    )
    

    panels = [
        ImageChooserPanel('image'),
    ]
