<p>
    <a href="{% url 'Pizza:index' %}"> Baylor's Pizzeria</a>
    <a href="{% url 'Pizza:pizzas' %}"> Pizzas</a>
    {% if user.is_authenticated %}
    Hello, {{ user.username }}.
    <a href="{% url 'users:logout' %}">Log out</a>
    {% else %}
    <a href="{% url 'users:register' %}">Register</a>
    <a href="{% url 'users:login' %}">Log in</a>
    {% endif %}

</p>

{% block content %}{% endblock content %}

<p>
    <a href="{% url 'Pizza:index' %}"> Baylor's Pizzeria</a>
    <a href="{% url 'Pizza:pizzas' %}"> Pizzas</a>
    {% if user.is_authenticated %}
    Hello, {{ user.username }}.
    <a href="{% url 'users:logout' %}">Log out</a>
    {% else %}
    <a href="{% url 'users:register' %}">Register</a>
    <a href="{% url 'users:login' %}">Log in</a>
    {% endif %}

</p>