# pydantic-discrimination-union-problem
Example code for testing Fastapi, Pydantic and discrimination union combination

## Installation
Using Python version 3.8.10. Create a virtual environment and activate it.

### OK
Uses the last OK commit for this example to work
[git+git://github.com/PrettyWood/pydantic.git@45db4ad3aa558879824a91dd3b011d0449eb2977](https://github.com/PrettyWood/pydantic/commit/45db4ad3aa558879824a91dd3b011d0449eb2977)

    pip install -r requirements_ok.txt --force-reinstall

### ERROR
Uses the breaking commit [git+git://github.com/PrettyWood/pydantic.git@417601ae551b92ad875b84dbad93a51eaa40f66c](https://github.com/PrettyWood/pydantic/commit/417601ae551b92ad875b84dbad93a51eaa40f66c).

    pip install -r requirements_error.txt --force-reinstall

## Start server
With activated virtual environment

    python main.py

Access the openapi endpoint documentation [http://localhost/docs](http://localhost/docs)


## The error output

I get the following error output during startup:

```
C:\dev\pydantic-discrimination-union-problem\.venv\Scripts\python.exe C:/dev/pydantic-discrimination-union-problem/main.py
Traceback (most recent call last):
  File "C:/dev/pydantic-discrimination-union-problem/main.py", line 47, in <module>
    async def get_cutlery():
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\fastapi\routing.py", line 582, in decorator
    self.add_api_route(
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\fastapi\routing.py", line 525, in add_api_route
    route = route_class(
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\fastapi\routing.py", line 351, in __init__
    self.response_field = create_response_field(
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\fastapi\utils.py", line 65, in create_response_field
    return response_field(field_info=field_info)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 389, in __init__
    self.prepare()
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 508, in prepare
    self._type_analysis()
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 695, in _type_analysis
    self.sub_fields = [self._create_sub_type(self.type_, '_' + self.name)]
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 735, in _create_sub_type
    field_info, _ = self._get_field_info(name, type_, None, self.model_config)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 425, in _get_field_info
    raise ValueError(f'`Field` default cannot be set in `Annotated` for {field_name!r}')
ValueError: `Field` default cannot be set in `Annotated` for '_Response_get_cutlery_cutlery_get'

Process finished with exit code 1
```
