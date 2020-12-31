from jinja2 import Template, escape
''' ------------------------Jinja------------------------ '''

# ----- Урок 1 -----
#-----------------------------------------------------------------------------------------------------------------------

#name = "Федор"
#age = 28

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per2 = { 'name': 'Федор', 'age': 34}

# tm = Template("Привет {{ name }}") # Создаём экземпляр класса Template, на основе текстового шаблона
''' {% %} - спецификатор шаблона
 {{ }} - выражение для вставки конструкции Python в шаблон
 {# #} - блок комментариев
 # ## - Строковый комментарий}'''

per = Person("Фёдор", 33)

tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}.")
msg = tm.render(p = per)

tm2 = Template("Мне {{ p.age }} лет и зовут {{ p.name }}.")
# tm2 = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}.")
msg2 = tm2.render(p = per2)

# tm = Template("Мне {{ a }} лет и зовут {{ n }}.")
# msg = tm.render(n=name, a=age)

# msg2 = f"Привет {name}" # F строка
# print(msg, msg2, sep="\n")
print(msg)
print(msg2)

#-----------------------------------------------------------------------------------------------------------------------

# ----- Урок 2 -----
#-----------------------------------------------------------------------------------------------------------------------

data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}                               
подставляет соответствующее значение{% endraw %}''' # <-- Блок Raw

link1 = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a> '''

#Код ниже, делает одно и тоже
'''' ---------- '''
tm2 = Template("{{ link | e}}") # <-- Указываем флаг е для экронирования
msg3 = tm2.render(link=link1)

msg2 = escape(link1)
print(msg2)
'''' ---------- '''

tm1 = Template(data)
msg1 = tm1.render(name='Фёдор')

# ----------------------------------------|
cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'},]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{%else -%}    
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities = cities)
# ----------------------------------------|

print(msg)
print(msg1)
print(msg3)

#-----------------------------------------------------------------------------------------------------------------------

# ----- Урок 3 -----
#-----------------------------------------------------------------------------------------------------------------------

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}
]

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

tpl5 = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{%  endfilter%}
{%  endfor -%}
'''

"""
{{%filter<название фильтра>%}}
<фрагмент для применения фильтра>
{% endfilter%}
"""

tm5 = Template(tpl5)
msg5 = tm5.render(users=persons)

# sum - вычисление суммы поля коллекции
# sum(iterable, attribute=None, start=0)

#---------------------------------------------------------------------------|
digs = [1,2,3,4,5]
tpl1 = "Сумма {{ cs | sum}}"
tm1 = Template(tpl1)
msg1 = tm1.render(cs = digs)

tpl2 = "Суммарная цена автомобилей {{ cs | max(attribute='price') }}" # Выводит максимальное значение(можно и минимальное min)
tm2 = Template(tpl2)
msg2 = tm2.render(cs = cars)

tpl3 = "Суммарная цена автомобилей {{ cs | random }}" # Выводит случайное значение
tm3 = Template(tpl3)
msg3 = tm3.render(cs = cars)

tpl4 = "Автомобиль {{ cs | replace('о','О') }}" # Заменит все маленькие о на большие
tm4 = Template(tpl4)
msg4 = tm4.render(cs = cars)

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
#---------------------------------------------------------------------------|

#Macro
#---------------------------------------------------------------------------|
# Определение макроса
html = '''
{% macro input(name, value='', type='text', size=20) -%} 
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{input('username')}}
<p>{{input('email')}}
<p>{{input('password')}}
'''

tm6 =Template(html)
msg6 = tm6.render()
#---------------------------------------------------------------------------|

#Call(Вложенный макрос)
#---------------------------------------------------------------------------|
'''
{%call[(параметры)]<вызов макроса>%}
<вложенный шаблон>
{% endcall %}
'''

html2 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor%}
</ul>
{%- endmacro %}

{{list_users(users)}}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm7 = Template(html2)
msg7 = tm7.render(users = persons)

#---------------------------------------------------------------------------|

print(msg)
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(msg6)
print(msg7)

#-----------------------------------------------------------------------------------------------------------------------
