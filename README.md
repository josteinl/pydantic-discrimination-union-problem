# pydantic-discrimination-union-problem
Example code for testing Fastapi, Pydantic and discrimination union combination

## Installation
Using Python version 3.9.9. Create a virtual environment and activate it.


### Pydantic 1.9.0 trial

    pip install -r requirements_pydantic.txt --force-reinstall


``` 
pip freeze

anyio==3.5.0
asgiref==3.5.0
click==8.0.3
colorama==0.4.4
fastapi==0.73.0
h11==0.13.0
idna==3.3
pydantic==1.9.0
sniffio==1.2.0
starlette==0.17.1
typing_extensions==4.0.1
uvicorn==0.17.1
``` 


 ## Start server
With activated virtual environment

    python main.py

Access the openapi endpoint documentation [http://localhost/docs](http://localhost/docs)


## The error output

If I specify the Field() with ```...```:

    Cutlery = Annotated[
        Union[Knife, Fork, Spoon],
        Field(..., discriminator='cutlery_type_id'),
    ]

I get the following error output during startup:

```
python main.py
Traceback (most recent call last):
  File "C:\dev\pydantic-discrimination-union-problem\main.py", line 47, in <module>
    async def get_cutlery():
  File "C:\Users\jol\venv\pydantic-discrimination-union-problem\lib\site-packages\fastapi\routing.py", line 582, in decorator
    self.add_api_route(
  File "C:\Users\jol\venv\pydantic-discrimination-union-problem\lib\site-packages\fastapi\routing.py", line 525, in add_api_route
    route = route_class(
  File "C:\Users\jol\venv\pydantic-discrimination-union-problem\lib\site-packages\fastapi\routing.py", line 351, in __init__
    self.response_field = create_response_field(
  File "C:\Users\jol\venv\pydantic-discrimination-union-problem\lib\site-packages\fastapi\utils.py", line 65, in create_response_field
    return response_field(field_info=field_info)
  File "pydantic\fields.py", line 419, in pydantic.fields.ModelField.__init__
  File "pydantic\fields.py", line 534, in pydantic.fields.ModelField.prepare
  File "pydantic\fields.py", line 728, in pydantic.fields.ModelField._type_analysis
  File "pydantic\fields.py", line 776, in pydantic.fields.ModelField._create_sub_type
  File "pydantic\fields.py", line 451, in pydantic.fields.ModelField._get_field_info
ValueError: `Field` default cannot be set in `Annotated` for '_Response_get_cutlery_cutlery_get'
```

Removing the ```...``` from Field():

    Cutlery = Annotated[
        Union[Knife, Fork, Spoon],
        Field(discriminator='cutlery_type_id'),
    ]

the server starts, and everything seems to work OK

Now (2022-02-02) using pydantic version 1.9.0 I do not get the errors I encountered before.

The following versions failed (tested 2021-09-13 Python 3.8): 

    pip install --force-reinstall git+git://github.com/PrettyWood/pydantic.git@f/discriminated-union#egg=pydantic

or the commit I think has introduced some problem (2021-09-06):

    pip install --force-reinstall git+git://github.com/PrettyWood/pydantic.git@417601ae551b92ad875b84dbad93a51eaa40f66c

and again if I use the commit, one before the above (2021-09-06) (45db4ad3aa558879824a91dd3b011d0449eb2977), it works
both with and without the ```...```.

    pip install --force-reinstall git+git://github.com/PrettyWood/pydantic.git@45db4ad3aa558879824a91dd3b011d0449eb2977
