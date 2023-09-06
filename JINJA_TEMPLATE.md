# JINJA TEMPLATES

### Variable Tag:

    {{ variable_name }}

Outputs the value of a variable within the template.

### Expression Tag:

    {% expression %}

Executes a simple expression within the template, such as assignments, mathematical operations, or function calls.

### For Loop Tag:

    {% for item in items %}
        # block of contents
    {% endfor %}

Iterates over a sequence (e.g., list, dictionary) and generates content for each item in the sequence.

### If-Else Tag:

    {% if condition %}
        # block of contents
    {% else %}
        # block of contents
    {% endif %}

Allows conditional rendering of content based on a specified condition.

### Block Tag:

    {% block block_name %}
        # block of contents
    {% endblock %}

Defines a block of content that can be overridden in child templates that extend the current template.

### Macro Tag:

    {% macro macro_name(arguments) %}
        # block of contents
    {% endmacro %}

Defines reusable macros that can be called within templates to generate specific content or logic.

### Include Tag:

    {% include "template_file.html" %}

Includes the content of an external template file within the current template.

### Extends Tag:

    {% extends "base_template.html" %}

Specifies that the current template extends a base template, inheriting its structure and blocks.

### Import Tag:

    {% import "macros.html" as macros %}

Imports macros from an external template for use in the current template.

### Set Tag:

    {% set variable = value %}

Assigns a value to a variable within the template.

### Raw Tag:

    {% raw %}
        # block of contents
    {% endraw %}

Prevents Jinja from processing the content within the tag and outputs it as-is.

### Filter Tag:

    {% filter filter_function %}
      # block of contents
    {% endfilter %}

Applies a filter to a section of content, modifying its output.

### Whitespace Control Tags:

- **{%- ... -%}**: Removes leading and trailing whitespace.
- **{%+ ... +%}**: Preserves leading and trailing whitespace.

### Comments:

    {# This is a comment #}

Adds comments within templates that are not rendered in the output.

### Template Inheritance Tags:

- **{% block %}**: Defines blocks within the base template.

- **{% extends %}**: Specifies that a template extends another template.

- **{% include %}**: Includes content from external templates.
