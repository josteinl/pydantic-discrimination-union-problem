import enum
from typing import List, Union, Literal

from typing_extensions import Annotated
from fastapi import FastAPI
from pydantic import Field, BaseModel
import uvicorn


class CutleryTypeEnum(enum.IntEnum):
    KNIFE = 1
    FORK = 2
    SPOON = 3


class CutleryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Knife(CutleryBase):
    cutlery_type_id: Literal[CutleryTypeEnum.KNIFE] = CutleryTypeEnum.KNIFE


class Fork(CutleryBase):
    cutlery_type_id: Literal[CutleryTypeEnum.FORK] = CutleryTypeEnum.FORK
    number_of_teeth: int = None


class Spoon(CutleryBase):
    cutlery_type_id: Literal[CutleryTypeEnum.SPOON] = CutleryTypeEnum.SPOON
    volume: float = None


Cutlery = Annotated[
    Union[Knife, Fork, Spoon],
    Field(discriminator="cutlery_type_id"),
]

app = FastAPI()


@app.get("/cutlery",
         response_model=List[Cutlery],
         # response_model=List[Union[Knife, Fork, Spoon]],
         )
async def get_cutlery():

    return [Knife(name='The special knife'),
            Fork(name='Two theeth fork', number_of_teeth=2),
            Fork(name='Three teeth', number_of_teeth=3),
            Spoon(name='Tea spoon', volume=3.2)]


uvicorn.run(app, host="127.0.0.1", port=80)
