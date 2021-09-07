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

