# utils.py
from django.template import Template, Context

def generate_invoice_html(template_html, data):
    template = Template(template_html)
    context = Context(data)
    return template.render(context)
