from jinja2 import Template

name = "Федор"

tm = Template("Привет {{ name }}")
msg = tm.render(name=name)

print(msg)