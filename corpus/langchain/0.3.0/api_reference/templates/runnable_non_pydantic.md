{{ objname }}
{{ underline }}==============

    The :py:class:`Runnable Interface <langchain_core.runnables.base.Runnable>` has additional methods that are available on runnables, such as :py:meth:`with_types <langchain_core.runnables.base.Runnable.with_types>`, :py:meth:`with_retry <langchain_core.runnables.base.Runnable.with_retry>`, :py:meth:`assign <langchain_core.runnables.base.Runnable.assign>`, :py:meth:`bind <langchain_core.runnables.base.Runnable.bind>`, :py:meth:`get_graph <langchain_core.runnables.base.Runnable.get_graph>`, and more.

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
