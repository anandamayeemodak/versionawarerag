{{ objname }}
{{ underline }}==============

   {% block attributes %}
   {% if attributes %}

   {% for item in attributes %}
      ~{{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block methods %}
   {% if methods %}

   {% for item in methods %}
      ~{{ item }}
   {%- endfor %}

   {% for item in methods %}

   {%- endfor %}

   {% endif %}
   {% endblock %}
