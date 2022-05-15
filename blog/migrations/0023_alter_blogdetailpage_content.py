# Generated by Django 3.2.12 on 2022-05-15 07:44

import blog.models
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20220506_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=blog.models.CustomStreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('blockquote', wagtail.core.blocks.BlockQuoteBlock(label='Block Quote')), ('documentchooser', wagtail.documents.blocks.DocumentChooserBlock(label='Document Chooser')), ('url', wagtail.core.blocks.URLBlock(label='URL')), ('embed', wagtail.embeds.blocks.EmbedBlock(label='Embed')), ('rawhtml', wagtail.core.blocks.RawHTMLBlock(label='Raw HTML')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Table')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(label='Markdown')), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('imagedeck', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If button above is selected, that will be used first', required=False))])))], label='Imagedeck'))], blank=True, null=True),
        ),
    ]
