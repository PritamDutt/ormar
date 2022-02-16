"""
The `ormar` package is an async mini ORM for Python, with support for **Postgres,
MySQL**, and **SQLite**.

The main benefit of using `ormar` are:

*  getting an **async ORM that can be used with async frameworks**
(fastapi, starlette etc.)
*  getting just **one model to maintain** - you don't have to maintain pydantic
and other orm model (sqlalchemy, peewee, gino etc.)

The goal was to create a simple ORM that can be **used directly
(as request and response models)
with `fastapi`** that bases it's data validation on pydantic.

Ormar - apart form obvious ORM in name - get it's name from ormar in swedish which means
snakes, and ormar in croatian which means cabinet.

And what's a better name for python ORM than snakes cabinet :)

"""
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s:%(name)s:%(lineno)d %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "verbose_output": {
            "formatter": "default",
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "ormar": {
            "level": "INFO",
            "handlers": [
                "verbose_output",
            ],
        },
    },
}
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

try:
    from importlib.metadata import version  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version  # type: ignore
from ormar.protocols import QuerySetProtocol, RelationProtocol  # noqa: I100
from ormar.decorators import (  # noqa: I100
    post_bulk_update,
    post_delete,
    post_relation_add,
    post_relation_remove,
    post_save,
    post_update,
    pre_delete,
    pre_relation_add,
    pre_relation_remove,
    pre_save,
    pre_update,
    property_field,
)
from ormar.exceptions import (  # noqa: I100
    ModelDefinitionError,
    ModelError,
    MultipleMatches,
    NoMatch,
)
from ormar.fields import (
    BaseField,
    BigInteger,
    Boolean,
    DECODERS_MAP,
    Date,
    DateTime,
    Decimal,
    ENCODERS_MAP,
    EncryptBackends,
    Float,
    ForeignKey,
    ForeignKeyConstraint,
    ForeignKeyField,
    IndexColumns,
    Integer,
    JSON,
    LargeBinary,
    ManyToMany,
    ManyToManyField,
    PrimaryKeyConstraint,
    SQL_ENCODERS_MAP,
    SmallInteger,
    String,
    Text,
    Time,
    UUID,
    UniqueColumns,
)  # noqa: I100
from ormar.models import ExcludableItems, Extra, Model
from ormar.models.metaclass import ModelMeta
from ormar.queryset import OrderAction, QuerySet, and_, or_
from ormar.relations import RelationType
from ormar.signals import Signal


class UndefinedType:  # pragma no cover
    def __repr__(self) -> str:
        return "OrmarUndefined"


Undefined = UndefinedType()

__version__ = version("ormar")
__all__ = [
    "Integer",
    "BigInteger",
    "SmallInteger",
    "Boolean",
    "Time",
    "Text",
    "String",
    "JSON",
    "DateTime",
    "Date",
    "Decimal",
    "Float",
    "ForeignKeyConstraint",
    "ManyToMany",
    "Model",
    "ModelDefinitionError",
    "MultipleMatches",
    "NoMatch",
    "ForeignKey",
    "QuerySet",
    "RelationType",
    "Undefined",
    "UUID",
    "UniqueColumns",
    "IndexColumns",
    "QuerySetProtocol",
    "RelationProtocol",
    "ModelMeta",
    "property_field",
    "post_bulk_update",
    "post_delete",
    "post_save",
    "post_update",
    "post_relation_add",
    "post_relation_remove",
    "pre_delete",
    "pre_save",
    "pre_update",
    "pre_relation_remove",
    "pre_relation_add",
    "Signal",
    "BaseField",
    "ManyToManyField",
    "ForeignKeyField",
    "OrderAction",
    "ExcludableItems",
    "and_",
    "or_",
    "EncryptBackends",
    "ENCODERS_MAP",
    "SQL_ENCODERS_MAP",
    "DECODERS_MAP",
    "LargeBinary",
    "PrimaryKeyConstraint",
    "ModelError",
    "Extra",
]
