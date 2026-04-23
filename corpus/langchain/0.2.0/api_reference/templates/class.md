{{ underline }}==============

   {% block attributes %}
   {% if attributes %}

   {% for item in attributes %}
      ~{{ name }}.{{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block methods %}
   {% if methods %}

   {% for item in methods %}
      ~{{ name }}.{{ item }}
   {%- endfor %}

   {% for item in methods %}

   {%- endfor %}

   {% endif %}
   {% endblock %}
