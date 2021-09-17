from dataclasses import dataclass
from typing import AbstractSet, Dict, List

@dataclass
class DataClassPaper:
    Title: str
    year: str
    ML_Techniques: str
    Category : str
    Sub_category : str
    Venue : str
    Link : str
    bibtex : str
    abstract : str


@dataclass
class HomePageData:
    Header: str
    subHeader: str
    title : str
    HomePageText : str
    menu: List[str]
    categoryChart : dict
    VenueChart: dict


@dataclass
class childc:
    name: str
    value: int


@dataclass
class parentc:
    name: str
    children: List[childc]

@dataclass
class root:
    name: str
    children: List[parentc]


@dataclass
class Absdata:
    Title: str
    Abstract: str