# Django Template Tags Cheat Sheet

## 1. Variable Tag:

    {{ variable_name }}

**Description**: Inserts the value of the variable into the template.

## 2. For Loop Tag:

     {% for item in items %}
         {{ item }}
     {% endfor %}

**Description**: Iterates over a list or queryset and displays each item.

## 3. If-Else Tag:

     {% if condition %}
         Display this content if the condition is true.
     {% else %}
         Display this content if the condition is false.
     {% endif %}

**Description**: Conditional statement for displaying content.

## 4. Block Tag:

     {% block content %}
         This is the default content.
     {% endblock %}

**Description**: Defines a block that can be overridden in child templates.

## 5. Include Tag:

     {% include "included_template.html" %}

**Description**: Includes the content of another template within the current template.

## 6. URL Tag:

     {% url 'view_name' %}

**Description**: Generates a URL for a named URL pattern.

## 7. Static Tag:

     {% static 'path/to/static/file.css' %}

**Description**: Generates a URL for a static file (e.g., CSS, JavaScript).

## 8. Extends Tag:

     {% extends "base_template.html" %}

**Description**: Specifies that the current template extends a base template.

## 9. Block Tag (Child Template):

     {% block content %}
         This content replaces the parent template's block content.
     {% endblock %}

**Description**: Overrides a block from the parent template in a child template.

## 10. Filter Tag:

      {{ value|filter_name:"arg" }}

**Description**: Applies a filter to a variable's value.

## 11. CSRF Token Tag:

      {% csrf_token %}

**Description**: Outputs a hidden input field with a CSRF token for form submissions.

## 12. Comment Tag:

      {% comment %}
          This text is commented out and not displayed in the rendered HTML.
      {% endcomment %}

**Description**: Allows you to add comments in the template code that are not visible in the output.

## 13. Trans Tag (Internationalization):

      {% trans "text_to_translate" %}

**Description**: Marks text for translation in internationalization.

## 14. Template Inheritance (Extending Multiple Blocks):

      {% block block_name %}
          Content for the block.
      {% endblock %}
      ...
      {% block another_block %}
          Content for another block.
      {% endblock %}

**Description**: Demonstrates the use of multiple blocks in a template.

## 15. Template Tags for Forms:

Various template tags are available for rendering forms, such as {{ form.as_p }}, {{ form.as_table }}, and {{ form.as_ul }}.

### References:

**Django Template Tags** (https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)
