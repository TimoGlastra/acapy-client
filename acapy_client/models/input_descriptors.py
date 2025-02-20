from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.constraints import Constraints
from ..models.input_descriptors_metadata import InputDescriptorsMetadata
from ..models.schema_input_descriptor import SchemaInputDescriptor
from ..types import UNSET, Unset

T = TypeVar("T", bound="InputDescriptors")


@attr.s(auto_attribs=True)
class InputDescriptors:
    """ """

    constraints: Union[Unset, Constraints] = UNSET
    group: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    metadata: Union[Unset, InputDescriptorsMetadata] = UNSET
    name: Union[Unset, str] = UNSET
    purpose: Union[Unset, str] = UNSET
    schema: Union[Unset, List[SchemaInputDescriptor]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        constraints: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constraints, Unset):
            constraints = self.constraints.to_dict()

        group: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group

        id = self.id
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name
        purpose = self.purpose
        schema: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = []
            for schema_item_data in self.schema:
                schema_item = schema_item_data.to_dict()

                schema.append(schema_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _constraints = d.pop("constraints", UNSET)
        constraints: Union[Unset, Constraints]
        if isinstance(_constraints, Unset):
            constraints = UNSET
        else:
            constraints = Constraints.from_dict(_constraints)

        group = cast(List[str], d.pop("group", UNSET))

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, InputDescriptorsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = InputDescriptorsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        purpose = d.pop("purpose", UNSET)

        schema = []
        _schema = d.pop("schema", UNSET)
        for schema_item_data in _schema or []:
            schema_item = SchemaInputDescriptor.from_dict(schema_item_data)

            schema.append(schema_item)

        input_descriptors = cls(
            constraints=constraints,
            group=group,
            id=id,
            metadata=metadata,
            name=name,
            purpose=purpose,
            schema=schema,
        )

        input_descriptors.additional_properties = d
        return input_descriptors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
