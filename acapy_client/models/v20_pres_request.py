from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.v20_pres_format import V20PresFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresRequest")


@attr.s(auto_attribs=True)
class V20PresRequest:
    """ """

    formats: List[V20PresFormat]
    request_presentationsattach: List[AttachDecorator]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    will_confirm: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formats = []
        for formats_item_data in self.formats:
            formats_item = formats_item_data.to_dict()

            formats.append(formats_item)

        request_presentationsattach = []
        for request_presentationsattach_item_data in self.request_presentationsattach:
            request_presentationsattach_item = request_presentationsattach_item_data.to_dict()

            request_presentationsattach.append(request_presentationsattach_item)

        id = self.id
        type = self.type
        comment = self.comment
        will_confirm = self.will_confirm

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formats": formats,
                "request_presentations~attach": request_presentationsattach,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if will_confirm is not UNSET:
            field_dict["will_confirm"] = will_confirm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        formats = []
        _formats = d.pop("formats")
        for formats_item_data in _formats:
            formats_item = V20PresFormat.from_dict(formats_item_data)

            formats.append(formats_item)

        request_presentationsattach = []
        _request_presentationsattach = d.pop("request_presentations~attach")
        for request_presentationsattach_item_data in _request_presentationsattach:
            request_presentationsattach_item = AttachDecorator.from_dict(request_presentationsattach_item_data)

            request_presentationsattach.append(request_presentationsattach_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        will_confirm = d.pop("will_confirm", UNSET)

        v20_pres_request = cls(
            formats=formats,
            request_presentationsattach=request_presentationsattach,
            id=id,
            type=type,
            comment=comment,
            will_confirm=will_confirm,
        )

        v20_pres_request.additional_properties = d
        return v20_pres_request

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
