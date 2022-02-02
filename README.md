# pydantic-discrimination-union-problem
Example code for testing Fastapi, Pydantic and discrimination union combination

## Different trials in other branches

Successful trial (2022-02-02) with the Pydantic release version 1.9.0 in branch [pydantic_1.9.0_trial](https://github.com/josteinl/pydantic-discrimination-union-problem/tree/pydantic_1.9.0_trial)

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

If I specifiy the Field() with ```...```:

    Cutlery = Annotated[
        Union[Knife, Fork, Spoon],
        Field(..., discriminator='cutlery_type_id'),
    ]

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

Removing the ```...``` from Field():

    Cutlery = Annotated[
        Union[Knife, Fork, Spoon],
        Field(discriminator='cutlery_type_id'),
    ]

the server starts, but when I call the endpoint I get another crash:

```
C:\dev\pydantic-discrimination-union-problem\.venv\Scripts\python.exe C:/dev/pydantic-discrimination-union-problem/main.py
INFO:     Started server process [28416]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:80 (Press CTRL+C to quit)
INFO:     127.0.0.1:50130 - "GET /cutlery HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\uvicorn\protocols\http\h11_impl.py", line 373, in run_asgi
    result = await app(self.scope, self.receive, self.send)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\uvicorn\middleware\proxy_headers.py", line 75, in __call__
    return await self.app(scope, receive, send)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\fastapi\applications.py", line 208, in __call__
    await super().__call__(scope, receive, send)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\middleware\errors.py", line 181, in __call__
    raise exc from None
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\middleware\errors.py", line 159, in __call__
    await self.app(scope, receive, _send)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\exceptions.py", line 82, in __call__
    raise exc from None
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\exceptions.py", line 71, in __call__
    await self.app(scope, receive, sender)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\routing.py", line 580, in __call__
    await route.handle(scope, receive, send)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\routing.py", line 241, in handle
    await self.app(scope, receive, send)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\starlette\routing.py", line 52, in app
    response = await func(request)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\fastapi\routing.py", line 234, in app
    response_data = await serialize_response(
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\fastapi\routing.py", line 127, in serialize_response
    value, errors_ = field.validate(response_content, {}, loc=("response",))
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 824, in validate
    v, errors = self._validate_sequence_like(v, values, loc, cls)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 857, in _validate_sequence_like
    r, ee = self._validate_singleton(v_, values, v_loc, cls)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 994, in _validate_singleton
    value, error = field.validate(v, values, loc=loc, cls=cls)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 813, in validate
    v, errors = self._validate_singleton(v, values, loc, cls)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 990, in _validate_singleton
    return self._validate_discriminated_union(v, values, loc, cls)
  File "C:\dev\pydantic-discrimination-union-problem\.venv\lib\site-packages\pydantic\fields.py", line 1009, in _validate_discriminated_union
    assert cls is not None
AssertionError
```

I get the above error if I use either of these commits (latest of today 2021-09-13): 

    pip install --force-reinstall git+git://github.com/PrettyWood/pydantic.git@f/discriminated-union#egg=pydantic

or the commit I think has introduced some problem (2021-09-06):

    pip install --force-reinstall git+git://github.com/PrettyWood/pydantic.git@417601ae551b92ad875b84dbad93a51eaa40f66c

and again if I use the commit, one before the above (2021-09-06) (45db4ad3aa558879824a91dd3b011d0449eb2977), it works
both with and without the ```...```.

    pip install --force-reinstall git+git://github.com/PrettyWood/pydantic.git@45db4ad3aa558879824a91dd3b011d0449eb2977
