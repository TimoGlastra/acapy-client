from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.credential_preview import CredentialPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialOffer")


@attr.s(auto_attribs=True)
class CredentialOffer:
    """ """

    offersattach: List[AttachDecorator]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    credential_preview: Union[Unset, CredentialPreview] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offersattach = []
        for offersattach_item_data in self.offersattach:
            offersattach_item = offersattach_item_data.to_dict()

            offersattach.append(offersattach_item)

        id = self.id
        type = self.type
        comment = self.comment
        credential_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_preview, Unset):
            credential_preview = self.credential_preview.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offers~attach": offersattach,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if credential_preview is not UNSET:
            field_dict["credential_preview"] = credential_preview

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        offersattach = []
        _offersattach = d.pop("offers~attach")
        for offersattach_item_data in _offersattach:
            offersattach_item = AttachDecorator.from_dict(offersattach_item_data)

            offersattach.append(offersattach_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        _credential_preview = d.pop("credential_preview", UNSET)
        credential_preview: Union[Unset, CredentialPreview]
        if isinstance(_credential_preview, Unset):
            credential_preview = UNSET
        else:
            credential_preview = CredentialPreview.from_dict(_credential_preview)

        credential_offer = cls(
            offersattach=offersattach,
            id=id,
            type=type,
            comment=comment,
            credential_preview=credential_preview,
        )

        credential_offer.additional_properties = d
        return credential_offer

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
