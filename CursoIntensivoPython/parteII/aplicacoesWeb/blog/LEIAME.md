# Blog

- Inicie um novo projeto Django chamado Blog.

- Crie uma aplicação chamada blogs no projeto, com um modelo de nome BlogPost.
O modelo deve ter campos como *title*, *text* e *date_added*.

- Crie um superusuário para o projeto e use o site de administração para inserir
algumas postagens pequenas.

- Crie uma página inicial que mostre todas as postagens em ordem cronológica.

- Construa um formulário para criar novas postagens e outro para editar
postagens existentes. Preencha seus formulários para garantir que funcionem.

- Adicione um sistema de autenticação e cadastro de usuários no projeto. Garanta
 que usuários logados vejam seus nomes de usuário em algum lugar da tela,
 equanto usuários não cadastrados vejam um link para a página de cadastro

- Garanta que toda postagem esteja associada a um usuário em particular.

- Certifique-se de que todas as postagens sejam publicamente acessíveis, mas apenas os usuários cadastrados possam adicionar postagens e editar postagens existentes.

- Garanta que o usuário esteja editando suas próprias postagens antes de processar o formulário

## Passo-a-Passo

### Definição do projeto

1. Especificação
2. Criar ambiente virtual: `python -m venv b_env`
3. Instalar o Django: `pip3 install Django`
4. Criar o projeto: `django-admin startproject blog .`
5. Criar o banco de dados: `python manage.py migrate`
6. Iniciar a aplicação: `python manage.py startapp blogs`

### Funcionalidades do projeto

7. Criar modelos em `./blog/blogs/models.py`
8. Inserir a aplicação em `./blog/blog/settings.py`
9. Atualizar o banco de dados: `python manage.py makemigrations`
10. Aplicar a migração: `python manage.py migrate`
11. Criar superusuário: `python manage.py createsuperuser`
12. Registrar o modelo em em `./blog/blogs/admin.py`

### Interface de visualização do projeto

13. Mapear url em `./blog/blog/urls.py`
14. Criar o arquivo `./blog/blogs/urls.py`
15. Incluir em `./blog/blogs/urls.py` a linha `app_name = 'blogs'`
16. Criar a view em `./blog/blogs/views.py`
17. Criar o diretório `./blog/blogs/templates/blogs`
18. Criar o template base para as páginas `base.html`
19. Mapear a URL das publicações em `./blog/blogs/urls.py`
20. Criar a view de publicações em `./blog/blogs/views.py`
21. Criar o `index.html`

### Interface de inclusão/edição do projeto

22. Criar o arquivo `./blog/blogs/forms.py`
23. Mapear a URL para inserir uma publicação em `./blog/blogs/urls.py`
24. Criar a view para inserir uma publicação em `./blog/blogs/views.py`
25. Criar o template para novas publicações `new_post.html`
26. Incluir o link para `new_post.html` na página de publicações

### Usuários

27. `python manage.py startapp users`
28. incluir `users` em `settings.py`
29. incluir `users` em `urls.py`
30. criar `/users/urls.py`
31. mapear url de login em `/users/urls.py`
32. criar `/users/templates/users/login.html`
33. incluir link de login em `base.html`
34. mapear url de logout em `/users/urls.py`
35. incluir `LOGOUT_REDIRECT_URL = '/'` em `settings.py`
36. incluir link de logout em `base.html`
37. mapear url de registro em `/users/urls.py`
38. criar a view da página de registro em `/users/views.py`
39. criar o template de cadastro em `register.html`
40. incluir link de cadastro em `base.html`

### Restringindo acesso

41. Acrescentar `@login_required` em `views.py` em todas as páginas restritas
42. Acrescentar `LOGIN_URL = '/users/login'` em `settings.py`
43. Incluir chave estrangeira de usuário no nível mais alto de informação restrita `owner = models.ForeignKey(User, on_delete=models.CASCADE)`
44. Descrobir os ID dos usuários existentes através do shell de Django:
```
python manage.py shell
from django.contrig.auth.models import User
User.objects.all()
for user in User.objects.all():
    print(user.username,user.id)
exit()
```
45. Migrar os dados existentes para o superusuário com `python manage.py makemigrations blogs`
46. Execute `python manage.py migrate`
47. Acrescentar `.filter(owner=request.user)` em `views.py` na definição restrita mais alta
48. Inluir `erro 404` se o usuário tentar uma URL que não pertence a ele em `views.py`:
```
if registro.owner != request.user:
    raise Http404
```
49.  Associar novas entradas ao usuário atual em `views.py`

### Aparência

50. `pip3 install django-bootstrap3`
51. Incluir `'bootstrap3'` em `INSTALLED_APPS` em `settings.py`
52. Habilitar o jQuery em `settings.py`:
```
BOOTSTRAP3 = {
    'include_jquery':True
}
```
53. Alterar `base.html`
54. Alterar `index.html`
55. Alterar `login.html`
56. Alterar páginas de conteúdo

[^1] Para executar a aplicação `python manage.py runserver`
[^2] Para executar o shell de Django `python manage.py shell`
