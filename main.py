import enum
from typing import List, Union, Literal, Annotated

from fastapi import FastAPI
from pydantic import Field, BaseModel
import uvicorn
from pydantic.fields import UndefinedType


class CutleryTypeEnum(enum.IntEnum):
    KNIFE = 1
    FORK = 2
    SPOON = 3


class CutleryBase(BaseModel):
    name: str


class Knife(CutleryBase):
    cutlery_type_id: Literal[CutleryTypeEnum.KNIFE]


class Fork(CutleryBase):
    cutlery_type_id: Literal[CutleryTypeEnum.FORK]
    number_of_teeth: int = None


class Spoon(CutleryBase):
    cutlery_type_id: Literal[CutleryTypeEnum.SPOON]
    volume: float = None


# Problem version
Cutlery = Annotated[
    Union[Knife, Fork, Spoon],
    Field(discriminator='cutlery_type_id'),
]

# working version (for now)
# class Cutlery(BaseModel):
#     __root__: Annotated[
#         Union[Knife, Fork, Spoon],
#         Field(discriminator='cutlery_type_id'),
#     ]

app = FastAPI()


@app.get("/cutlery",
         response_model=List[Cutlery])
async def get_cutlery():
    return [{'cutlery_type_id': CutleryTypeEnum.KNIFE, 'name': 'My sharp knife'},
            {'cutlery_type_id': CutleryTypeEnum.FORK, 'name': 'The three teeth fork'},
            {'cutlery_type_id': CutleryTypeEnum.SPOON, 'name': 'Tea spoon'}]


#
# Enable second usage of Cutlery result in traceback on startup
#

@app.get("/cutlery2",
         response_model=List[Cutlery])
async def get_cutlery2():
    return [{'cutlery_type_id': CutleryTypeEnum.KNIFE, 'name': 'My sharp knife'},
            {'cutlery_type_id': CutleryTypeEnum.KNIFE, 'name': 'My knife is sharp'},
            {'cutlery_type_id': CutleryTypeEnum.FORK, 'name': 'The three teeth fork'},
            {'cutlery_type_id': CutleryTypeEnum.SPOON, 'name': 'Tea spoon'}]


#
# second try with inline types
#

# @app.get("/cutlery3",
#          response_model=List[Annotated[
#              Union[Knife, Fork, Spoon],
#              Field(discriminator='cutlery_type_id'),
#          ]])
# async def get_cutlery3():
#     return [{'cutlery_type_id': CutleryTypeEnum.KNIFE, 'name': 'My sharp knife'},
#             {'cutlery_type_id': CutleryTypeEnum.FORK, 'name': 'The three teeth fork'},
#             {'cutlery_type_id': CutleryTypeEnum.SPOON, 'name': 'Tea spoon'}]
#
#
# @app.get("/cutlery4",
#          response_model=List[Annotated[
#              Union[Knife, Fork, Spoon],
#              Field(discriminator='cutlery_type_id'),
#          ]])
# async def get_cutlery4():
#     return [{'cutlery_type_id': CutleryTypeEnum.KNIFE, 'name': 'My sharp knife'},
#             {'cutlery_type_id': CutleryTypeEnum.KNIFE, 'name': 'My knife is sharp'},
#             {'cutlery_type_id': CutleryTypeEnum.FORK, 'name': 'The three teeth fork'},
#             {'cutlery_type_id': CutleryTypeEnum.SPOON, 'name': 'Tea spoon'}]
#

uvicorn.run(app, host='127.0.0.1', port=80)
